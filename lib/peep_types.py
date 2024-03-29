from dataclasses import dataclass, field
from typing import Tuple, Dict, Any, List
from lib.attack import AttackInfo
from lib.body import create_body
from lib.items import weapons
from lib.model import Size
from lib.peeps import Peep, Attack
from lib.constants import COLOR, GAME_SETTINGS
from lib.pclass import get_pclass, level_calc, peep_acquire_abilities
from lib.stats import roll_dice, Stats


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
    height: int = 5
    pclass: str = 'FIGHTER'

    # todo: move this to level info to allow different rates and limit
    hp_inc: str = '1d1'     # incremental hp per level
    skill_inc: float = 1.0  # rate of skill increase per level
    attacks: Tuple[AttackInfo, ...] = field(default_factory=tuple)    # attacks available for this range of levels

    # todo: calculate these from other stats
    thaco: int = 0
    speed: float = 0
    ac: int = 0
    statscur: Stats = field(default_factory=Stats)
    stats: Stats = field(default_factory=Stats)
    pabilities: List[Any] = field(default_factory=list)
    aabilities:List[Any] = field(default_factory=list)
    states: List[Any] = field(default_factory=list)

    # todo: separate move information for projectiles
    move_tactic: str = 'hunt'
    hunt_target: any =  None
    direct: int = -1
    shooter: Peep = None
    gold: str = '1d1'
    brightness: int = 0

    body_stats: Dict[str,Any] = None
    stuff: List[Any] = field(default_factory=list)

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
        speed=1.3,
        ac=19,
        gold="500d4",
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
        speed=1.3,
        ac=10,
        gold="0d1",
        attacks=(
            AttackInfo('bite', '1d1', speed=3),
            # AttackInfo('scratch', '2d2'),
            # AttackInfo('tail', '2d1'),
        )
    ),

    PType(
        name='giant rat leader',
        char='R',
        type='monster',
        fgcolor=COLOR.YELLOW,
        hitdice='3d12',
        thaco=19,
        speed=4.0,
        ac=10,
        gold="10d2",
        attacks=(
            AttackInfo('bite', '2d4'),
            AttackInfo('scratch', '4d2'),
            AttackInfo('tail', '8d1'),
        )
    ),

    PType(
        name='big bird',
        char='b',
        type='monster',
        fgcolor=COLOR.WHITE,
        bgcolor=COLOR.BLACK,
        hitdice='5d10',
        thaco=17,
        speed=1.5,
        ac=8,
        gold="10d3",
        attacks=(
            AttackInfo('beak', '1d10'),
            AttackInfo('talons', '2d3'),
            AttackInfo('wing_blow', '5d1', speed=0.95,),
            AttackInfo('air_strike', '3d1', speed=0.2, range=7, blowback=100)
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
        speed=2.0,
        ac=10,
        gold="500d2",
        attacks=(
            AttackInfo('bite', '1d10'),
            AttackInfo('scratch', '2d7'),
            AttackInfo('tail', '3d5'),
            AttackInfo('fire_breath', '2d10', speed=0.2, range=15, blowback=100),
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
        speed=7.5,
        ac=3,
        gold="500d3",
        attacks=(
            AttackInfo('bite', '1d30'),
            AttackInfo('scratch', '2d21'),
            AttackInfo('tail', '3d15'),
            AttackInfo('acid_breath', '2d30', speed=0.2, range=15, blowback=100),
        ),
    ),
    PType(
        name='multi-hued dragon',
        char='D',
        type='monster',
        fgcolor=COLOR.CYAN,
        bgcolor=COLOR.BLACK,
        hitdice='12d20',
        thaco=3,
        speed=7.5,
        ac=3,
        gold="500d4",
        attacks=(
            AttackInfo('bite', '1d30'),
            AttackInfo('scratch', '2d21'),
            AttackInfo('tail', '3d15'),
            AttackInfo('acid_breath', '2d30', range=15, blowback=100),
            AttackInfo('fire_breath', '2d30', range=15, blowback=100),
            AttackInfo('ice_breath', '2d30', range=15, blowback=100),
            AttackInfo('lightning_breath', '2d30', speed=0.2, range=15, blowback=100),
        ),
    ),
    PType(
        name='balrog',
        char='B',
        type='monster',
        fgcolor=COLOR.RED,
        bgcolor=COLOR.BLACK,
        hitdice='10d30',
        thaco=2,
        speed=3.0,
        ac=2,
        gold='500d2',
        attacks=(
            AttackInfo('burn', '1d30'),
            AttackInfo('fire_whip', '5d10', range=3, speed=.3, blowback=100),
        ),
    ),
    PType(
        name='dog',
        char='d',
        type='monster',
        hitdice='5d10',
        thaco=19,
        speed=3.3,
        ac=17,
        gold='3d3',
        attacks=(
            AttackInfo('teeth', '1d10'),
            AttackInfo('tail', '3d5'),
            AttackInfo('scratch', '2d7'),
        ),
    ),
    PType(
        name='cat',
        char='d',
        type='monster',
        hitdice='5d9',
        thaco=19,
        speed=3.5,
        ac=17,
        gold='3d3',
        attacks=(
            AttackInfo('teeth', '1d10'),
            AttackInfo('tail', '3d5'),
            AttackInfo('scratch', '2d7'),
        ),
    ),
    PType(
        name='queen mosquito',
        char='M',
        type='monster',
        hitdice='6d10',
        thaco=0,
        speed=4,
        ac=10,
        gold="5d3",
        attacks=(
            AttackInfo('big slurp', '3d3', blowback=-1),
            AttackInfo('summoned_mosquito', '1d2', range=10, speed=10, blowback=-1)
        ),
        stuff=[(weapons.sword(name="mosquito_mouth_stabber", size=Size(1.2, 1.1, 1.0), attack=AttackInfo('blood_slice', '5d5', blowback=-0.5), pos=(10, 3)))],
    ),
    PType(
        name='mosquito',
        char='m',
        type='monster',
        hitdice='1d1',
        thaco=20,
        speed=3,
        ac=2,
        gold="0d1",
        attacks=(
            AttackInfo("lil' slurp", '1d2', blowback=-1),
        ),
    ),
    PType(
        name='chest',
        char='=',
        type='monster',
        hitdice='1d1',
        thaco=0,
        speed=0,
        ac=0,
        gold="100d5",
        attacks=(
        ),
    ),
    PType(
        name='Pat (Mimic)',
        char='=',
        type='monster',
        hitdice='1d1',
        thaco=17,
        speed=4,
        ac=5,
        gold="300d5",
        attacks=(
            AttackInfo("bite", '25d1', blowback=0),
        ),
    ),
    PType(
        name='summoned_mosquito',
        char='m',
        type='monster',
        hitdice='1d1',
        thaco=10,
        speed=3,
        ac=2,
        gold="0d1",
        attacks=(
            AttackInfo('little slurp', '1d2', blowback=-1),
        ),
    ),
    PType(
        name='dodger',
        char='d',
        type='monster',
        hitdice='1000d10',
        thaco=0,
        speed=1.0,
        ac=0,
        attacks=(
            AttackInfo('absolute destruction', '10d10000000'),
        ),
    ),

    PType(
        name='human',
        char='h',
        type='monster',
        hitdice='10d8',
        thaco=19,
        speed=2,
        ac=10,
        brightness=5,
        attacks=(
            AttackInfo('karate-chop', '3d5'),
            AttackInfo('head-butt', '1d9'),
            AttackInfo('arrow', '1d6', range=100, blowback=100, speed=0.25) #Blowback is for projectile
        ),
        body_stats={
            'btype': 'humanoid',
            'height': 160,
            'weight': 90,
            'body2head': 7.5,
        },
    ),
    PType(
        name='wall',
        char='#',
        type='wall',
        fgcolor=COLOR.YELLOW,
        hitdice='20d100',
        regen_fac=0,
        thaco=20,
        speed=0,
        ac=100,
        gold="0d1",
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
        gold="0d1",
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
        speed=10.0,
        ac=-10,
        gold="0d1",
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='righteous_arrow',
        char='-',
        type='projectile',
        fgcolor=COLOR.WHITE,
        bgcolor=COLOR.BLACK,
        hitdice='1d5',
        thaco=20,
        speed=10.0,
        ac=-10,
        gold='0d1',
        brightness=5,
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='air_strike',
        char='§',
        type='projectile',
        fgcolor=COLOR.WHITE,
        bgcolor=COLOR.BLACK,
        hitdice='1d2',
        thaco=20,
        speed=10.0,
        ac=-10,
        gold="0d1",
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
        speed=10.0,
        ac=-10,
        gold="0d1",
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='fire_whip',
        char='-',
        type='projectile',
        fgcolor=COLOR.RED,
        bgcolor=COLOR.BLACK,
        hitdice='2d8',
        thaco=20,
        speed=3.0,
        ac=-10,
        gold="0d1",
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='acid_breath',
        char='*',
        type='projectile',
        fgcolor=COLOR.GREEN,
        bgcolor=COLOR.BLACK,
        hitdice='2d8',
        thaco=20,
        speed=10.0,
        ac=-10,
        gold="0d1",
        attacks=(
        ),
        move_tactic='pos_path',
    ),
    PType(
        name='ice_breath',
        char='*',
        type='projectile',
        fgcolor=COLOR.WHITE,
        bgcolor=COLOR.BLACK,
        hitdice='2d8',
        thaco=20,
        speed=10.0,
        ac=-10,
        gold="0d1",
        attacks=(

        ),
        move_tactic='pos_path',
    ),
    PType(
        name='lightning_breath',
        char='*',
        type='projectile',
        fgcolor=COLOR.YELLOW,
        bgcolor=COLOR.BLACK,
        hitdice='2d8',
        thaco=20,
        speed=10.0,
        ac=-10,
        gold="0d1",
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
        speed=attack_info.speed,
        range=attack_info.range,
        blowback=attack_info.blowback,
    )

def create_peep(
        ptype,
        pclass="THIEF",
        name='',
        pos=(0, 0),
        height=1.0,
        weight=1.0,
        head2body=7.5,
        exp=0,
        attacks=(), # overrides ptype attacks if set
        shooter=None
    ):
    pt = PTYPES_BY_NAME[ptype]
    pc = get_pclass(pclass)
    hp = roll_dice(pt.hitdice)
    factor = pc.level_factor * GAME_SETTINGS.LEVEL_UP_FACTOR
    level = level_calc(exp, factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL)
    regen_fac = pt.regen_fac
    attacks = attacks if len(attacks) else pt.attacks # todo: combine type and passed in?
    gold = roll_dice(pt.gold)
    brightness = pt.brightness

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
        statscur=pt.stats,
        stats=pt.stats,
        height=pt.height,
        attacks=tuple(create_attack(ai) for ai in attacks),
        pos=pos,
        prev_pos=[],
        pabilities=[],
        aabilities=[],
        states=[],
        body=create_body('humanoid', height, weight, head2body=head2body),
        move_tactic=pt.move_tactic,
        shooter=shooter,
        gold=gold,
        pclass=pc,
        brightness=brightness
    )
    if pt.stuff:
        ret.stuff.extend(pt.stuff)
    n = 0
    while n <= ret.level:
        peep_acquire_abilities(ret, n)
        n += 1
    return ret


def test_out():
    for name in PTYPES_BY_NAME:
        p = create_peep(name)
        print(p)
        # print(yaml.dump(m, sort_keys=False, default_flow_style=False))


if __name__ == '__main__':
    test_out
