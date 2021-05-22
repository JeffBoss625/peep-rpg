from dataclasses import dataclass, field
from typing import Tuple, ClassVar, AnyStr, List, Dict

from yaml import dump

# from lib.items.belt import SoldiersBelt
# from lib.items.bow import Arrow, Bow
# from lib.items.holster import Quiver
import lib.items.clothes as clothes
from lib.items.item import Item
from lib.model import Size, register_yaml
from lib.util import DotDict


class RACE:
    HUMAN = 'human'

# a logical "place" ody on the bthat can hold, wear, or bear one or more items.
@dataclass
class BodySlot:
    # nature of wearing items relative to part  - 'cover', 'around', 'front', 'held', 'back', 'strap'
    name: str = ''

    # limit to number of items
    #   cover: number of layers for this part (e.g. shirt & mail)
    #   carry: number carried (e.g. hung on shoulder)
    #   around: number worn (e.g. rings on a finger)
    max_count: int = 1

    # type of fit to go with name
    #   cover: loose or fitted
    #   carry: strapped, hung, held
    #   around: loose, fitted, or fitted-clasp
    #   held: *typically* held in hand (shield or weapon)
    fit: Tuple[str] = field(default_factory=tuple)

    # weight_cap: int = 0
    # size_min: Size = None
    # size_max: Size = None
    items: List[Item] = field(default_factory=list)  # items in order. e.g. cover: under (shirt) then over (jacket).


@dataclass
class BodyPart:
    name: ''                        # head, hand, waist...
    size: Size = ()
    labels: Tuple = field(default_factory=tuple)
    weight: float = 0
    weight_cap: float = 0                       # weight capacity this part can carry
    slots: List = field(default_factory=list)   # number, volume and types of items this part can wear or carry

@dataclass
class Body:
    body_type: str = ''  # name of body type - humanoid, dragon...
    size: Size = ()
    weight: float = 1.0 # 1.0 = average human male weight (65 KG)
    parts: Dict[str,Tuple[BodyPart]] = field(default_factory=dict)      # BodyParts by name: head, torso, finger...

    # hide reproducable state
    def __getstate__(self):
        items = []
        for index, part, slot, item in self.item_tuples():
            items.append((slot.name, item))

        # state arguments to create_humanoid() that will recreate this body
        return {
            'body_type': self.body_type,
            'height': self.size.h,
            'weight': self.weight,
            'items': items,
        }

    def _parts(self, part_name, labels=()):
        ret = []
        for p in self.parts[part_name]:
            if labels and intersect(labels, p.labels) != list(labels):
                continue
            ret.append(p)
        return ret

    def protection(self, part_name, labels=()):
        ret = []
        for p in self._parts(part_name, labels):
            for s in p.slots:
                for i in s.items:
                    ret.append(i)
        return ret

    def wear(self, item):
        finfo = item.fit_info
        if not finfo:
            return False

        parts = self.parts.get(finfo.body_part, ())
        if not parts:
            return False

        for p in parts:
            for slot in p.slots:
                if slot.name == finfo.slot_name and finfo.fit in slot.fit:
                    if slot.max_count > len(slot.items):
                        slot.items.append(item)
                        return True

        return False

    # return items in context-tuples:
    # (
    #   index,          fixed index of slot container (Body or BodyPart)
    #   body/part,      that which holds the slot,
    #   slot,           the slot
    #   item,           item in that slot
    # )
    def item_tuples(self):
        ret = []
        index = 0

        for parts in self.parts.values():
            for part in parts:
                for slot in part.slots:
                    for item in slot.items:
                        ret.append((index, part, slot, item))
                    index += 1

        return ret

