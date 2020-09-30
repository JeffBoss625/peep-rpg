from dataclasses import dataclass, field, MISSING
from typing import Dict, Tuple, List

from lib.constants import COLOR
from lib.items import Ammo, Item
from lib.model import DataModel, ModelDict, register_yaml, PubSub, Size

from lib.util import DotDict


@dataclass
class BodySlot:
    name: str = ''
    weight_cap: int = 0
    size_cap: Size = None
    item: Item = None

@dataclass
class BodyPart:
    name: str = ''
    size: Size = None
    weight: int = 0
    weight_cap: int = 0         # capacity to carry
    slots: List[BodySlot] = None

@dataclass
class Body(DataModel):
    name: str = ''
    size: Size = None
    weight: int = 0
    parts: Tuple[BodyPart] = None      # BodyParts in order top to bottom

def create_part(name, total_height, hratio, wdratio):
    h = total_height * hratio
    size = Size(int(h), int(h * wdratio[0]), int(h * wdratio[1]))
    return BodyPart(name, size)

# average height in cm: Elf: 180, Human: 175, Dwarf: 135, Hobbit: 105
def create_humanoid(name, height, weight, body_to_head):
    # humanoid size ratios
    # body-to-head: normal Human 7.5, Dunadain and Elves are 8, Dwarves are 6.
    hrat = DotDict({
        # heights (in proportion to overall height)
        'head':  0.133,
        'neck':  0.025,         # contribution to overall height. actual neck length is about 50% more
        'torso': 0.305,         # torso/back
        'waist': 0.030,
        'legs':  0.470,         # waist-to-ankle
        'feet':  0.037,         # ankle-to-heal
        # above adds up to 1

        # armspan components (in proportion to height)
        # 'biacromial': 0.240,    # width between shoulder-blades
        'arm':   0.265,         # wrist-to-shoulder
        'hand':  0.115,         # wrist-to-fingertips
        # above adds up to 1 (same as height)

        'finger1': .043,
        'finger2': .047,
        'finger3': .043,
        'finger4': .036,
    })
    # width-depth ratios (relative to height of that part)
    wdrat = DotDict({
        'head':     (0.8, 0.8),
        'neck':     (3.0, 3.0),
        'torso':    (0.787, 0.180),
        'waist':    (9.0, 5.0),
        'legs':     (0.3, 0.3),
        'feet':     (1.0, 2.0),

        'arm':      (0.125, 0.125),
        'hand':     (0.8, 0.1),
        'finger1':  (0.2, 0.2),
        'finger2':  (0.2, 0.2),
        'finger3':  (0.2, 0.2),
        'finger4':  (0.2, 0.2),
    })
    parts = tuple(create_part(name, height, hrat[name], wdrat[name]) for name in hrat.keys())
    return Body('human', Size(height,height/4, height/10), weight, parts)


# BODY SLOTS for wearing items
HumanoidBodySlots = [
    # Upper Bodywear
    ('head', ('head',)),    # helmet, crown, hood, hat, ...
    ('neck', ('neck',)),    # necklass, amulet, neck scarf, ...
    ('torso',(
        'torso_under',      # chain mail, jerkin, ...
        'torso_over'        # plate, cuirass
        'garment_outer',    # cloak, jacket, ...
        'on_back',          # backpack, quiver-sling (ammo and bow), ...
        'on_shoulder',      # quiver, sack, ...
    )),
    ('waist', (
        'waist_upper',      # belt, sash, scabbard, knife-belt, dart-belt, ...
        'waist_lower',      # belt, sash, scabbard, knife-belt, dart-belt, ...
    )),

    # Hands / Arms
    ('right_hand', (
        'right_hand_cover',     # glove, gauntlet, OR rings
        'right_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
    )),
    ('left_hand', (
        'left_hand_cover',     # glove, gauntlet, OR rings
        'left_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
    )),

    # rings left                    # rings cannot be warn over gauntlets, but some rings can be used
    ('l_finger1', ('l_finger1',)),
    ('l_finger2', ('l_finger2',)),
    ('l_finger3', ('l_finger3',)),
    ('l_finger4', ('l_finger4',)),
    # rings right
    ('r_finger1', ('r_finger1',)),
    ('r_finger2', ('r_finger2',)),
    ('r_finger3', ('r_finger3',)),
    ('r_finger4', ('r_finger4',)),

    ('legs', (
        'legs_inner',  # breeches, pants, leather-leggings, cargo-pants (pockets!), ...
        'legs_outer',  # leg guards, samurai armor, poleyn, chausses (chain), full plate, ...
    )),
    ('feet', (
        'foot_inner',  # socks-of-cold-protection, ...
        'foot_outer',  # boots, sandles, shoes, slippers, ...
    )),
]

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
    fgcolor: str = COLOR.WHITE
    bgcolor: str = COLOR.BLACK

    # todo: maintain two structures, the resting/normal state and the current state (hp, speed... enhanced from potions etc)
    # todo: lazy-calculate values such as "speed" and "ac" from equipment, dexterity, etc...
    maxhp: int = 0
    thaco: int = 20
    speed: int = 10
    ac: int = 10
    move_tactic: str = 'seek'

    hp: int = 0
    tics: int = 0
    pos: tuple = field(default=(0,0))
    attacks: Dict[str, PubSub] = field(default_factory=ModelDict)

    _yaml_ignore = {'tics', 'pos'}


def printargs(model, msg, **args):
    print(model.__class__.__name__, model.name, msg, args)


register_yaml((Peep, Ammo, Attack))

if __name__ == '__main__':

    bill = create_humanoid('bill', 200, 100, 7.5)
    print(bill)
    # p = Peep('bill')
    # p.subscribe(printargs)
    # p.name = 'bill'
    # p.name = 'bbb'
    # p.hp = 2
    # p.hp = 2
    # p.pos = (3,4)
    # p.attacks['bite'] = Attack(damage='3d6')
    #
    # print('DUMP:')
    # print(dump(p))

