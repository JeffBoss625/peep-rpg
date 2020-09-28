from dataclasses import dataclass, field, MISSING
from typing import Dict, Tuple, List

from lib.constants import Color
from lib.items import Ammo
from lib.model import DataModel, ModelDict, register_yaml, PubSub, Size
from yaml import dump

@dataclass
class BodySlot:
    name: str = ''

@dataclass
class BodyPart:
    name: str = ''
    size: Size = field(default=Size())
    weight: int = 0
    slot: BodySlot = field(default=BodySlot())


class Body(DataModel):
    parts: Tuple[BodyPart] = field(default=())      # BodyParts in order top to bottom
    weight: int = 0
    size: Size = field(default=Size())

    def __post_init__(self):
        self.weight = sum(p.weight for p in self.parts)

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
    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK

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

    _yaml_ignore = {'tics', 'pos'}


def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


register_yaml((Peep, Ammo, Attack))

if __name__ == '__main__':
    p = Peep('bill')
    p.subscribe(printargs)
    p.name = 'bill'
    p.name = 'bbb'
    p.hp = 2
    p.hp = 2
    p.pos = (3,4)
    p.attacks['bite'] = Attack(damage='3d6')

    print('DUMP:')
    print(dump(p))

    # a = ModelDict()
    # a.subscribe(printargs)
    # a['bite'] = Attack('3d4', 4)
    # del a['bite']
    # print(a)
    # print(yaml.dump(p, sort_keys = False))