# A specialized slot that holds a single item
from dataclasses import dataclass, field
from typing import Tuple

from lib.items.item import Item, BODY_SLOT, ITEM_SLOT
from lib.model import Size


@dataclass
class HolsterSlot:
    holds_slot_type: str = ''
    item_cap: int = 1  # max number of items
    weight_cap: int = 0
    size_cap: Size = field(default_factory=Size)  # volume holding capacity width, length, height in inches
    items: Tuple[Item, int] = field(default_factory=tuple)

    # todo: trigger weight/size check when items are changes

# Containers that hold specific subset of item types such as darts, arrows, knives, a sword, axes...
@dataclass
class Holster:
    slots: Tuple[HolsterSlot] = field(default_factory=tuple)  # item slots supported

@dataclass
class Quiver(Item, Holster):
    name: str = 'quiver'
    char: str = ']'
    material: str = 'leather'
    size: Size = Size(80, 10, 10)
    weight: int = 900
    slot_type: str = (BODY_SLOT.ON_SHOULDER,)
    slots: Tuple[HolsterSlot] = (HolsterSlot(ITEM_SLOT.ARROW, 20, 6000, Size(90, 10, 10)),)