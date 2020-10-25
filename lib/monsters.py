from lib.peeps import Peep, Attack, LevelData
from lib.constants import COLOR
from lib.peep_types import create_peep
import yaml

MONSTERS = [
    # GOBLINS
    create_peep('goblin', name='Thark'),
    create_peep('giant rat'),
    create_peep('big bird'),
    create_peep('red dragon', name='Spark'),
    create_peep('black dragon', name='Brog'),
]

MONSTERS_BY_NAME = {m.name:m for m in MONSTERS}

def monster_by_name(name, pos=(0,0), hp=0):
    ret = MONSTERS_BY_NAME[name]
    ret.hp = ret.maxhp if hp == 0 else hp
    ret.pos = pos
    return ret

def color_rep(dumper, data):
    return dumper.represent_scalar('!color', data.name)


if __name__ == '__main__':
    for m in MONSTERS:
        print(yaml.dump(m, sort_keys=False, default_flow_style=False))
