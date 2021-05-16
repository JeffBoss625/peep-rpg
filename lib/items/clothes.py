from dataclasses import dataclass

from lib.items.item import Item, FitInfo
from lib.model import register_yaml, Size

AVERAGE_CLOAK_SIZE = Size(0.8, 1.05, 1.05)
AVERAGE_CLOAK_THICK = 0.3 / 175
AVERAGE_CLOAK_WEIGHT = 1 / 65

@dataclass
class Cloak(Item):
    name: str = 'cloak'
    char: str = '('
    fit_info: str = FitInfo('cover', 'loose', 'body')
    circ: float = 0.0

def cloak(h=1.0, w=1.0, d=1.0, thick=1.0):
    # average human body dimensions (h,w,d) are 1.0 x 0.25 x 0.125
    ret = Cloak()
    ret.size = AVERAGE_CLOAK_SIZE.copy(h, w, d)
    ret.thick = thick * AVERAGE_CLOAK_THICK
    vol = ret.thick * ret.size.cover_area()
    avol = AVERAGE_CLOAK_THICK * AVERAGE_CLOAK_SIZE.cover_area()
    ret.weight = AVERAGE_CLOAK_WEIGHT * (vol/avol)
    return ret


register_yaml((Cloak,))


