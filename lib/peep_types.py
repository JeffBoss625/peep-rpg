from dataclasses import dataclass, field
from typing import Tuple, Dict, Any

from lib.body import create_humanoid, RACE
from lib.peeps import Peep, Attack
from lib.constants import COLOR, GAME_SETTINGS
from lib.pclass import get_pclass, level_calc
import yaml

from lib.stat import roll_dice


@dataclass
class AttackInfo:
    name: str = ''
    damage: str = '1d1'
    range: int = 0
    reach: int = 1.5
    # blowback is multiplied by damage done and applied to attacker. positive causes damage negative
    # *heals* hit points (life drain)
    blowback: float = 0

@dataclass
class IntRange:
    lo: int = 0
    hi: int = 0

@dataclass
class LevelInfo:
    name: str = ''
    lvl_range: IntRange = field(default_factory=IntRange)


@dataclass
class PType:
    name: str = ''
    char: str = ''
    type: str = 'monster'
    fgcolor: str = COLOR.WHITE
    bgcolor: str = COLOR.BLACK
    hitdice: str = '1d1'         # initial hit points (dice) at level 0
    regen_fac: float = 1.0
    skill: float = 1.0

    # todo: move this to level info to allow different rates and limit
    hp_inc: str = '1d1'     # incremental hp per level
    skill_inc: float = 1.0  # rate of skill increase per level
    attacks: Tuple[AttackInfo,...] = field(default_factory=tuple)    # attacks available for this range of levels

    # todo: calculate these from other stats
    thaco: int = 0
    speed: int = 0
    ac: int = 0

    # todo: separate move information for projectiles
    move_tactic: str = 'hunt'
    direct: int = -1

    body_stats: Dict[str,Any] = None

    # level_info: Tuple[LevelInfo] = field(default_factory=LevelInfo)


