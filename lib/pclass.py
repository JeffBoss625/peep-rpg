from dataclasses import dataclass, field
from random import randint
from typing import Tuple, List

from lib.constants import GAME_SETTINGS
import math

from lib.direction import direction_from_vector, direction_to_dxdy
from lib.stats import roll_dice


class PCLASSES:
    FIGHTER = 'FIGHTER'
    THIEF = 'THIEF'
    RANGER = 'RANGER'


@dataclass
class PClass:
    name: str = ''
    level_factor: float = 1.0
    regen_factor: float = 1.0
    hitdicefac: float = 1.0
    abilitiesbylevel: List = field(default_factory=list)
    states: list = ()


@dataclass
class Ability:
    name: str = ''
    isactive: bool = False
    time_activated: float = -100

    def handle_move_into_monster(self, src, dst, game):
        return False #continue to attack tgt

    def __str__(self):
        return self.name[0].upper() + self.name[1:]


@dataclass
class AbilityCharge(Ability):
    name: str = 'charge'
    state: str = 'charging'
    duration: int = 100
    cooldown: int = 20
    halt_hit: int = True
    isactive: bool = True
    time_activated: float = -100

    def compound(self, peep):
        for s in peep.states:
            if s.name == self.state:
                for a in peep.aabilities:
                    if a.name == self.name:
                        activate_ability(peep, a, False)

@dataclass
class AbilityBypass(Ability):
    name: str = 'bypass'
    state: str = 'bypassing'
    duration: float = 0.1
    cooldown: int = 5
    isactive: bool = True
    time_activated: float = -100
    halt_hit = False

@dataclass
class AbilityQuickshot(Ability):
    name: str = 'quickshot'
    state: str = 'quickshooting'
    duration: float = 5
    cooldown: int = 15
    isactive: bool = True
    time_activated: float = -100
    halt_hit = False


    # todo: Refactor activate_ability into the abilities themselves.


PCLASSES = [
    PClass(
        name=PCLASSES.FIGHTER,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
        abilitiesbylevel=[
            [AbilityCharge()], #Level zero abilities
            [Ability(name='rage', isactive=False)],
        ],
        states=[],
    ),
    PClass(
        name=PCLASSES.THIEF,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
        abilitiesbylevel=[
            [AbilityBypass()],
            [Ability(name='backstab', isactive=False)]
    ],
    ),
    PClass(
        name=PCLASSES.RANGER,
        level_factor=1.0,
        regen_factor=1.0,
        hitdicefac=1.0,
        abilitiesbylevel=[
            [AbilityQuickshot()],
            [Ability(name='backstab', isactive=False)]
    ],
    )
]

@dataclass
class PAbility:
    name: str = ''
    state: str = ''
    duration: int = 1
    healthreq: float = 1.0    #Percent health left required to activate

    def activate(self, peep):
        raise NotImplementedError('needs to be defined in subclass')

@dataclass
class PeepState:
    name: str = ''
    duration: float = 1.0

    def handle_move_into_monster(self, src, dst, state, game):
        return False #continue to attack tgt


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

    def handle_move_into_monster(self, src, dst, state, game):
        x_mod = (dst.pos[0] - src.pos[0])
        y_mod = (dst.pos[1] - src.pos[1])
        target_pos = (src.pos[0] + x_mod * 2, src.pos[1] + y_mod * 2)
        if game.maze_model.peep_at(target_pos):
            dst.pos = (target_pos[0], target_pos[1])
            moving_peep = game.maze_model.peep_at(target_pos)
            target_pos = (target_pos[0] + x_mod, target_pos[1] + y_mod)
            while game.maze_model.peep_at(target_pos):
                moving_peep.pos = (target_pos[0], target_pos[1])
                target_pos = (target_pos[0] + x_mod, target_pos[1] + y_mod)
                if game.maze_model.peep_at(target_pos):
                    moving_peep = game.maze_model.peep_at(target_pos)
                else:
                    break
        elif game.maze_model.wall_at(target_pos):
            pass
        else:
            src.pos = target_pos
        return False

