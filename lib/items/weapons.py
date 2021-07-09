from dataclasses import dataclass

from lib.attack import AttackInfo
from lib.model import Size
from lib.items.item import Item, FitInfo

AVERAGE_SWORD_SIZE = Size(0.4, .02, .0025)
AVERAGE_SWORD_WEIGHT = 3 / 65

@dataclass
class Sword(Item):
    name: str = 'sword'
    char: str = '/'
    fit_info: FitInfo = FitInfo('held', 'held', 'hand', ('dom',))

# depth is the thickness of the sword.
def sword(size=Size(1.0,1.0,1.0), attack=AttackInfo('hit', '1d1'), **params):
    ret = Sword(**params)
    ret.size = size.copy(*AVERAGE_SWORD_SIZE.as_tuple())
    ret.attack = attack
    vol = ret.size.volume()
    avol = AVERAGE_SWORD_SIZE.volume()
    ret.weight = AVERAGE_SWORD_WEIGHT * (vol/avol)

    return ret
