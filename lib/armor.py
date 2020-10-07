from dataclasses import dataclass
from lib.items import *
import yaml

from lib.model import register_yaml


@dataclass
class Protection:
    pierce: int = 0
    slash: int = 0
    crush: int = 0
    heat: int = 0
    cold: int = 0
    acid: int = 0
    elec: int = 0
    fall: int = 0

class PROTECTION:
    IRON = Protection(50,70,50,5,5,20,5,10)

@dataclass
class Iron:
    material = 'iron'
    fgcolor = COLOR.BLUE
    prot: Protection = field(default=PROTECTION.IRON)

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

