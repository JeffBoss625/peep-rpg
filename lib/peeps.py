from dataclasses import dataclass
from lib.model import *


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
    pos: tuple = field(default_factory=tuple)
    attacks: dict = field(default_factory=lambda: ModelDict())

    _yaml_ignore = {'tics', 'pos'}


def init_cls():
    for cls in [Peep, Ammo, Attack]:
        register_yaml(cls)


def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


if __name__ == '__main__':
    p = Peep('bill')
    p.subscribe(printargs)
    p.name = 'bill'
    p.name = 'bbb'
    p.hp = 2
    p.hp = 2

    # a = ModelDict()
    # a.subscribe(printargs)
    # a['bite'] = Attack('3d4', 4)
    # del a['bite']
    # print(a)
    # print(yaml.dump(p, sort_keys = False))