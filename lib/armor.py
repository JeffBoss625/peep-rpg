from lib.items import *
import yaml

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

@dataclass
class Iron:
    material = 'iron'
    fgcolor = COLOR.BLUE
    slot_type = 'head'
    prot: Protection = field(default_factory=Protection)

@dataclass
class Cap:
    char = '^'
    slot_type = BODY_SLOT.HEAD

class IronCap(Item, Cap, Iron, Protection):
    pass


# register_yaml([IronCap, Iron, Cap, Protection])

METAL_HELMS = (
    ('iron', 'cap')
)

if __name__ == '__main__':
    mc = IronCap('iron-cap', size=())
    print(yaml.dump(mc, sort_keys=False))