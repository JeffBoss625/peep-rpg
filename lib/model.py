# Data model for

from dataclasses import dataclass, field
from lib.constants import Color
import yaml

class PubSub:
    def __init__(self):
        self._subscribers = {}  # subscribers by topic

    def subscribe(self, topic, fn):
        subs = self._subscribers.get(topic, [])
        if not subs:
            self._subscribers[topic] = subs
        subs.append(fn)

    def unsubscribe(self, topic, fn):
        self._subscribers[topic].remove(fn)

    def publish(self, model_name, *args):
        for fn in self._subscribers.get(model_name, []):
            fn(model_name, *args)


# a dictionary containing models for which we will publish events when dictionary entries change.
class MDict(dict, PubSub):
    def __init__(self):
        super().__init__()
        PubSub.__init__(self)

    def __delitem__(self, k):
        prev = self.get(k)
        super().__delitem__(k)
        self.publish(prev.model_name(), 'delete', k, prev)

    def __setitem__(self, k, v):
        mname = v.model_name()
        prev = self.get(k, None)
        if prev == v:
            return
        super().__setitem__(k, v)
        if prev:
            self.publish(mname, 'replace', k, prev, v)
        else:
            self.publish(mname, 'add', k, v)


# dataclass models with change-tracking, yaml serialization and update event publication
# topic is often the class name (lower case)
class DataModel(PubSub):
    def __init__(self):
        super().__init__()

    def __setattr__(self, k, v):
        if hasattr(self, '_subscribers') and k[0] != '_' and getattr(self, k, v) != v:
            object.__setattr__(self, k, v)
            self.publish(self.model_name(), 'update', k, v)
        else:
            object.__setattr__(self, k, v)

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
    attacks: dict = field(default_factory=lambda: MDict())

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
        self.publish(self.model_name, 'extend', slines)

def _getstate(sdict, cdict):
    nocopy = getattr(dict, '_yaml_ignore', {})
    ret = {}
    for k in sdict:
        if k[0] == '_' or k in nocopy:
            continue
        v = sdict[k]
        if k in cdict and v == cdict[k]:
            continue

        if isinstance(v, MDict):
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


for cls in [Peep, Ammo, Attack]:
    tag = '!' + cls.model_name()

    yaml.Dumper.add_representer(cls, _to_yaml(tag, cls))
    yaml.Loader.add_constructor(tag, _from_yaml(cls))

    cls.__getstate__ = _model_getstate

def printargs(*args):
    print(args)


if __name__ == '__main__':
    p = Peep('bill')
    p.subscribe('peep', printargs)
    p.name = 'bill'
    p.name = 'bbb'

    a = MDict()
    a.subscribe('attack', printargs)
    a['bite'] = Attack('3d4', 4)
    del a['bite']
    print(a)
    print(yaml.dump(p, sort_keys = False))