class PAbilityRage (PAbility):
    name: str = 'rage'
    state: str = 'enraged'
    duration: float = 3
    healthreq: float = .4

    def activate(self, peep):
        if peep.hp <= self.healthreq * peep.maxhp and peep.hp > 0:
            print('hi')


class PAbilityBackstab (PAbility):
    name: str = 'backstab'
    state: str = 'backstabbing'
    duration: float = 10
    healthreq: float = 1.0


class PabilitySpeed_Adr (PAbility):
    name: str = 'speed_adr'
    state: str = 'adr_pump'
    duration: float = 10
    healthreq: float = .2


@dataclass
class PeepBypassing (PeepState):
    name: str = 'bypassing'
    dmgboost: float = 1.0
    hpboost: float = 1.0
    speedboost: float = 0
    maxcompounded: int = 1
    compounded: int = 0
    path: bool = False
    num_mult: int = 0

    def handle_move_into_monster(self, src, dst, state, game):
        x_mod = (dst.pos[0]-src.pos[0]) * 2
        y_mod = (dst.pos[1]-src.pos[1]) * 2
        target_pos = (src.pos[0]+x_mod, src.pos[1]+y_mod)
        if game.maze_model.peep_at(target_pos):
            target_pos = list(dst.pos)
            dst.pos = src.pos
            src.pos = (target_pos[0], target_pos[1])
        elif game.maze_model.wall_at(target_pos):
            target_pos = list(dst.pos)
            dst.pos = src.pos
            src.pos = (target_pos[0], target_pos[1])
        else:
            src.pos = target_pos
        src.states.remove(state)
        return True #no attacks

@dataclass
class PeepBackstabbing (PeepState):
    name: str = 'backstabbing'
    dmgboost: float = 1.0
    hpboost: float = 1.0
    speedboost: float = 0
    maxcompounded: int = 1
    compounded: int = 0
    path: bool = False
    num_mult: int = 0
    backstab: bool = True

    def handle_move_into_monster(self, src, dst, state, game):
        dst_facing = direction_to_dxdy(dst.direct)
        src_facing = direction_to_dxdy(src.direct)
        if dst_facing == src_facing:
            random = randint(0, 1)  # chance to not backstab
            if random == 0:
                state.dmgboost = 2.0
            else:
                state.dmgboost = 1.0
                if src == game.player:
                    game.message("Your backstab missed! Your attack does normal damage.")
        elif dst_facing[0] == src_facing[0]:
            random = randint(0, 1)  # chance to not backstab
            if random == 0:
                state.dmgboost = 1.5
            else:
                state.dmgboost = 1.0
                if src == game.player:
                    game.message("Your backstab missed! Your attack does normal damage.")
        elif dst_facing[1] == src_facing[1]:
            random = randint(0, 1)  # chance to not backstab
            if random == 0:
                state.dmgboost = 1.5
            else:
                state.dmgboost = 1.0
                if src == game.player:
                    game.message("Your backstab missed! Your attack does normal damage.")
        return False

@dataclass
class PeepEnraged (PeepState):
    name: str = 'enraged'
    dmgboost: float = 1.3     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 0.1   #Percent speed boost
    maxcompounded: int = 3
    compounded: int = 0
    path: bool = False
    num_mult: int = 0

    def handle_move_into_monster(self, src, dst, state, game):
        return False

class PeepQuickshooting (PeepState):
    def __init__(self):
        self.data = []
    name: str = 'quickshooting'
    dmgboost: float = 1.3     #Percent dmg boost
    hpboost: float = 1.0      #Percent hp boost
    speedboost: float = 0   #Percent speed boost
    maxcompounded: int = 3
    compounded: int = 0
    path: bool = False
    num_mult: int = 0
    _duration: int = 5

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, v):
        self._duration = v

    def handle_move_into_monster(self, src, dst, state, game):
        return False

    @staticmethod
    def handle_activated(self, peep):
        for attack in peep.attacks:
            if attack.range > 0:
                attack.speed *= 2

    @staticmethod
    def handle_deactivated(self, peep):
        for attack in peep.attacks:
            if attack.range > 0:
                attack.speed *= 0.5

