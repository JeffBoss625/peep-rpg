from dataclasses import dataclass
from typing import Tuple

from lib.items.holster import HolsterSlot, Holster
from lib.items.item import Item, ITEM_SLOT, BODY_SLOT
from lib.model import register_yaml, Size


@dataclass
class Belt:
    char: str = '_'
    material: str = 'leather'
    size: Size = Size(45, 45, 5)
    weight: int = 300
    slot_type: Tuple[BODY_SLOT] = (BODY_SLOT.WAIST,)


@dataclass
class SoldiersBelt(Belt, Holster, Item):
    name: str = 'soldiers-belt'
    slots: Tuple[HolsterSlot] = (HolsterSlot(ITEM_SLOT.SWORD, 1, 42000, Size(80, 10, 2)),)


register_yaml((SoldiersBelt,))


