from lib.model import Ammo, Attack
from lib.constants import Color





def create_projectile(name, x=0, y=0, hp=0, direct=0):
    ret = None
    if name == 'arrow':
        ret = Ammo(
        name= 'arrow',
        char = '-',
        fgcolor= Color.YELLOW,
        speed= 100,
        tics= 0,
        attacks= {
            'hit': Attack('1d15'),
        }
    )
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.x = x
    ret.y = y
    ret.direct = direct
    return ret