MONSTERS = [
    # GOBLINS
    PType(
        name='goblin',
        char='g',
        type='monster',
        fgcolor=COLOR.GREEN,
        hitdice='1d6',
        regen_fac=1.0,
        thaco=18,
        speed=13,
        ac=19,
        attacks=(
            AttackInfo('bite', '1d3'),
            AttackInfo('scratch', '2d2'),
            AttackInfo('punch', '2d1'),
        ),
    ),

    # Animals
    PType(
        name='giant rat',
        char='r',
        type='monster',
        fgcolor=COLOR.YELLOW,
        hitdice='1d4',
        thaco=19,
        speed=13,
        ac=10,
        attacks=(
            AttackInfo('bite', '1d3'),
            AttackInfo('scratch', '2d2'),
            AttackInfo('tail', '2d1'),
        )
    ),

    PType(
        name='big bird',
        char='b',
        type='monster',
        fgcolor=COLOR.WHITE,
        bgcolor=COLOR.BLACK,
        hitdice='3d8',
        thaco=17,
        speed=19,
        ac=8,
        attacks=(
            AttackInfo('beak', '1d10'),
            AttackInfo('talons', '2d7'),
            AttackInfo('wing_blow', '6d1'),
        )
    ),

    # Red Dragons
    PType(
        name='red dragon',
        char='D',
        type='monster',
        fgcolor=COLOR.RED,
        bgcolor=COLOR.BLACK,
        hitdice='8d10',
        regen_fac=2.0,
        thaco=10,
        speed=20,
        ac=10,
        attacks=(
            AttackInfo('bite', '1d10'),
            AttackInfo('scratch', '2d7'),
            AttackInfo('tail', '3d5'),
            AttackInfo('fire_breath', '2d10', range=15),
        )
    ),
    # The Black Dragon
    PType(
        name='black dragon',
        char='D',
        type='monster',
        fgcolor=COLOR.BLUE,
        bgcolor=COLOR.BLACK,
        hitdice='12d10',
        thaco=3,
        speed=75,
        ac=3,
        attacks=(
            AttackInfo('bite', '1d30'),
            AttackInfo('scratch', '2d21'),
            AttackInfo('tail', '3d15'),
            AttackInfo('acid_breath', '2d30', range=15),
        ),
    ),
    PType(
        name='dog',
        char='d',
        type='monster',
        hitdice='5d10',
        thaco=19,
        speed=33,
        ac=10,
        attacks=(
            AttackInfo('teeth', '1d10'),
            AttackInfo('tail', '3d5'),
            AttackInfo('scratch', '2d7'),
        ),
    ),
    PType(
        name='dodger',
        char='d',
        type='monster',
        hitdice='1000d10',
        thaco=0,
        speed=1,
        ac=0,
        attacks=(
            AttackInfo('absolute destruction', '10d10000000'),
        ),
    ),

    PType(
        name='human',
        char='h',
        type='monster',
        hitdice='3d8',
        thaco=19,
        speed=45,
        ac=10,
        attacks=(
            AttackInfo('karate-chop', '5d8'),
            AttackInfo('head-butt', '4d4'),
            AttackInfo('arrow', '1d6', range=100)
        ),
        body_stats={
            'btype': 'humanoid',
            'height': 160,
            'weight': 90,
            'body2head': 7.5,
        }
    ),
    PType(
        name='wall',
        char='#',
        type='wall',
        fgcolor=COLOR.YELLOW,
        hitdice='20d100',
        thaco=20,
        speed=0,
        ac=100,
        attacks=(
            # AttackInfo('crush', '2d4'),
        ),
    ),

    PType(
        name='permanent wall',
        char='%',
        type='wall',
        fgcolor=COLOR.CYAN,
        hitdice='100d999999999999',
        thaco=15,
        speed=0,
        ac=100,
        attacks=(
            # AttackInfo('smush', '5d10'),
            # AttackInfo('bury', '2d12'),
        ),
    ),

    PType(
        name='arrow',
        char='-',
        type='projectile',
        fgcolor=COLOR.YELLOW,
        bgcolor=COLOR.BLACK,
        hitdice='1d2',
        thaco=20,
        speed=200,
        ac=-10,
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='fire_breath',
        char='*',
        type='projectile',
        fgcolor=COLOR.RED,
        bgcolor=COLOR.BLACK,
        hitdice='2d8',
        thaco=20,
        speed=200,
        ac=-10,
        attacks=(

        ),
        move_tactic='pos_path',
    ),
]

PTYPES_BY_NAME = {m.name:m for m in MONSTERS}

def create_attack(attack_info):
    return Attack(
        name=attack_info.name,
        damage=attack_info.damage,
        range=attack_info.range,
        blowback=attack_info.blowback,
    )

def create_peep(
        ptype,
        pclass="FIGHTER",
        name='',
        pos=(0, 0),
        body_stats=None,
        exp=0,
        attacks=(), # overrides ptype attacks if set
    ):
    pt = PTYPES_BY_NAME[ptype]
    pc = get_pclass(pclass)
    hp = roll_dice(pt.hitdice)
    factor = pc.level_factor * GAME_SETTINGS.LEVEL_UP_FACTOR
    level = level_calc(exp, factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL)
    regen_fac = pt.regen_fac
    attacks = attacks if len(attacks) else pt.attacks # todo: combine type and passed in?


    ret = Peep(
        name=name if name else 'a ' + ptype,
        type=pt.type,
        char=pt.char,
        fgcolor=pt.fgcolor,
        bgcolor=pt.bgcolor,
        hp=hp,
        maxhp=hp,
        regen_fac=regen_fac,
        exp=exp,
        level=level,
        level_factor=factor,
        hitdice=pt.hitdice,
        hitdicefac=pc.hitdicefac,
        thaco=pt.thaco,
        speed=pt.speed,
        ac=pt.ac,
        attacks=tuple(create_attack(ai) for ai in attacks),
        pos=pos,
        body=create_humanoid(**body_stats) if body_stats else None,
        move_tactic=pt.move_tactic,
    )
    return ret


if __name__ == '__main__':
    for name in PTYPES_BY_NAME:
        p = create_peep(name)
        print(p)
        # print(yaml.dump(m, sort_keys=False, default_flow_style=False))
