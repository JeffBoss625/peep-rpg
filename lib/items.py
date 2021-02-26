from dataclasses import field, dataclass
from typing import Tuple, List

from lib.peep_types import AttackInfo

@dataclass
class DamageInfo:
    name: str = ''
    damage: str = '1d1'
    reach: int = 1.5
    blowback: int = 0

@dataclass
class Item:
    name: str = ''
    height: int = 5
    width: int = 5
    weight: int = 10
    space: int = 0
    melee_damage: Tuple[DamageInfo, ...] = field(default_factory=tuple)
    holding: List[..., ...] = field(default_factory=list)
    item_slot: List[str, str] = field(default_factory=list)
    type: Tuple[..., ...] = field(default_factory=tuple)

ITEMS = [
    Item(
        name='Cool Shield',
        item_slot=[
            'hand1',
            'hand2',
        ],
        type=('shield', 'rect'),
        height=3,
        width=3,
        space=0,
        melee_damage=(
            DamageInfo('bash', '1d3'),
        ),
    ),
    Item(
        name='Cool Sword',
        item_slot=['hand1', 'hand2'],
        type=('sword', 'long'),
        height=5,
        width=1,
        space=0,
        melee_damage=(
            DamageInfo('slice', '1d7'),
        ),
    ),
]

def create_item(name='', pos=(0, 0), item_stats=None):
    pass