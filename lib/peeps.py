from dataclasses import dataclass, field, replace
from typing import Tuple, List, Any
from lib.body import Body
from lib.constants import COLOR
from lib.constants import GAME_SETTINGS
from lib.model import DataModel, register_yaml, ModelList
import math
from lib.stats import Stats


@dataclass
class Attack(DataModel):
    name: str = ''
    damage: str = '1d1'
    speed: float = 1.0
    range: int = 0
    # blowback is multiplied by damage done and applied to attacker. positive causes damage negative
    # *heals* hit points (life drain)
    blowback: float = 0

    def __post_init__(self):
        super().__init__()

    def projectile_attack(self):
        return replace(self, range=0)

@dataclass
class Inventory:
    hand1: str = ''
    hand2: str = ''
    back: str = ''
    waist: str = ''
    gloves: str = ''
    head: str = ''
    neck: str = ''
    wrist: str = ''
    arm: str = ''
    feet: str = ''
    under_armor: str = ''
    over_armor: str = ''
    legs: str = ''
    shoulders: str = ''

@dataclass
class LevelData():
    pclass: str = ''
    level: int = 0
    expmin: int = 0
    expmax: int = 0
    hp: int = 0   # todo: use human relative scale 0.1..3.0..


@dataclass
class Peep(DataModel):
    def __post_init__(self):
        super().__init__()

    name: str = ''
    type: str = ''
    char: str = '?'
    fgcolor: str = COLOR.WHITE
    bgcolor: str = COLOR.BLACK

    # todo: maintain two structures, the resting/normal state and the current state (hp, speed... enhanced from potions etc)
    # todo: lazy-calculate values such as "speed" and "ac" from equipment, dexterity, etc...
    ldata: Tuple[LevelData] = field(default=())
    maxhp: int = 0
    thaco: int = 20
    speed: float = 1.0
    ac: int = 10
    pclass: str = 'FIGHTER'
    statscur: Stats = field(default_factory=Stats)
    stats: Stats = field(default_factory=Stats)
    height: int = 5
    move_tactic: str = 'hunt'
    _hunt_target: any = None
    direct: int = -1
    pos_path: Tuple[Tuple[int, int]] = field(default_factory=tuple)
    pos_i = 0  #todo: should be called path_i: index for how far along a projectile is along a path
    pabilities: List[Any] = field(default_factory=list)
    aabilities:List[Any] = field(default_factory=list)
    states: List[Any] = field(default_factory=list)
    hp: int = 0
    regen_fac: float = 1.0
    exp: int = 1
    level: int = 1
    level_factor: int = 2
    hitdice: str = '1d1'
    hitdicefac: int = 0
    _tics: int = 0              # private- events don't propogate for this attribute
    _age: int = 0              #total time has passed since peep created.

    pos: Tuple[int,int] = field(default_factory=tuple)
    prev_pos: Tuple[int,int] = field(default_factory=tuple)
    attacks: List[Attack] = field(default_factory=list)
    inventory: Inventory = field(default_factory=Inventory)
    stuff: ModelList = field(default_factory=ModelList)
    gold: int = 10
    shooter: Any = None

    body: Body = None

    _yaml_ignore = {'_tics', 'pos'}

    def equip(self, holder, item):
        pass

    # return the experience point value for killing this monster
    def exp_value(self):
        b = GAME_SETTINGS.BASE_KILL_EXP
        # very basic - todo: use attacks and other info to calculate experience
        return b * math.pow(self.maxhp, 0.5) * self.regen_fac

    def put_item(self, slot, item, game):
        self.stuff.remove(item)
        if hasattr(item, 'attack'):
            self.attacks = list(self.attacks)
            self.attacks.append(item.attack)
        prev = slot.put(item)
        msg = [f'you are wearing a {item.name}']
        if prev:
            msg.append(f'...you put other items back in your bag')
            game.banner(msg)

    def remove_item(self, slot, item, game):
        slot.items.remove(item)
        if item.attack:
            for a in self.attacks:
                if a == item.attack:
                    self.attacks.remove(a)



def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


register_yaml((Peep, Attack))

def make_dad_buff(dad):
    dad.equip()


if __name__ == '__main__':
    pass
    # dad = create_humanoid(RACE.HUMAN, 203, 120, 8)
    # volumes = list((p.name, p.size.volume()) for p in dad.parts)
    # vtot = sum(v[1] for v in volumes)
    # print('vtotal parts', vtot)
    # print('vtotal', bill.size.volume())
    # vnorm = list((p[0], 100000 * p[1]/vtot) for p in volumes)
    # print(dump(vnorm))

    # p = Peep('bill')
    # p.subscribe(printargs)
    # p.name = 'bill'
    # p.name = 'bbb'
    # p.hp = 2
    # p.hp = 2
    # p.pos = (3,4)
    # p.attacks['bite'] = Attack(damage='3d6')
    #
    # print('DUMP:')
    # print(dump(p))

