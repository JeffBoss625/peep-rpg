from lib.peep_types import create_peep

_PEEPS = [
    create_peep('dog', name='Bo Bo the Destroyer'),
    create_peep('human', name='Super Dad', height=1.3, weight=1.5, head2body=8.0 ),
]

_PEEPS_BY_NAME = {m.name: m for m in _PEEPS}

def player_by_name(name, pos=(0,0), maxhp=0):
    ret = _PEEPS_BY_NAME[name]
    if maxhp > 0:
        ret.maxhp = maxhp
    ret.hp = ret.maxhp
    ret.pos = pos
    return ret


