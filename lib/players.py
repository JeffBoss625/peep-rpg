from lib.peep import Peep, Attack

_PEEPS = [
    Peep(
        name='Bo Bo the Destroyer',
        type='player',
        char='@',
        maxhp=10,
        thaco=19,
        speed=33,
        tics=0,
        ac=10,
        attacks={
            'teeth': Attack('1d5'),
            'tail': Attack('3d1'),
            'scratch': Attack('2d3'),
        }
    ),


]

_PEEPS_BY_NAME = {m.name: m for m in _PEEPS}

def player_by_name(name, x=0, y=0, hp=0, speed=0):
    ret = _PEEPS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.x = x
    ret.y = y
    return ret


