from dataclasses import dataclass

from lib.items.item import Item, FitInfo
from lib.model import register_yaml, Size


@dataclass
class Cloak(Item):
    name: str = 'cloak'
    char: str = '('
    fit_info: str = FitInfo('cover', 'loose', 'body')
    circ: float = 0.0

def cloak(height_fac, circ_fac):
    # average human body dimensions (h,w,d) are 1.0 x 0.25 x 0.125
    ret = Cloak()
    ret.size = Size(height_fac, 0.25 * circ_fac, 0.125 * circ_fac)
    ret.circ = ret.size.w * ret.size.d * 2
    ret.weight *= (height_fac * circ_fac)
    return ret


register_yaml((Cloak,))


