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

def monster_by_name(name, pos=(0,0), maxhp=0):
    ret = MONSTERS_BY_NAME[name]
    if maxhp > 0:
        ret.hp = maxhp
    ret.hp = ret.maxhp
    ret.pos = pos
    return ret

def color_rep(dumper, data):
    return dumper.represent_scalar('!color', data.name)


if __name__ == '__main__':
    for m in MONSTERS:
        print(yaml.dump(m, sort_keys=False, default_flow_style=False))
