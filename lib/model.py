# Data model for

from dataclasses import dataclass, field
from lib.constants import Color
import yaml

class Model:
    def __init__(self):
        self._dirty = True
        self._subscribers = {}

    def __setattr__(self, k, v):
        if not hasattr(self, '_subscribers') or k[0] == '_':   # not initialized
            object.__setattr__(self, k, v)
            return

        if getattr(self, k, v) != v:
            object.__setattr__(self, k, v)
            object.__setattr__(self, '_dirty', True)
            self.publish('update', k, v)
        else:
            object.__setattr__(self, k, v)

    def subscribe(self, topic, fn):
        subs = self._subscribers.get(topic, [])
        if not subs:
            self._subscribers[topic] = subs
        subs.append(fn)

    def unsubscribe(self, topic, fn):
        self._subscribers[topic].remove(fn)

    def publish(self, topic, *args):
        for sub in self._subscribers.get(topic, []):
            sub(topic, *args)


@dataclass
class Attack(Model):
    damage: str = '1d1'
    range: int = 0
    blowback: int = 0


@dataclass
class Ammo(Model):
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
class Peep(Model):
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
    attacks: dict = field(default_factory=dict)

    _yaml_ignore = {'tics', 'x', 'y'}


class TextModel(Model):
    def __init__(self, text=None):
        super().__init__()
        self.text = text if text else []

    # add all arguments as a single joined line/message.
    # break newlines into separate lines
    def print(self, *args):
        s = ' '.join(str(a) for a in args)
        self.text.extend(s.split('\n'))
        self._dirty = True

    def extend(self, lines):
        for s in lines: self.text.extend(s.split('\n'))
        self._dirty = True

def _model_getstate(self):
    nocopy = getattr(self, '_yaml_ignore', {})
    ret = {}
    sdict = self.__dict__
    cdict = self.__class__.__dict__
    for k in self.__dict__:
        if k[0] == '_' or k in nocopy:
            continue
        if k in cdict and sdict[k] == cdict[k]:
            continue
        ret[k] = sdict[k]

    return ret

def _to_yaml(tag, cls):
    def fn(dpr, v):
        return dpr.represent_yaml_object(tag, v, cls)
    return fn

def _from_yaml(cls):
    def fn(ldr, node):
        return ldr.construct_yaml_object(node, cls)
    return fn


for cls in [Peep, Ammo, Attack]:
    tag = '!' + cls.__name__.lower()

    yaml.Dumper.add_representer(cls, _to_yaml(tag, cls))
    yaml.Loader.add_constructor(tag, _from_yaml(cls))

    cls.__getstate__ = _model_getstate

if __name__ == '__main__':
    p = Peep('bill')
    print(p._dirty)
    p.name = 'bill'
    print(p._dirty)
    p.name = 'bbb'
    print(p._dirty)
    # print(yaml.dump(p, sort_keys = False))