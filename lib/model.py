from dataclasses import dataclass, MISSING
import yaml
import re

# special value (used simply as a class, not instance) to indicate non-existent items with obj.get(key, default)
from lib.util import DotDict


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
        try:
            self._subscribers.remove(fn)
            for sm in self.submodels():
                sm.unsubscribe(fn)
        except ValueError:
            pass

    def publish(self, model, event_type, **kwds):
        for fn in self._subscribers:
            fn(model, event_type, **kwds)

    def publish_update(self, prev_val, new_val, **kwds):
        vlen = getattr(kwds, 'len', 1)  # len indicates multiple values were changed (prev and new are lists)
        prev_list = []
        new_list = []
        if prev_val:
            prev_list = [prev_val] if vlen == 1 else prev_val
        if new_val:
            new_list = [new_val] if vlen == 1 else new_val

        for s in self._subscribers:
            for pv in prev_list:
                if pv and isinstance(pv, PubSub):
                    pv.unsubscribe(s)

            for nv in new_list:
                if nv and isinstance(nv, PubSub):
                    nv.subscribe(s)

        self.publish(self, 'update', prev=prev_val, new=new_val, **kwds)

    def submodels(self):
        return []

# A dictionary that subscribes to any models put in and unsubscribes to models removed, propagating update events
# to a managed set of subscribers.
#
#
# NOTE: the dict extension only handles set and delete operations, not constructors, update etc.
# To propogate changes, callers need to confine updates to simply:
#   dict[key] = x
#   del dict[key]
#
#
class ModelDict(DotDict, PubSub):
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

    def submodels(self):
        return list(v for v in self.values() if isinstance(v, PubSub))

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
        self.extend([v])

    def extend(self, v):
        kwds = {'i': len(self)}
        vlen = len(v)
        if vlen == 0:
            return
        super().extend(v)
        if vlen == 1:
            # one item added publish the value, not the array
            v = v[0]
        else:
            # multiple items added, set len property and publish array
            kwds['len'] = vlen
        self.publish_update(None, v, **kwds)   # v is an array or tuple

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
        return list(v for v in self if isinstance(v, PubSub))

# dataclass models with change-tracking
class DataModel(PubSub):
    # ** NOTE ** __init__() must be called by @dataclass __post_init__()
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
    def __init__(self, model_name='no_name', text=None):
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

    def replace(self, lines):
        if isinstance(lines, str):
            lines = [lines]
        self.text = []
        self.extend(lines)

    def extend(self, lines):
        slines = []
        for s in lines: slines.extend(s.split('\n'))
        self.text.extend(slines)
        self.publish_update(None, lines)

    # Replace a rectangular region of text.
    #
    # xoff, yoff - column and row offsets for the upper-left corder of the replacement (inclusive)
    # lines: a block of text (same length strings)
    def replace_region(self, xoff, yoff, lines):
        text = self.text
        prev = []
        width = len(lines[0])
        for ln in lines:
            if len(ln) != width:
                raise ValueError(f'region has inconsistent line length: {width} and {len(ln)}')

        for y in range(0, len(lines)):
            nrow = lines[y]
            prow = text[yoff + y]
            prev.append(prow[xoff:xoff + width])
            text[yoff + y] = prow[0:xoff] + nrow + prow[xoff + width:]

        # should probably represent text region as an object with offset.
        self.publish_update(prev, lines)

    def char_at(self, x, y):
        return self.text[y][x]

@dataclass
class Size:
    h: int = 0
    w: int = 0
    d: int = 0

    def volume(self):
        return self.h * self.w * self.d

    @classmethod
    def from_yaml(cls, loader, node):
        v = loader.construct_scalar(node)
        h, w, d = map(int, v.split('x'))
        return Size(h, w, d)

    @classmethod
    def to_yaml(cls, dumper, v):
        return dumper.represent_scalar('!size', f'{v.h}x{v.w}x{v.d}')

    @classmethod
    def yaml_pattern(cls):
        return re.compile(r'^\d+x\d+x\d+$')

# return only values that are different from field defaults
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

def default_model_name_fn(cls):
    return cls.__name__.lower()

def register_yaml(classes):
    for cls in classes:
        cls.model_name = default_model_name_fn
        tag = getattr(cls, 'yaml_tag', '!' + cls.model_name(cls))

        to_yaml = getattr(cls, 'to_yaml', _to_yaml(tag, cls))
        yaml.Dumper.add_representer(cls, to_yaml)

        from_yaml = getattr(cls, 'from_yaml', _from_yaml(cls))
        yaml.Loader.add_constructor(tag, from_yaml)

        pat = getattr(cls, 'yaml_pattern', None)
        if pat:
            yaml.add_implicit_resolver(tag, pat())

        if not hasattr(cls, '__getstate__'):
            cls.__getstate__ = _datamodel_getstate


register_yaml([Size])
yaml.add_representer(ModelList, yaml.Dumper.yaml_representers[list], yaml.Dumper)
yaml.add_representer(ModelDict, yaml.Dumper.yaml_representers[dict], yaml.Dumper)


if __name__ == '__main__':
    Size(3,4,5)
