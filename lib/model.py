# Data model for

from dataclasses import dataclass, field
from lib.constants import Color
from yaml import YAMLObject

@dataclass
class Attack(YAMLObject):
    yaml_tag = '!attack'
    damage: str = '1d1'
    range: int = 0
    blowback: int = 0

    def __getstate__(self):
        return uniq_state(self, {})

@dataclass
class Ammo(YAMLObject):
    yaml_tag = '!ammo'
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

    def __getstate__(self):
        return uniq_state(self, {})

@dataclass
class Peep(YAMLObject):
    yaml_tag = '!peep'
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
    # todo: natural state and temp state - maintain both
    hp: int = 0
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = field(default_factory=dict)

    def __getstate__(self):
        return uniq_state(self, {'tics', 'x', 'y'})

def uniq_state(obj, nocopy):
    ret = {}
    sdict = obj.__dict__
    cdict = obj.__class__.__dict__
    for k in obj.__dict__:
        if k not in cdict or (sdict[k] != cdict[k] and k not in nocopy):
            ret[k] = sdict[k]

    return ret


