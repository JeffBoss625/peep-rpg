from lib.model import Peep, Attack
from lib.constants import Color
import yaml

MONSTERS = [
    # GOBLINS
    Peep(
        name='Thark',
        type='goblin',
        char='g',
        fgcolor=Color.GREEN,
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
        fgcolor=Color.YELLOW,
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
        fgcolor=Color.WHITE,
        bgcolor=Color.BLACK,
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

    # Red Dragons
    Peep(
        name='Spark',
        type='red dragon',
        char='D',
        fgcolor= Color.RED,
        bgcolor= Color.BLACK,
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
    ),
    # The Black Dragon
    Peep(
        name='Brog',
        type='black dragon',
        char='D',
        fgcolor=Color.BLUE,
        bgcolor=Color.BLACK,
        maxhp=200,
        thaco=3,
        speed=75,
        ac=3,
        attacks={
            'bite': Attack('1d30'),
            'scratch': Attack('2d21'),
            'tail': Attack('3d15'),
            'acid_breath': Attack('2d30', range=15),
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

def color_rep(dumper, data):
    return dumper.represent_scalar('!color', data.name)


if __name__ == '__main__':
    for m in MONSTERS:
        print(yaml.dump(m, sort_keys=False, default_flow_style=False))