@dataclass
class PeepSleeping (PeepState):
    name: str = 'sleeping'
    dmgboost: float = 1.0
    hpboost: float = 1.0
    speedboost: float = 0
    maxcompounded: int = 1
    compounded: int = 0
    path: bool = False
    num_mult: int = 0

    sleepiness: int = 1
    max_sleepiness: int = 500
    age_checked: int = 0

    def handle_sound_processed(self, peep, sound):
        sound_threshold = self.sleepiness * 0.1
        if sound >= sound_threshold:
            self.sleepiness -= sound
            if self.sleepiness <= 0:
                peep.states.remove(self)
        else:
            pass

    def handle_elapse_time(self, control):
        time_passed = control.player.age - self.age_checked
        self.sleepiness += 25 * time_passed
        if self.sleepiness >= 500: self.sleepiness = 500
        self.age_checked = control.player.age

    def handle_hit(self, peep):
        self.sleepiness -= 500
        if self.sleepiness <= 0:
            peep.states.remove(self)



ABILITIES_BY_NAME = {
    'charge': AbilityCharge,
    'bypass': AbilityBypass,
    'quickshot': AbilityQuickshot
}

PABILITIES_BY_NAME = {
    'rage': PAbilityRage,
    'speed_adr': PabilitySpeed_Adr,
    'backstab': PAbilityBackstab,
}

PCLASSES_BY_NAME = {m.name:m for m in PCLASSES}

STATECLASSES_BY_NAME = {
    'enraged': PeepEnraged,
    'charging': PeepCharging,
    'backstabbing': PeepBackstabbing,
    'bypassing': PeepBypassing,
    'quickshooting': PeepQuickshooting,
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
                src.aabilities.append(ability)
            else:
                src.pabilities.append(PABILITIES_BY_NAME[ability.name])

def activate_pability(peep, pability):
    state = STATECLASSES_BY_NAME[pability.state]()
    if peep.hp <= pability.healthreq * peep.maxhp and peep.hp > 0:
        if peep.states:
            for s in peep.states:
                if s.name == pability.state:
                    if s.compounded < s.maxcompounded - 1:
                        s.compounded += 1
                        peep.speed = peep.speed - s.speedboost
                        s.speedboost += state.speedboost
                        s.dmgboost = s.dmgboost + (state.dmgboost - 1)
                        peep.speed = peep.speed + s.speedboost

                    s.duration = pability.duration
        else:
            peep.states.append(state)
            peep.speed = peep.speed + state.speedboost
# todo: Make states into dictionary

def activate_ability(peep, ability, cooldown_check=True):
    if cooldown_check:
        for a in peep.aabilities:
            if a.name == ability.name:
                time_elapsed = peep._age - a.time_activated
                if time_elapsed < ability.cooldown:
                    return None
    state = STATECLASSES_BY_NAME[ability.state]()
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
                    else:
                        state.duration = ability.duration

                    ability.time_activated = peep._age
                    break
                else:
                    state.duration = ability.duration
                    ability.time_activated = peep._age
                    break
            else:
                state.duration = ability.duration
                ability.time_activated = peep._age
                peep.states.append(state)
                peep.speed = peep.speed + state.speedboost
    else:
        state.duration = ability.duration
        ability.time_activated = peep._age
        peep.states.append(state)
        peep.speed = peep.speed + state.speedboost

    return True

def check_states(peep, state, inc):
    state.duration -= inc
    if state.duration <= 0:
        if hasattr(state, 'handle_deactivated'):
            state.handle_deactivated(None, peep)
            pass
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
        if hasattr(state, 'handle_deactivated'):
            state.handle_deactivated(None, peep)
        remove_state(peep, state)
        return False
