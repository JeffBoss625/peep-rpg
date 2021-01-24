from dataclasses import dataclass, field
from typing import Tuple

import yaml

from lib.items.item import BODY_SLOT, Item
from lib.model import register_yaml, Size


@dataclass
class Shield(Item):
    char: str = ')'
    slot_type: str = BODY_SLOT.ON_BACK
    layers: Tuple = field(default_factory=tuple)

    def __post_init__(self):
        self.size = Size(self.size.h, self.size.w, sum(layer.thick_mm for layer in self.layers))

def create_shield(layers):
    prot = layers[0].prot


register_yaml([Shield])


if __name__ == '__main__':
    s = Shield(layers=(Layer('iron', 'plate', 2), Layer('oak', 'plate', 10)))
    print(yaml.dump(s, sort_keys=False))

