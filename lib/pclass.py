from dataclasses import dataclass
from lib.constants import GAME_SETTINGS
import math


class PCLASSES:
    FIGHTER = 'FIGHTER'

@dataclass
class PClass:
    name: str = ''
    level_factor: float = 1.0
    regen_factor: float = 1.0
    hitdicefac: float = 1.0


PCLASSES = [
    PClass(
        name=PCLASSES.FIGHTER,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
    )
]

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

def xptolevel_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base*math.pow(factor, i)
        ret += addon
    return ret

def level_calc(xp, factor, base):
    ret = 1
    to_level = base - 1
    while to_level < xp:
        to_level = xptolevel_calc(ret + 1, factor, base) - 1
        ret += 1
    return ret

def get_pclass(name):
    return PCLASSES_BY_NAME[name]
