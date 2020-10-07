from dataclasses import dataclass, field
from typing import Tuple

from yaml import dump

from lib.items import Item, Quiver, Bow, Arrow
from lib.model import Size, register_yaml, DataModel
from lib.util import DotDict

RACE = DotDict(
    HUMAN='human'
)

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
    slots: Tuple[BodySlot] = field(default_factory=list)

@dataclass
class Body(DataModel):
    def __post_init__(self):
        super().__init__()

    name: str = ''
    size: Size = None
    weight: int = 0
    parts: Tuple[BodyPart] = None      # BodyParts in order top to bottom

    def __getstate__(self):
        items_by_slot = {}
        for part in self.parts:
            for slot in part.slots:
                if slot.item:
                    items_by_slot[slot.name] = slot.item

        return {
            'name': self.name,
            'height': self.size.h,
            'weight': self.weight,
            'items': items_by_slot,
        }

    def body_slots(self):
        ret = DotDict()
        for p in self.parts:
            slots = DotDict()
            for s in p.slots:
                slots[s.name] = s
            ret[p.name] = slots
        return ret

    # todo: use an ordered DotDict to store parts
    def parts_by_name(self):
        ret = DotDict()
        for p in self.parts:
            ret[p.name] = p
        return ret

# average height in cm: Elf: 180, Human: 175, Dwarf: 135, Hobbit: 105
def update_proportions(body, body_to_head):
    # humanoid size ratios
    # body-to-head: normal Human 7.5, Dunadain and Elves are 8, Dwarves are 6.
    hratio = DotDict({
        # heights (in proportion to overall height)
        'head':  0.133,         # for 7.5 body-to-head ratio
        'neck':  0.025,         # contribution to overall height. actual neck length is about 50% more
        'torso': 0.305,         # torso/back
        'waist': 0.030,
        'legs':  0.470,         # waist-to-ankle
        'feet':  0.037,         # ankle-to-heal
        # above adds up to 1

        # armspan components (in proportion to height)
        # 'biacromial': 0.240,  # width between shoulder-blades
        'arm':   0.265,         # wrist-to-shoulder
        'hand':  0.115,         # wrist-to-fingertips
        # above adds up to 1 (same as height)

        'finger1': .043,
        'finger2': .047,
        'finger3': .043,
        'finger4': .036,
    })
    # width-depth ratios (relative to height of that part)
    wdratio = DotDict({
        'head':     (0.6, 0.8),
        'neck':     (3.0, 3.0),
        'torso':    (0.787, 0.190),
        'waist':    (9.0, 5.0),
        'legs':     (0.26, 0.26),
        'feet':     (1.0, 2.0),

        'arm':      (0.125, 0.125),
        'hand':     (0.8, 0.1),
        'finger1':  (0.2, 0.2),
        'finger2':  (0.2, 0.2),
        'finger3':  (0.2, 0.2),
        'finger4':  (0.2, 0.2),
    })
    for part in body.parts:
        pn = part.name
        if pn[0:2] in ['l_', 'r_']:
            pn = pn[2:]
        h = body.size.h * hratio[pn]
        wdrat = wdratio[pn]
        part.size = Size(int(h), int(h*wdrat[0]), int(h*wdrat[1]))


def create_humanoid(body_type, height, weight, body_to_head):
    height *= 10        # save precision
    slot_definitions = (
        # Upper Bodywear
        ('head', ('head',)),    # helmet, crown, hood, hat, ...
        ('neck', ('neck',)),    # necklass, amulet, neck scarf, ...
        ('torso',(
            'torso_under',      # chain mail, jerkin, ...
            'torso_over'        # plate, cuirass
            'garment_outer',    # cloak, jacket, ...
            'on_back',          # backpack, quiver-sling (ammo and bow), ...
            'on_shoulder1',      # quiver, sack, ...
            'on_shoulder2',      # quiver, sack, ...
        )),
        ('waist', (
            'waist_upper',      # belt, sash, scabbard, knife-belt, dart-belt, ...
            'waist_lower',      # belt, sash, scabbard, knife-belt, dart-belt, ...
        )),

        # Hands / Arms
        ('r_hand', (
            'r_hand',           # glove, gauntlet, OR rings
            'r_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
        )),
        ('l_hand', (
            'l_hand',           # glove, gauntlet, OR rings
            'l_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
        )),

        # rings cannot be warn over gauntlets (but perhaps may be held?)
        # rings right
        ('r_finger1', ('r_finger1',)),
        ('r_finger2', ('r_finger2',)),
        ('r_finger3', ('r_finger3',)),
        ('r_finger4', ('r_finger4',)),
        # rings left
        ('l_finger1', ('l_finger1',)),
        ('l_finger2', ('l_finger2',)),
        ('l_finger3', ('l_finger3',)),
        ('l_finger4', ('l_finger4',)),

        ('legs', (
            'legs_inner',  # breeches, pants, leather-leggings, cargo-pants (pockets!), ...
            'legs_outer',  # leg guards, samurai armor, poleyn, chausses (chain), full plate, ...
        )),
        ('feet', (
            'foot_inner',  # socks-of-cold-protection, ...
            'foot_outer',  # boots, sandles, shoes, slippers, ...
        )),
    )

    parts = []
    for name, slotnames in slot_definitions:
        bslots = tuple(BodySlot(slotname) for slotname in slotnames)
        parts.append(BodyPart(name, slots=bslots))

    ret = Body(body_type, Size(height, int(height/4), int(height/10)), weight, tuple(parts))
    update_proportions(ret, body_to_head)

    return ret


register_yaml((BodySlot, BodyPart, Body, Arrow))

if __name__ == '__main__':
    dad = create_humanoid(RACE.HUMAN, 203, 120, 8)
    bslots = dad.body_slots()
    bslots.torso.on_shoulder1.item = Bow()
    quiver = Quiver()
    slot = quiver.slots[0]
    slot.items = ((Arrow(), 20),)
    bslots.torso.on_shoulder2.item = quiver
    print(dump(dad))
    print(dad.parts_by_name().head.size)


