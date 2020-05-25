from lib.peep import Peep, Attack

MONSTERS = [
    # GOBLINS
    Peep(
        name='Thark',
        type='goblin',
        char='g',
        maxhp=10,
        thaco=18,
        speed=13,
        ac=19,
        attacks={
            'bite': Attack('1d3'),
            'scratch': Attack('2d2'),
            'punch': Attack('2d1'),
        }
    ),
    Peep(
        name='Spark',
        type='dragon',
        char='D',
        maxhp=50,
        thaco=10,
        speed=20,
        ac=10,
        attacks={
            'bite': Attack('1d10'),
            'scratch': Attack('2d7'),
            'tail': Attack('3d5'),
            'fire_breath': Attack('2d10'),
        }
    )


]

MONSTERS_BY_NAME = {m.name:m for m in MONSTERS}

def monster_by_name(name, x=0, y=0, hp=0):
    ret = MONSTERS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.x = x
    ret.y = y
    return ret


