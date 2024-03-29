from dataclasses import dataclass, field
from typing import Tuple, Any, List

import yaml

from lib.constants import COLOR
from lib.model import Size, register_yaml


# item slots on the body (armor, rings, held weapons...)
class BODY_SLOT:
    HEAD = 'head'
    NECK = 'neck'
    TORSO_UNDER = 'torso_under'
    TORSO_OVER = 'torso_over'
    GARMENT_OUTER = 'garment_outer'
    ON_BACK = 'on_back'
    ON_SHOULDER = 'on_shoulder'
    WAIST = 'waist'
    # todo: consider upper-arm lower-arm arm-holster...
    L_HAND = 'l_hand'
    L_HAND_HOLDING = 'l_hand_holding'
    R_HAND = 'r_hand'
    R_HAND_HOLDING = 'r_hand_holding'
    L_ARM = 'l_arm'
    R_ARM = 'r_arm'
    L_FINGER1 = 'r_finger1'
    L_FINGER2 = 'r_finger2'
    L_FINGER3 = 'r_finger3'
    L_FINGER4 = 'r_finger4'
    R_FINGER1 = 'r_finger1'
    R_FINGER2 = 'r_finger2'
    R_FINGER3 = 'r_finger3'
    R_FINGER4 = 'r_finger4'
    # todo: consider top and bottom legs (shin guards...)
    LEGS_INNER = 'legs_inner'
    LEGS_OUTER = 'legs_outer'
    FOOT_INNER = 'foot_inner'
    FOOT_OUTER = 'foot_outer'


# item slots within other items (scabbards, knife-belts, quivers, bags, sacks...)
class ITEM_SLOT:
    DART = 'dart'
    KNIFE = 'knife'
    SWORD = 'sword'
    ARROW = 'arrow'
    BOW = 'bow'  # e.g. bow or crossbow shoulder-sling or belt-sling
    BOLT = 'bolt'
    PELLET = 'pellet'
    AXE = 'axe'  # handled tool such as axe, pickaxe, or hammer
    WAND = 'wand'
    VIAL = 'vial'  # small potions, liquids
    CANTEEN = 'canteen'  # large liquid container, wineskin, ... (multi-dose)
    BAG = 'bag'  # bag, sack, ...
    BOX = 'box'  # box, chest, ...


@dataclass
class FitInfo:
    slot_name: str = ''     # cover (shirt, cloak, boots), around (finger, waist), strap (shoulder/back)
    fit: str = ''           # fit detail for cover or around: fitted, loose, fitted-clasp...
    body_part: str = ''     # if for a specific body part, name the part here (hand, foot, waist...)
    fit_pref: Tuple[str] = field(default_factory=tuple)  # other fit detail: dom(inant)/subdom(inant) for weapons/shields

@dataclass
class Layer:
    elasticity: float = 1.0
    thickness: float = 1.0
    area: float = 1.0
    breaking_pt: float = 1.0
    plastic_region: float = 1.0
    toughness: float = 1.0  # holds together and friction like felt
    hardness: float = 1.0
    durability: float = 1.0


@dataclass
class Properties:
    layers: List[Layer] = field(default_factory=list)
    pierce_area: float = 1.0
    mass: float = 1.0
    slash_sharpness: float = 1.0


@dataclass
class Item:
    name: str = 'thing'
    char: str = '?'
    size: Size = field(default_factory=Size)  # height, width, depth in mm ** when placed in storage or slot **
    fit_info: FitInfo = None    # information on wearing on the body
    weight: float = 1.0
    pos: Tuple[int,int] = field(default_factory=tuple)
    amount: int = 1
    properties: Properties = None

    fgcolor: str = COLOR.WHITE
    bgcolor: str = COLOR.BLACK


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
    # BELT: 'BELT'                    # on waist: throwing knives, sword, darts, pick-axe, throwing axes, bag of sling shot, ...
    # WEAPON_SLOT: 'WEAPON_SLOT'      # wielding: sword that fires small blades, double-crossbow with 2 loaded rounds
    # POCKET: 'POCKET'                # pants and jackets may have pockets that can hold rings, shot, etc.
    #
    # # STORAGE
    # BACKPACK: 'BACKPACK'            # on back: holds small/medium items
    # BAG: 'BAG'                      # hold in hand, holds multiple items at ready
    # LARGE_SACK: 'LARGE_SACK'        # hold in 1 hand AND on back (2 slots). holds more stuff


# A weapon that launches items at higher speed than could be simply thrown
@dataclass
class Shooter:
    shot_slot_type: str = ''
    shot_speed: int = 0
    shot_thaco: int = 0
    shot_deceleration: int = 0  # 1/10,000 percent change in speed per square traveled (negative is deceleration)


register_yaml((Shooter, Item))


if __name__ == '__main__':
    pass

    # s = Bow('short bow', '}')
    # sstr = yaml.dump(s)
    # print(s)
    # print(sstr)

