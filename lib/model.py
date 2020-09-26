# Data model for

from dataclasses import dataclass, field
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

    def unsubscribe(self, fn):
        self._subscribers.remove(fn)

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

    def subscribe(self, fn):
        for m in self:
            m.subscribe(fn)
        super().subscribe(fn)

    def unsubscribe(self, fn):
        for m in self:
            m.unsubscribe(fn)
        super().unsubscribe(fn)

# dataclass models with change-tracking
class DataModel(PubSub):
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

    @classmethod
    def model_name(cls):
        return cls.__name__.lower()

@dataclass(frozen=True)
class Attack(DataModel):
    damage: str = '1d1'
    range: int = 0
    blowback: int = 0


@dataclass()
class Ammo(DataModel):
    name: str = ''
    char: str = '?'
    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK
    thaco: int = 20
    speed: int = 100
    ac: int = 20
    maxhp: int = 1

    # temp state
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = field(default_factory=dict)
    move_tactic: str = 'straight'
    direct: int = 0

@dataclass
class Peep(DataModel):
    def __post_init__(self):
        super().__init__()

    name: str = ''
    type: str = ''
    char: str = '?'
    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK
    maxhp: int = 0
    thaco: int = 20
    speed: int = 10
    ac: int = 10
    move_tactic: str = 'seek'

    # temp state
    # todo: original state and current state - maintain both
    hp: int = 0
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = field(default_factory=lambda: ModelDict())

    _yaml_ignore = {'tics', 'x', 'y'}


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
        self.publish(self, 'update', added=slines)

#
# YAML Serialization Functions
#
def _getstate(sdict, cdict):
    nocopy = getattr(dict, '_yaml_ignore', {})
    ret = {}
    for k in sdict:
        if k[0] == '_' or k in nocopy:
            continue
        v = sdict[k]
        if k in cdict and v == cdict[k]:
            continue

        if isinstance(v, ModelDict):
            v = v.copy()    # as regular dict
        ret[k] = v

    return ret

def _model_getstate(self):
    return _getstate(self.__dict__, self.__class__.__dict__)

def _to_yaml(tag, cls):
    def fn(dpr, v):
        return dpr.represent_yaml_object(tag, v, cls)
    return fn

def _from_yaml(cls):
    def fn(ldr, node):
        return ldr.construct_yaml_object(node, cls)
    return fn

def reg(cls):
    tag = '!' + cls.model_name()

    yaml.Dumper.add_representer(cls, _to_yaml(tag, cls))
    yaml.Loader.add_constructor(tag, _from_yaml(cls))

    cls.__getstate__ = _model_getstate

def init_cls():
    for cls in [Peep, Ammo, Attack]:
        reg(cls)

def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


if __name__ == '__main__':
    p = Peep('bill')
    p.subscribe(printargs)
    p.name = 'bill'
    p.name = 'bbb'
    p.hp = 2
    p.hp = 2

    # a = ModelDict()
    # a.subscribe(printargs)
    # a['bite'] = Attack('3d4', 4)
    # del a['bite']
    # print(a)
    # print(yaml.dump(p, sort_keys = False))