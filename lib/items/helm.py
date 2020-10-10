from dataclasses import dataclass, field

from lib.constants import COLOR
from lib.items import *
import yaml

from lib.items.item import BODY_SLOT, Item
from lib.items.material import Iron, Protection
from lib.model import register_yaml, Size


@dataclass
class Cap:
    char: str = '^'
    slot_type: str = BODY_SLOT.HEAD
    size: Size = ()

class IronCap(Iron, Cap, Item):
    name: str = 'iron-cap'


register_yaml([IronCap, Iron, Cap, Protection])

METAL_HELMS = (
    ('iron', 'cap')
)

if __name__ == '__main__':
    mc = IronCap('iron-cap')
    print(yaml.dump(mc, sort_keys=False))

