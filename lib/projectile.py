from lib.model import Ammo, Attack
from lib.constants import Color

PROJECTILES = [
    Ammo(
        name= 'arrow',
        char = '-',
        fgcolor= Color.YELLOW,
        speed= 100,
        tics= 0,
        attacks= {
            'hit': Attack('1d15'),
        }
    ),
]

PROJECTILES_BY_NAME = {p.name:p for p in PROJECTILES}

def ammo_by_name(name, x=0, y=0, hp=0, direct=0):
    ret = PROJECTILES_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.x = x
    ret.y = y
    ret.direct = direct
    return ret