def intersect(a, b):
    ret = []
    for i in a:
        if i in b:
            ret.append(i)
    return ret
    #
    # for part in body.parts:
    #     pn = part.name
    #     if pn[0:2] in ['l_', 'r_']:
    #         pn = pn[2:]
    #     h = body.size.h * hratio[pn]
    #     wdrat = wdratio[pn]
    #     part.size = Size(int(h), int(h*wdrat[0]), int(h*wdrat[1]))

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

    # body proportions in a straight standing position
    # average male height in cm: Dunadain: 180, Human: 175, Dwarf: 135, Hobbit: 105
    part_sizes = (
        # height in proportion to overall height, (width, depth) in proportion to height
        ('body', 1.000, (0.240, 0.08)),       # overall body proportions with 0.240 biacromial (between shoulderblades)

        # standing proportions
        ('head',  0.133, (0.6, 0.8)),         # for 7.5 body-to-head ratio
        ('neck',  0.025, (3.0, 3.0)),         # contribution to overall height. actual neck length is about 50% more
        ('torso', 0.305, (0.787, 0.190)),     # torso/back
        ('waist', 0.030, (9.0, 5.0)),
        ('legs',  0.470, (0.26, 0.26)),       # waist-to-ankle
        ('foot',  0.037, (1.0, 2.0)),         # ankle-to-heal
        # heights add up to 1

        # armspan components (in proportion to height)
        ('arm',   0.265, (0.125, 0.125)),     # shoulder-to-wrist
        ('wrist', 0.020, (2.5, 1.0)),         # wrist
        ('hand',  0.115, (0.8, 0.1)),         # wrist-to-fingertips

        ('back', 0.305, (0.787, 0.0)),        # 2-dimensional back of torso (hxw)
    )

    finger_sizes = (
        ('index',  .043, (0.2, 0.2)),
        ('middle', .047, (0.2, 0.2)),
        ('ring',   .043, (0.2, 0.2)),
        ('pinky',  .036, (0.2, 0.2)),
    )

    # store parts by name with labels to define side (left/right) and detail (index finger)
    symmetrical = {'foot', 'arm', 'wrist', 'hand'}
    parts_by_name = {}
    for name, h, (w_fac, d_fac), in part_sizes:
        size = Size(h, h*w_fac, h*d_fac)
        if name in symmetrical:
            parts = (
                BodyPart(name, size, ('left',)),
                BodyPart(name, size, ('right',)),
            )
        else:
            parts = (BodyPart(name, size),)

        parts_by_name[name] = parts

    fingers = []
    for side in ('left', 'right'):
        for name, h, (w_fac, d_fac), in finger_sizes:
            size = Size(h, h*w_fac, h*d_fac)
            fingers.append(BodyPart('finger', size, (side, name)))
    parts_by_name['finger'] = tuple(fingers)

    # worn items are 'cover' slots that support 1-2 layers
    wear_info = (
        ('body',  'cover', ('loose',), 1),      # 1: cloak, cape, ...
        ('head',  'cover', ('fitted',), 2),     # 1: hood, padded cap, ... 2: helmet, crown, hat, ...
        ('torso', 'cover', ('fitted',), 2),     # 1: jerkin, chainmail;  2: plate, cuirass, chest plate...
        ('arm',   'cover', ('fitted',), 1),     # 1: bracers
        ('hand',  'cover', ('fitted',), 1 ),    # 1 glove, gauntlet, OR rings
        ('legs',  'cover', ('fitted',), 2),     # 1: breeches, pants, leather-leggings, cargo-pants, ...
                                    # 2: leg guards, samurai armor, poleyn, chausses (chain), plate,
        ('foot', 'cover', ('fitted',), 2),      # 1: wool-socks, .. 2: boots, sandles, shoes, slippers, ...
    )

    carry = (
        ('back', 'strap', ('strap',), 2),        # strap over shoulder: backpack, shield, quiver, sack...
        ('hand', 'held', ('held',), 1),          # shield, weapon, bag, wand, staff, any item, ...
    )

    accessorize = (
        # loose necklass, amulet, neck scarf, ...
        # tight collar/protector or necklass with clasp
        ('neck', 'around', ('loose', 'fitted-clasp'), 1),
        # clapsed or tied tight: belt, sash, scabbard, knife-belt, dart-belt, ...
        ('waist', 'around', ('fitted-clasp',), 1),
        # loose bracelets that slip over the hand and tight bracelets with clasps
        ('wrist', 'around', ('loose', 'fitted-clasp'), 1),
        # fitted rings ('index', 'middle', 'ring', 'pinky')
        ('finger', 'around', ('fitted',), 1),
    )

    for slot_defs in (wear_info, carry, accessorize):
        for part_name, wear_type, fit, max_count in slot_defs:
            for part in parts_by_name[part_name]:
                part.slots.append(BodySlot(wear_type, max_count, fit))

    return Body('humanoid', Size(height, height/4, height/8), weight, parts_by_name)

def create_dragon(height, weight):
    height *= 2
    weight *= 20

    slot_definitions = (
        # Upper Bodywear
        ('head', (
            'cover',    # dragon helm (like horse helm)
            'on',       # crown - only over supple materials like cloth/flexible leather
        )),
        ('neck', ('around',)),      # huge necklass, collar, belt as collar...
        ('body',(
            'cover',                # dragon armor - cover all except bottom/under-side
            'under',                # under-armor/plate/shield
            'on',                   # saddle, pack
        )),
        # Hands / Arms
        ('l_arm', ('around',)),     # huge bracelet, band, belt as band
        ('r_arm', ('around',)),

        ('l_leg', ('around',)),     # huge bracelet, band, belt as band
        ('r_leg', ('around',)),
    )
    parts = []
    for name, slotnames in slot_definitions:
        bslots = list(BodySlot(slotname) for slotname in slotnames)
        parts.append(BodyPart(name, slots=bslots))

    ret = Body('dragon', Size(height, int(height/4), int(height/10)), weight, list(parts))
    update_dragon_proportions(ret, (90, 70, 180))
    return ret


register_yaml((BodySlot, BodyPart, Body))

def test():
    # body = create_dragon(height=203, weight=120)
    body = create_body('humanoid')
    c = clothes.cloak(1.1, 1.2, 1.2, 1.1)
    body.wear(c)
    # print(dump(body.parts, sort_keys=False))
    for index, part, slot, item in body.item_tuples():
        print(f'{index} {part.name} {slot.name} {item.name}')

if __name__ == '__main__':
    test()
