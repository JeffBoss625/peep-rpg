from dataclasses import dataclass

from lib.items.item import Item, ITEM_SLOT, Shooter, BODY_SLOT
from lib.model import register_yaml

# A Shooter transfers velocity
@dataclass
class Bow(Shooter, Item):
    shot_slot_type: str = ITEM_SLOT.ARROW
    shot_speed: int = 100  # speed -= distance * (deceleration/10,000)
    shot_thaco: int = 20  # could replace this with distance tables. should be affected by armor type.
    shot_deceleration: int = 100  # 1% speed loss per square
    slot_type: str = BODY_SLOT.ON_SHOULDER


@dataclass
class Arrow(Item):
    name = 'arrow'
    char = '-'
    material = 'wood'
    size = (90, 2, 2)  # cm (about 3 ft)
    weight = 100  # grams
    slot_type = ITEM_SLOT.ARROW


register_yaml((Bow,))


