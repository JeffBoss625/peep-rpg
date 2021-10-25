from dataclasses import dataclass, field
from typing import Tuple

from lib.constants import GAME_SETTINGS
import math

from lib.stats import roll_dice


class PCLASSES:
    FIGHTER = 'FIGHTER'



@dataclass
class PaInfo:
    name: str = ''

@dataclass
class PClass:
    name: str = ''
    level_factor: float = 1.0
    regen_factor: float = 1.0
    hitdicefac: float = 1.0
    pabilities: Tuple[PaInfo, ...] = field(default_factory=tuple)
    apabilities: list = ()
    abilities: list = ()
    aabilities: list = ()


PCLASSES = [
    PClass(
        name=PCLASSES.FIGHTER,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
        pabilities=(
            PaInfo(name='rage'),
        ),
        apabilities=[],
        abilities=[],
        aabilities=[],
    )
]

@dataclass
class Pability:
    name: str = ''
    dmgboost: float = 1.0     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 1.0   #Percent speed boost
    healthreq: float = 1.0    #Percent health left required to activate
    levelreq: int = 1         #Level required to use ability


PABILITIES = [
    Pability(
        name='rage',
        dmgboost=1.5,
        speedboost=1.1,
        healthreq=0.25,
        levelreq=1,
    ),
    Pability(
        name='sp_adr',
        speedboost=2.0,
        healthreq=0.1,
        levelreq=3,
    ),
]


PABILITIES_BY_NAME = {i.name:i for i in PABILITIES}

def pability_by_name(name):
    return PABILITIES_BY_NAME[name]

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

def xptolevel_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base * math.pow(factor, i)
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

def handle_level_up(src, level, game):
    while src.level < level:
        src.maxhp += round(roll_dice(src.hitdice) * src.hitdicefac)
        src.level += 1
        game.message(f'{src.name} is now level {src.level}!')

