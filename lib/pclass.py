from dataclasses import dataclass

import math


class PCLASSES:
    FIGHTER = 'FIGHTER'

@dataclass
class PClass:
    name: str = ''
    level_factor: float = 1.0
    regen_factor: float = 1.0
    hit_dice: str = '1d8'


PCLASSES = [
    PClass(
        name=PCLASSES.FIGHTER,
        level_factor=1.0,
        regen_factor=1.0,
        hit_dice='1d8',
    )
]

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

def level_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base*math.pow(factor, i)
        ret += addon
    return ret


def get_pclass(name):
    return PCLASSES_BY_NAME[name]
