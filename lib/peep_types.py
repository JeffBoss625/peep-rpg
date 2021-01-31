from dataclasses import dataclass, field
from typing import Tuple, Dict, Any

from lib.body import create_humanoid, RACE
from lib.peeps import Peep, Attack
from lib.constants import COLOR
from lib.constants import PCLASS
from lib.pclass import get_pclass
import yaml

from lib.stat import roll_dice


@dataclass
class AttackInfo:
    name: str = ''
    damage: str = '1d1'
    range: int = 0
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
    hp: str = '1d1'         # initial hit points (dice) at level 0
    regen: float = 1.0
    exp: float = 0
    level: int = 1
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
        hp='1d6',
        regen=1.0,
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
        hp='1d4',
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
        hp='3d8',
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
        hp='8d10',
        regen=2.0,
        thaco=10,
        speed=20,
        ac=10,
        attacks=(
            AttackInfo('bite', '1d10'),
            AttackInfo('scratch', '2d7'),
            AttackInfo('tail', '3d5'),
            AttackInfo('fire_breath', '2d10', range=5),
        )
    ),
    # The Black Dragon
    PType(
        name='black dragon',
        char='D',
        type='monster',
        fgcolor=COLOR.BLUE,
        bgcolor=COLOR.BLACK,
        hp='12d10',
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
        hp='5d10',
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
        hp='1000d10',
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
        hp='3d8',
        thaco=19,
        speed=45,
        ac=10,
        attacks=(
            AttackInfo('karate-chop', '5d8'),
            AttackInfo('head-butt', '4d4'),
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
        hp='20d100',
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
        hp='100d999999999999',
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
        hp='1d2',
        thaco=20,
        speed=200,
        ac=-10,
        attacks=(
            AttackInfo(name='hit', damage='1d6', blowback=2.0),
        ),
        move_tactic='straight',
    ),
    PType(
        name='fire breath',
        char='*',
        type='projectile',
        fgcolor=COLOR.RED,
        bgcolor=COLOR.BLACK,
        hp='2d8',
        thaco=20,
        speed=200,
        ac=-10,
        attacks=(
            AttackInfo(name='burn', damage='3d6', blowback=10.0),
        ),
        move_tactic='straight',
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

def create_peep(ptype, pclass=PCLASS.FIGHTER, name='', pos=(0, 0), body_stats=None, seed=0):
    pt = PTYPES_BY_NAME[ptype]
    pc = get_pclass(pclass)
    hp = roll_dice(pt.hp)

    ret = Peep(
        name=name if name else 'a ' + ptype,
        type=pt.type,
        char=pt.char,
        fgcolor=pt.fgcolor,
        bgcolor=pt.bgcolor,
        hp=hp,
        maxhp=hp,
        thaco=pt.thaco,
        speed=pt.speed,
        ac=pt.ac,
        attacks=tuple(create_attack(ai) for ai in pt.attacks),
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
