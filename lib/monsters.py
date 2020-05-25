from lib.peep import Peep, Attack

MONSTERS = [
    # GOBLINS
    Peep(
        name='Thark',
        type='goblin',
        char='g',
        hp=10,
        thaco=18,
        speed=13,
        tics=0,
        ac=19,
        attacks={
            'bite': Attack('1d3'),
            'scratch': Attack('2d2'),
            'punch': Attack('2d1'),
        }
    ),


]

MONSTERS_BY_NAME = {m.name:m for m in MONSTERS}

def monster_by_name(name, x=0, y=0, hp=0):
    ret = MONSTERS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.x = x
    ret.y = y
    return ret


