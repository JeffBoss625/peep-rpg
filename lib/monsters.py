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

    # Animals
    Peep(
        name='Giant Rat',
        type='rat',
        char='g',
        maxhp=5,
        thaco=19,
        speed=13,
        ac=10,
        attacks={
            'bite': Attack('1d3'),
            'scratch': Attack('1d3'),
            'tail': Attack('2d1'),
        }
    ),

    Peep(
        name='Big Bird',
        type='bird',
        char='g',
        maxhp=15,
        thaco=17,
        speed=19,
        ac=8,
        attacks={
            'beak': Attack('1d10'),
            'talons': Attack('2d7'),
            'wing_blow': Attack('6d1'),
        }
    ),

    # Dragons
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
            'fire_breath': Attack('2d10', range=5),
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


