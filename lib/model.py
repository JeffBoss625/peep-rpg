# Data model for

from dataclasses import dataclass, field, MISSING
from lib.constants import Color
import yaml

# special value (used simply as a class, not instance) to indicate non-existent items with obj.get(key, default)
class NotSet:
    pass

class PubSub:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, fn):
        self._subscribers.append(fn)
        for sm in self.submodels():
            sm.subscribe(fn)

    def unsubscribe(self, fn):
        self._subscribers.remove(fn)
        for sm in self.submodels():
            sm.unsubscribe(fn)

    def publish(self, model, msg, **kwds):
        for fn in self._subscribers:
            fn(model, msg, **kwds)

    def publish_update(self, prev_val, new_val, **kwds):
        if prev_val and isinstance(prev_val, PubSub):
            for s in self._subscribers:
                prev_val.unsubscribe(s)
        if new_val and isinstance(new_val, PubSub):
            for s in self._subscribers:
                new_val.subscribe(s)

        self.publish(self, 'update', prev=prev_val, new=new_val, **kwds)

    def submodels(self):
        return []

# a dictionary containing models for which we will publish events when dictionary models are
# added (publishes "add" message) or removed (publishes "remove" message).
#
# NOTE: the dict extension only handles set and delete operations, not constructors, update etc.
# To propogate changes, callers need to confine updates to simply:
#   dict[key] = x
#   del dict[key]
#
#
class ModelDict(dict, PubSub):
    def __init__(self):
        super().__init__()
        PubSub.__init__(self)

    def __delitem__(self, k):
        prev = self.get(k)
        super().__delitem__(k)
        self.publish_update(prev, None, key=k)

    def __setitem__(self, k, v):
        prev = self.get(k, None)
        if prev == v:
            return
        super().__setitem__(k, v)
        self.publish_update(prev, v, key=k)

    def __getstate__(self):
        return self.copy()

    def submodels(self):
        return self.values()

class ModelList(list, PubSub):
    def __init__(self):
        super().__init__()
        PubSub.__init__(self)

    def __delitem__(self, i):
        prev = self[i]
        super().__delitem__(i)
        self.publish_update(prev, None, i=i)

    def __setitem__(self, i, v):
        prev = self[i]
        if prev == v:
            return
        super().__setitem__(i, v)
        self.publish_update(prev, v, i=i)

    def append(self, v):
        super().append(v)
        self.publish_update(None, v, i=len(self)-1)

    def remove(self, v):
        super().remove(v)
        self.publish_update(v, None)

    def pop(self, *args):
        prev = super().pop(*args)
        if len(args):
            i = args[0]
            if i < 0:
                i += len(args)
        else:
            i = len(args)-1
        self.publish_update(prev, None, i=i )

    def submodels(self):
        return self

# dataclass models with change-tracking
class DataModel(PubSub):
    # ** NOTE ** __init__() must be called by @dataclass __postinit__()
    def __init__(self):
        super().__init__()

    def __setattr__(self, k, v):
        if not hasattr(self, '_subscribers') or k[0] == '_':
            # not initialized
            object.__setattr__(self, k, v)
            return

        prev = getattr(self, k, NotSet)
        if v == prev:
            return
        if prev == NotSet:
            prev = None
        object.__setattr__(self, k, v)
        self.publish_update(prev, v, key=k)

    def submodels(self):
        ret = []
        for v in self.__dict__.values():
            if v and isinstance(v, PubSub):
                ret.append(v)
        return ret

    @classmethod
    def model_name(cls):
        return cls.__name__.lower()

def yaml_friendly(v):
    if hasattr(v, '__getstate__'):
        v = v.__getstate__()
    elif isinstance(v, tuple):
        v = list(v)
    return v

#
# YAML Serialization Functions
#

class TextModel(PubSub):
    def __init__(self, model_name, text=None):
        super().__init__()
        self.text = []
        self.model_name = model_name
        if text:
            self.extend(text)

    # add all arguments as a single joined line/message.
    # break newlines into separate lines
    def print(self, *args):
        s = ' '.join(str(a) for a in args)
        self.extend([s])

    def extend(self, lines):
        slines = []
        for s in lines: slines.extend(s.split('\n'))
        self.text.extend(slines)
        self.publish_update(None, lines)


def _datamodel_getstate(self):
    sdict = self.__dict__
    fields = self.__class__.__dataclass_fields__

    nocopy = getattr(dict, '_yaml_ignore', {})
    ret = {}
    for k in sdict:
        if k[0] == '_' or k in nocopy:
            continue
        v = sdict[k]
        if k in fields:
            fld = fields[k]
            if fld.default != MISSING:
                if v == fld.default:
                    continue
            elif v == fld.default_factory():
                continue

        ret[k] = yaml_friendly(v)
    return ret

def _to_yaml(tag, cls):
    def fn(dpr, v):
        return dpr.represent_yaml_object(tag, v, cls)
    return fn

def _from_yaml(cls):
    def fn(ldr, node):
        return ldr.construct_yaml_object(node, cls)
    return fn

def register_yaml(cls):
    tag = '!' + cls.model_name()

    yaml.Dumper.add_representer(cls, _to_yaml(tag, cls))
    yaml.Loader.add_constructor(tag, _from_yaml(cls))

    cls.__getstate__ = _datamodel_getstate
