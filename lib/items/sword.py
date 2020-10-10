from dataclasses import dataclass
from typing import Tuple

from lib.items.item import BODY_SLOT
from lib.model import Size


@dataclass
class Belt:
    char: str = '_'
    material: str = 'leather'
    size: Size = Size(45, 45, 5)
    weight: int = 300

