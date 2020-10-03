from lib.peeps import Peep, Attack, create_humanoid, RACE

_PEEPS = [
    Peep(
        name='Bo Bo the Destroyer',
        type='dog',
        char='d',
        maxhp=100,
        thaco=19,
        speed=33,
        tics=0,
        ac=10,
        attacks={
            'teeth': Attack('1d10'),
            'tail': Attack('3d5'),
            'scratch': Attack('2d7'),
        },
        body=create_humanoid(RACE.HUMAN, 200, 100, 7.5)
    ),


]

_PEEPS_BY_NAME = {m.name: m for m in _PEEPS}

def player_by_name(name, pos=(0,0), hp=0, speed=0):
    ret = _PEEPS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.pos = pos
    return ret


