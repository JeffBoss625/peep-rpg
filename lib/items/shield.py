from dataclasses import dataclass, field

import yaml

from lib.items.item import BODY_SLOT, Item
from lib.items.material import Iron, Protection
from lib.model import register_yaml, Size


@dataclass
class Shield:
    char: str = ')'
    slot_type: str = BODY_SLOT.ON_BACK
    size: Size = ()

def create_shield(layers):
    prot = layers[0].prot


register_yaml([Shield])

METAL_HELMS = (
    ('iron', 'cap')
)

if __name__ == '__main__':
    mc = IronCap('iron-cap')
    print(yaml.dump(mc, sort_keys=False))

