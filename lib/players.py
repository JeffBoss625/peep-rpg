from lib.peep_types import create_peep

_PEEPS = [
    create_peep('dog', name='Bo Bo the Destroyer'),
    create_peep('human', name='Super Dad', body_stats={'height':203, 'weight':120, 'body2head':8.0} ),
]

_PEEPS_BY_NAME = {m.name: m for m in _PEEPS}

def player_by_name(name, pos=(0,0), hp=0):
    ret = _PEEPS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.pos = pos
    return ret


