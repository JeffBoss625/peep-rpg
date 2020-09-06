# Data model for

import dataclasses as dclib
from lib.constants import Color

@dclib.dataclass
class Attack:
    damage: str = '1d1'
    range: int = 0
    blowback: int = 0

@dclib.dataclass
class Ammo:
    name: str = ''
    char: str = '?'
    fgcolor: Color = Color.WHITE
    bgcolor: Color = Color.BLACK
    thaco: int = 20
    speed: int = 100
    ac: int = 20
    maxhp: int = 1

    # temp state
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = dclib.field(default_factory=dict)
    move_tactic: str = 'straight'
    direct: int = 0

@dclib.dataclass
class Peep:
    name: str = ''
    type: str = ''
    char: str = '?'
    fgcolor: Color = Color.WHITE
    bgcolor: Color = Color.BLACK
    maxhp: int = 0
    thaco: int = 20
    speed: int = 10
    ac: int = 10
    move_tactic: str = 'seek'
    # temp state
    hp: int = 0
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = dclib.field(default_factory=dict)


# CONSTRUCTION FROM DICTIONARY LOGIC - ignore
CLASS_FIELDS = {}

def _class_fields(klass):
    if klass not in CLASS_FIELDS:
        CLASS_FIELDS[klass] = {f.name: f.type for f in dclib.fields(klass)}
    return CLASS_FIELDS[klass]

def from_dict(klass, d):
    if not dclib.is_dataclass(klass):
        return d
    fields = _class_fields(klass)
    args = {}
    for f in d:
        if f not in fields:
            raise KeyError(str(klass.__name__) + ' has no property "' + f + '"')
        args[f] = from_dict(fields[f], d[f])

    ret = klass(**args)
    return ret
