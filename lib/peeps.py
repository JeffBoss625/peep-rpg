from dataclasses import dataclass, field, MISSING
from typing import Dict, Tuple

from lib.body import Body, create_humanoid, RACE
from lib.constants import COLOR
from lib.model import DataModel, ModelDict, register_yaml, PubSub, Size

from lib.util import DotDict

@dataclass
class Attack(DataModel):
    def __post_init__(self):
        super().__init__()

    damage: str = '1d1'
    range: int = 0
    blowback: int = 0


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
    maxhp: int = 0
    thaco: int = 20
    speed: int = 10
    ac: int = 10
    move_tactic: str = 'seek'

    hp: int = 0
    tics: int = 0
    pos: tuple = field(default=(0,0))
    attacks: Dict[str, PubSub] = field(default_factory=ModelDict)

    body: Body = None

    _yaml_ignore = {'tics', 'pos'}

    def equip(self, holder, item):
        pass

def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


register_yaml((Peep, Attack))

def make_dad_buff(dad):
    dad.equip()


if __name__ == '__main__':
    dad = create_humanoid(RACE.HUMAN, 203, 120, 8)
    volumes = list((p.name, p.size.volume()) for p in dad.parts)
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

