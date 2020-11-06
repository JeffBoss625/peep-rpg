from lib.attack import calc_deflection, attack_dst
from lib.peeps import Attack, Peep
from lib.stat import PlayerStats


class Out:
    def __init__(self):
        self.args = []

    def message(self, *args):
        self.args.append(args)

    def log(self, *args):
        self.args.append(args)


def test_calc_deflection():
    data = (
        # defl, skill   str     dex    exp
        #       ratio
        (0.5,   1.0,    1.0,    1.0,  0.5),
        (0.5,   1.5,    1.0,    1.0,  0.667),
        (0.5,   1.0,    1.5,    1.0,  0.6),
        (0.5,   1.0,    1.0,    1.5,  0.667),

        (0.5,   1.0,    1.5,    1.5,  0.733),
        (0.5,   1.5,    1.5,    1.0,  0.733),

        (0.5,   1.5,    1.5,    1.5,  0.822),

        (0.3,   3.0,    0.2,    2.0,  0.787),
        (0.3,   1.0,    0.2,    3.0,  0.54),
        (0.3,   3.0,    0.2,    1.0,  0.54),
        (0.3,   0.3,    0.2,    1.0,  0.054),
    )
    for defl, skill, str, dex, exp in data:
        d = calc_deflection(defl, skill, PlayerStats(str=str, dex=dex))
        assert d == exp

def test_attack():
    p1 = Peep(name='p1', hp=3, attacks=(Attack('teeth', damage='1d3'),))
    p2 = Peep(name='m1', hp=2, attacks=(Attack('kick', damage='1d3'),))

    out = Out()

    attack_dst(p1, p2, p1.attacks[0], out, 3)
    assert p2.hp == 2
    attack_dst(p2, p1, p2.attacks[0], out, 3)
    assert p1.hp == 3
    attack_dst(p1, p2, p1.attacks[0], out, 3)
    assert p2.hp == 2

    # try this.... not changing.
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)

