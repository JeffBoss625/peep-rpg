from dataclasses import dataclass, field
from typing import Tuple, List

from lib.constants import GAME_SETTINGS
import math

from lib.stats import roll_dice


class PCLASSES:
    FIGHTER = 'FIGHTER'



@dataclass
class Ability:
    name: str = ''
    isactive: bool = False

@dataclass
class PClass:
    name: str = ''
    level_factor: float = 1.0
    regen_factor: float = 1.0
    hitdicefac: float = 1.0
    abilitiesbylevel: List = field(default_factory=list)
    states: list = ()


PCLASSES = [
    PClass(
        name=PCLASSES.FIGHTER,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
        abilitiesbylevel=[
            [], #Level zero abilities
            [Ability(name='rage', isactive=False)],
        ],
        states=[],
    )
]

@dataclass
class Pability:
    name: str = ''
    state: str = ''
    duration: int = 1
    healthreq: float = 1.0    #Percent health left required to activate
    levelreq: int = 1         #Level required to use ability

@dataclass
class PeepState:
    name: str = ''
    duration: float = 1.0
    dmgboost: float = 1.0     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 0.1   #Percent speed boost


PEEPSTATES = [
    PeepState(
        name='Enraged',
        dmgboost=1.5,
        speedboost=.1,
    )
]


PABILITIES = [
    Pability(
        name='rage',
        state='Enraged',
        duration=3,
        healthreq=0.25,
        levelreq=1,
    ),
    Pability(
        name='sp_adr',
        state='Adr_Pump',
        healthreq=0.1,
        levelreq=3,
    ),
]


PABILITIES_BY_NAME = {i.name:i for i in PABILITIES}

def pability_by_name(name):
    return PABILITIES_BY_NAME[name]

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

PEEPSTATES_BY_NAME = {m.name:m for m in PEEPSTATES}

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

def peep_acquire_abilities(src, lvl):
    abilities = src.pclass.abilitiesbylevel[lvl]
    for ability in abilities:
        if ability:
            if ability.isactive:
                src.aabilities.append(ability)
            else:
                src.pabilities.append(PABILITIES_BY_NAME[ability.name])

def activate_pability(peep, pability):
    if peep.hp <= pability.healthreq * peep.maxhp:
        if peep.states:
            for s in peep.states:
                if s.name == pability.state:
                    if s.duration <= pability.duration:
                        peep.states.remove(s)
                        state = PEEPSTATES_BY_NAME[pability.state]
                        state.duration = pability.duration
                        peep.states.append(state)
                        peep.speed = peep.speed + state.speedboost
                else:
                    state = PEEPSTATES_BY_NAME[pability.state]
                    state.duration = pability.duration
                    peep.states.append(state)
                    peep.speed = peep.speed + state.speedboost
        else:
            state = PEEPSTATES_BY_NAME[pability.state]
            state.duration = pability.duration
            peep.states.append(state)
            peep.speed = peep.speed + state.speedboost


def check_states(peep, state, inc):
    state.duration -= inc
    if state.duration <= 0:
        peep.states.remove(state)
        peep.speed = peep.speed - state.speedboost

