from dataclasses import dataclass, field
from typing import Tuple

from yaml import dump

# from lib.items.belt import SoldiersBelt
# from lib.items.bow import Arrow, Bow
# from lib.items.holster import Quiver
from lib.items.item import Item
from lib.model import Size, register_yaml
from lib.util import DotDict


class RACE:
    HUMAN = 'human'

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
class Body:
    body_type: str = ''
    size: Size = ()
    weight: float = 0
    parts: Tuple[BodyPart] = field(default_factory=tuple)      # BodyParts in order top to bottom

    # hide reproducable state
    def __getstate__(self):
        items_by_slot = {}
        for part in self.parts:
            for slot in part.slots:
                if slot.item:
                    items_by_slot[slot.name] = slot.item

        # state arguments to create_humanoid() that will recreate this body
        return {
            'body_type': self.body_type,
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

    def parts_by_name(self):
        ret = DotDict()
        for p in self.parts:
            ret[p.name] = p
        return ret

# average male height in cm: Dunadain: 180, Human: 175, Dwarf: 135, Hobbit: 105
def update_human_proportions(body, body2head):
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
        'arm':   0.265,         # shoulder-to-wrist
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

def update_dragon_proportions(body, head):
    dratio = DotDict({
        # 'Name': (height, width, depth) in proportion to head
        'head':      (1.00, 1.00, 1.00),
        'neck':      (0.90, 0.90, 1.50),
        'body':      (2.50, 1.25, 5.00),
        'tail_base': (1.20, 1.20, 1.40),
        'tail_mid':  (0.90, 0.90, 1.30),
        'tail_tip':  (0.60, 0.60, 1.20),
        'l_arm':     (3.75, 0.90, 0.90),
        'r_arm':     (3.75, 0.90, 0.90),
        'l_leg':     (3.75, 0.90, 0.90),
        'r_leg':     (3.75, 0.90, 0.90),
    })
    for part in body.parts:
        ratio = dratio[part.name]
        part.size = Size(ratio[0] * head[0], ratio[1] * head[1], ratio[2] * head[2])

def create_body(body_type, height=1.0, weight=1.0, **kwds):
    if body_type == 'humanoid':
        ret = create_humanoid(height, weight, **kwds)
    elif body_type == 'dragon':
        ret = create_dragon(height, weight)
    else:
        raise ValueError(f'body_type {body_type}')

    return ret

def create_humanoid(height, weight, body2head=7.5):
    slot_definitions = (
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
            'waist',            # belt, sash, scabbard, knife-belt, dart-belt, ...
        )),

        # Hands / Arms
        ('l_hand', (
            'l_hand',           # glove, gauntlet, OR rings
            'l_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
        )),
        ('r_hand', (
            'r_hand',           # glove, gauntlet, OR rings
            'r_hand_holding',   # shield, weapon, bag, cup, wand, staff, any item, ...
        )),

        # rings cannot be warn over gauntlets (but perhaps may be held?)
        # rings left
        ('l_finger1', ('l_finger1',)),
        ('l_finger2', ('l_finger2',)),
        ('l_finger3', ('l_finger3',)),
        ('l_finger4', ('l_finger4',)),
        # rings right
        ('r_finger1', ('r_finger1',)),
        ('r_finger2', ('r_finger2',)),
        ('r_finger3', ('r_finger3',)),
        ('r_finger4', ('r_finger4',)),

        ('l_arm', ('l_wrist',)),
        ('r_arm', ('r_wrist',)),

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

    ret = Body('humanoid', Size(height, int(height/4), int(height/10)), weight, tuple(parts))
    update_human_proportions(ret, body2head)
    return ret

def create_dragon(height, weight):
    height *= 2
    weight *= 20

    slot_definitions = (
        # Upper Bodywear
        ('head', ()),
        ('neck', ('neck',)),    # necklass, amulet, neck scarf, ...
        ('body',(
            'on_back',          # for a saddle
        )),
        # Hands / Arms
        ('l_arm', ('l_wrist',)),
        ('r_arm', ('r_wrist',)),

        # rings cannot be warn over gauntlets (but perhaps may be held?)
        # rings right

        ('l_leg', ('l_ankle',)),
        ('r_leg', ('r_ankle',)),
    )
    parts = []
    for name, slotnames in slot_definitions:
        bslots = tuple(BodySlot(slotname) for slotname in slotnames)
        parts.append(BodyPart(name, slots=bslots))

    ret = Body('dragon', Size(height, int(height/4), int(height/10)), weight, tuple(parts))
    update_dragon_proportions(ret, (90, 70, 180))
    return ret


register_yaml((BodySlot, BodyPart, Body))

if __name__ == '__main__':
    # body = create_dragon(height=203, weight=120)
    body = create_body('humanoid')
    print(dump(body.parts, sort_keys=False))
    # bslots = body.body_slots()
    # bslots.torso.on_shoulder1.item = Bow()
    # bslots.torso.on_waist = SoldiersBelt()
    # quiver = Quiver()
    # slot = quiver.slots[0]
    # slot.items = ((Arrow(), 20),)
    # bslots.torso.on_shoulder2.item = quiver
    # state = body.__getstate__()
    # # print(state)
    # del state['items']
    # body2 = create_humanoid(**state)
    # # print(dump(body2))
    # # print(dump(body))
    # print(dump(list(body.parts_by_name().values())))


