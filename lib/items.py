from dataclasses import dataclass, field

from lib.constants import Color
from lib.model import DataModel

@dataclass
class Ammo(DataModel):
    def __post_init__(self):
        super().__init__()

    name: str = ''
    char: str = '?'
    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK
    thaco: int = 20
    speed: int = 100
    ac: int = 20
    maxhp: int = 1

    # temp state
    tics: int = 0
    pos: tuple = field(default_factory=tuple)
    attacks: dict = field(default_factory=dict)
    move_tactic: str = 'straight'
    direct: int = 0
