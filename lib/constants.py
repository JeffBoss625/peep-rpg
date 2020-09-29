# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
from dataclasses import dataclass

from lib.util import DotDict

COLOR = DotDict(
    BLACK='BLACK',
    BLUE='BLUE',
    CYAN='CYAN',
    GREEN='GREEN',
    MAGENTA='MAGENTA',
    RED='RED',
    WHITE='WHITE',
    YELLOW='YELLOW',
)


def curses_color(color):
    return 'COLOR_' + color


SIDE = DotDict(
    TOP='TOP',
    LEFT='LEFT',
    BOTTOM='BOTTOM',
    RIGHT='RIGHT',
    CENTER='CENTER',
)


# BODY SLOTS for wearing items
class Slot:
    # Upper Bodywear
    HEAD: 'HEAD'  # helmet, crown, hood, hat, ...
    NECK: 'NECK'  # necklass, amulet, neck scarf, ...
    TORSO_UNDER: 'TORSO_UNDER'  # chain mail, jerkin, ...
    TORSO_OVER: 'TORSO_OVER'  # plate, cuirass
    GARMENT_OUTER: 'GARMENT_OUTER'  # cloak, jacket, ...

    # Hands / Arms
    HAND_WEAR_RIGHT: 'HAND_WEAR_RIGHT'  # glove, gauntlet, OR rings
    HAND_WEAR_LEFT: 'HAND_WEAR_LEFT'  # glove, gauntlet, OR rings

    # rings left                    # rings cannot be warn over gauntlets, but some rings can be used
    L_FINGER1: 'L_FINGER1'
    L_FINGER2: 'L_FINGER2'
    L_FINGER3: 'L_FINGER3'
    L_FINGER4: 'L_FINGER4'
    # rings right
    R_FINGER1: 'R_FINGER1'
    R_FINGER2: 'R_FINGER2'
    R_FINGER3: 'R_FINGER3'
    R_FINGER4: 'R_FINGER4'

    # WIELDING/HOLDING
    HOLD_LEFT: 'HOLD_LEFT'  # right shield, weapon, bag, cup, wand, staff, any item, ...
    HOLD_RIGHT: 'HOLD_RIGHT'  # left shield, weapon, bag, cup, wand, staff, any item, ...

    WAIST_UPPER: 'WAIST_UPPER'  # belt, sash, scabbard, knife-belt, dart-belt, ...
    WAIST_LOWER: 'WAIST_LOWER'  # belt, sash, scabbard, knife-belt, dart-belt, ...

    LEGS_INNER: 'LEGS_INNER'  # breeches, pants, leather-leggings, cargo-pants (pockets!), ...
    LEGS_OUTER: 'LEGS_OUTER'  # leg guards, samurai armor, poleyn, chausses (chain), full plate, ...
    FOOT_INNER: 'FOOT_INNER'  # socks-of-cold-protection, ...
    FOOT_OUTER: 'FOOT_OUTER'  # boots, sandles, shoes, slippers, ...

    # ON SHOULDER/BACK
    ON_BACK: 'ON_BACK'  # backpack, quiver, sack, quiver-sling (ammo and bow)


class Key:
    CTRL_Q = '\x11'


if __name__ == '__main__':
    print(COLOR.values())
