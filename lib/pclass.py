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
            [Ability(name='charge', isactive=True)], #Level zero abilities
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

@dataclass
class Ability:
    name: str = ''
    state: str = ''
    duration: int = 1
    healthreq: float = 1.0
    cooldown: int = 1
    halt_hit: bool = False
    time_activated: float = -100     #based on peep age

@dataclass
class PeepState:
    name: str = ''
    duration: float = 1.0


@dataclass
class PeepCharging (PeepState):
    name: str = 'charging'
    duration: float = 30
    dmgboost: float = 1.0     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 0.1   #Percent speed boost
    maxcompounded: int = 5
    compounded: int = 0
    path: bool = True
    num_mult: int = 0

@dataclass
class PeepEnraged (PeepState):
    dmgboost: float = 1.0     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 0.1   #Percent speed boost
    path: bool = False
    num_mult: int = 0

@dataclass
class ability_charge(Ability):
    name: str = 'charge'
    state: str = 'charging'
    duration: int = 100
    cooldown: int = 20
    halt_hit: int = True


PABILITIES = [
    Pability(
        name='rage',
        state='enraged',
        duration=3,
        healthreq=0.25,
    ),
    Pability(
        name='sp_adr',
        state='Adr_Pump',
        healthreq=0.1,
    ),
]

ABILITIES_BY_NAME = {
    'charge': ability_charge,

}
PABILITIES_BY_NAME = {i.name:i for i in PABILITIES}

def pability_by_name(name):
    return PABILITIES_BY_NAME[name]

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

STATECLASSES_BY_NAME = {
    'enraged': PeepEnraged,
    'charging': PeepCharging,
}

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
                src.aabilities.append(ABILITIES_BY_NAME[ability.name])
            else:
                src.pabilities.append(PABILITIES_BY_NAME[ability.name])

def activate_pability(peep, pability):
    state = STATECLASSES_BY_NAME[pability.state]()
    if peep.hp <= pability.healthreq * peep.maxhp:
        if peep.states:
            for s in peep.states:
                if s.name == pability.state:
                    if s.duration <= pability.duration:
                        if s.compounded < s.maxcompounded:
                            state.duration = pability.duration
                            peep.speed = peep.speed - s.speedboost
                            s.speedboost += state.speedboost
                            s.dmgboost = s.dmgboost + (state.dmgboost - 1)
                            peep.speed = peep.speed + s.speedboost
                        else:
                            state.duration = pability.duration
                else:
                    state.duration = pability.duration
                    peep.states.append(state)
                    peep.speed = peep.speed + state.speedboost
                    break
        else:
            state.duration = pability.duration
            peep.states.append(state)
            peep.speed = peep.speed + state.speedboost

# todo: Make states into dictionary

def activate_ability(peep, ability):
    for a in peep.aabilities:
        if a.name == ability.name:
            time_elapsed = peep._age - a.time_activated
            if time_elapsed < ability.cooldown:
                return None
    state = STATECLASSES_BY_NAME[ability.state]()
    if peep.hp <= ability.healthreq * peep.maxhp:
        if peep.states:
            for s in peep.states:
                if s.name == ability.state:
                    if s.duration <= ability.duration:
                        if s.compounded < s.maxcompounded - 1:
                            s.compounded += 1
                            state.duration = ability.duration
                            peep.speed = peep.speed - s.speedboost
                            s.speedboost += state.speedboost
                            s.dmgboost = s.dmgboost + (state.dmgboost - 1)
                            peep.speed = peep.speed + s.speedboost
                            ability.time_activated = peep._age
                        else:
                            state.duration = ability.duration
                            ability.time_activated = peep._age
                else:
                    state.duration = ability.duration
                    ability.time_activated = peep._age
                    break
        else:
            state.duration = ability.duration
            ability.time_activated = peep._age
            peep.states.append(state)
            peep.speed = peep.speed + state.speedboost
    return True

def check_states(peep, state, inc):
    state.duration -= inc
    if state.duration <= 0:
        remove_state(peep, state)

def remove_state(peep, state):
    peep.states.remove(state)
    peep.speed = peep.speed - state.speedboost

def check_line(peep, x, y, state):
    change_x = peep.pos[0] - peep.prev_pos[0]
    change_y = peep.pos[1] - peep.prev_pos[1]
    if x - peep.pos[0] == change_x and y - peep.pos[1] == change_y:
        return True
    else:
        remove_state(peep, state)
        return False
