from dataclasses import dataclass, field

from lib.constants import Color
from lib.model import DataModel

@dataclass
class Item(DataModel):
    def __post_init__(self):
        super().__init__()
    name: str = ''
    char: str = '?'
    weight: int = 1
    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK


@dataclass
class Ammo(Item):
    speed: int = 100
    ac: int = 20
    maxhp: int = 1
    thaco: int = 20

    # temp state
    tics: int = 0
    pos: tuple = field(default_factory=tuple)
    attacks: dict = field(default_factory=dict)
    move_tactic: str = 'straight'
    direct: int = 0


if __name__ == '__main__':
    a = Ammo('dart', '/', Color.GREEN)
    print(a)