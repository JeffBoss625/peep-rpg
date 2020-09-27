from lib.items import Ammo
from lib.peeps import Attack
from lib.constants import Color


def create_projectile(name, pos=(0,0), hp=0, direct=0):
    ret = None
    if name == 'arrow':
        ret = Ammo(
            name='arrow',
            char='-',
            fgcolor=Color.YELLOW,
            thaco=20,
            speed=200,
            ac=2,
            tics=0,
            attacks={
                'hit': Attack(damage='1d15', blowback=100),
            }
        )
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.pos = pos
    ret.direct = direct
    return ret
