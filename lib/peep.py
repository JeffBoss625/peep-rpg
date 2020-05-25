import dataclasses as dclib

@dclib.dataclass
class Attack:
    damage: str = '1d1'
    range: int = 0

@dclib.dataclass
class Peep:
    name: str = ''
    type: str = ''
    char: str = '?'
    maxhp: int = 0
    thaco: int = 20
    speed: int = 10
    ac: int = 10

    # temp state
    hp: int = 0
    tics: int = 0
    x: int = 0
    y: int = 0
    attacks: dict = dclib.field(default_factory=dict)


CLASS_FIELDS = {}

def class_fields(klass):
    if klass not in CLASS_FIELDS:
        CLASS_FIELDS[klass] = {f.name: f.type for f in dclib.fields(klass)}
    return CLASS_FIELDS[klass]

def from_dict(klass, d):
    if not dclib.is_dataclass(klass):
        return d
    fields = class_fields(klass)
    args = {}
    for f in d:
        if f not in fields:
            raise KeyError(str(klass.__name__) + ' has no property "' + f + '"')
        args[f] = from_dict(fields[f], d[f])

    ret = klass(**args)
    return ret


if __name__ == "__main__":
    p1 = Peep(name='p1', maxhp=7)
    p1.attacks['teeth'] = Attack()
    p2 = from_dict(Peep, {'name': 'p2', 'maxhp': 3})
    print(p1)
    print(p2)