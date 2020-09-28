from dataclasses import dataclass, field

from lib.constants import Color
from lib.model import DataModel


@dataclass
class Item(DataModel):
    def __post_init__(self):
        super().__init__()
    name: str = ''
    char: str = '?'
    size: tuple = field(default_factory=tuple)  # width, length, height in inches ** when placed in storage or slot **
    weight: int = 1
    slot_type: str = ''

    fgcolor: str = Color.WHITE
    bgcolor: str = Color.BLACK

# Containers that hold multiple small items up to a given size and weight (bag, sack, box, chest, ...)
# It is possible for magical containers and holsters to have a greater size_cap(acity) than their size, and a lower
# weigth than the sum of items they hold.
@dataclass
class GeneralContainer(Item):
    weight_cap: int = 0
    size_cap: tuple = field(default_factory=tuple)  # volume holding capacity width, length, height in inches


    # # EQUIPMENT SLOTS
    #
    # # AT-READY
    # QUIVER: 'QUIVER'                # on back: bolts, arrows, ...
    # BELT_UPPER: 'BELT_UPPER'        # on waist: throwing knives, sword, darts, pick-axe, throwing axes, bag of sling shot, ...
    # BELT_LOWER: 'BELT_LOWER'        # on waist: throwing knives, sword, darts, pick-axe, throwing axes, bag of sling shot, ...
    # WEAPON_SLOT: 'WEAPON_SLOT'      # wielding: sword that fires small blades, double-crossbow with 2 loaded rounds
    # POCKET: 'POCKET'                # pants and jackets may have pockets that can hold rings, shot, etc.
    #
    # # STORAGE
    # BACKPACK: 'BACKPACK'            # on back: holds small/medium items
    # BAG: 'BAG'                      # hold in hand, holds multiple items at ready
    # LARGE_SACK: 'LARGE_SACK'        # hold in 1 hand AND on back (2 slots). holds more stuff


# slots for items that match them with holsters (scabbards, knife-belts, quivers...)
@dataclass
class HolsterSlotType:
    name: str = ''


HOLSTER_SLOTS = [
    'dart',
    'knife',
    'sword',
    'arrow',
    'bow',          # e.g. bow or crossbow shoulder-sling or belt-sling
    'bolt',
    'pellet',
    'axe',          # handled tool such as axe, pickaxe, or hammer
    'wand',
    'vial',         # small potions, liquids
    'canteen',      # large liquid container, wineskin, ... (multi-dose)
]

# slots for wearing/wielding items
BODY_SLOTS = [
    'head'
]

# A specialized slot that holds a single item
@dataclass
class HolsterSlot:
    holds_slot_type: str = ''
    weight_cap: int = 0
    size_cap: tuple = field(default_factory=tuple)  # volume holding capacity width, length, height in inches

# Containers that hold specific subset of item types such as darts, arrows, knives, a sword, axes...
class Holster(Item):
    slots: tuple = field(default_factory=tuple)     # item slots supported

# A weapon that launches items at higher speed than could be simply thrown
@dataclass
class Shooter(Item):
    shot_slot_type: str = ''
    shot_speed: int = 0
    shot_thaco: int = 0
    shot_deceleration: int = 0       # 1/10,000 percent change in speed per square traveled (negative is deceleration)

# A Shooter transfers velocity
@dataclass
class Bow(Shooter):
    def __post_init__(self):
        self.shot_slot_type = HolsterSlotType.ARROW
        self.shot_speed = 100           # speed -= distance * (deceleration/10,000)
        self.shot_deceleration = 100    # 1% speed loss per square
        self.shot_thaco = 20            # could replace this with distance tables. should be affected by armor type.

@dataclass
class Ammo(Item):
    ac: int = 20
    maxhp: int = 1
    thaco: int = 20
    move_tactic: str = 'straight'
    distance: int = 0   # track distance travelled, 10 per square.

    # temp state
    tics: int = 0
    speed: int = 100
    pos: tuple = field(default_factory=tuple)
    attacks: dict = field(default_factory=dict)
    direct: int = 0
    slot_type: str = ''


if __name__ == '__main__':
    s = Bow('short bow', '}')
    print(s)
    a = Ammo('dart', '/', slot_type=HolsterSlotType.DART)
    print(a)