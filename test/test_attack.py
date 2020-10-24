from lib.attack import *
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
        # defl, skill   weight  str     dex    round, exp
        #       ratio   ratio
        (0.5,   1.0,    1.0,    1.0,    1.0,   3,    0.5),
        (0.5,   1.5,    1.0,    1.0,    1.0,   3,    0.667),
        (0.5,   1.0,    1.5,    1.0,    1.0,   3,    0.6),
        (0.5,   1.0,    1.0,    1.5,    1.0,   3,    0.6),
        (0.5,   1.0,    1.0,    1.0,    1.5,   3,    0.667),

        (0.5,   1.5,    1.5,    1.0,    1.0,   3,    0.733),
        (0.5,   1.0,    1.5,    1.5,    1.0,   3,    0.68),
        (0.5,   1.0,    1.0,    1.5,    1.5,   3,    0.733),

        (0.5,   1.5,    1.5,    1.5,    1.0,   3,    0.787),
        (0.5,   1.0,    1.5,    1.5,    1.5,   3,    0.787),

        (0.5,   1.5,    1.5,    1.5,    1.5,   3,    0.858),

        (0.3,   1.5,    1.5,    1.5,    1.5,   3,    0.764),

        (0.3,   3.0,    1.5,    0.2,    2.0,   3,    0.817),
        (0.3,   3.0,    1.5,    0.2,    1.0,   3,    0.675),
        (0.3,   0.3,    1.5,    0.2,    1.0,   3,    0.067),
    )
    for defl, skill, weight, str, dex, roundto, exp in data:
        d = calc_deflection(defl, skill, weight, PlayerStats(str=str, dex=dex), roundto=roundto)
        assert d == exp

def test_attack():
    p1 = Peep(name='p1', hp=3, attacks={'teeth': Attack(damage='1d3')})
    p2 = Peep(name='m1', hp=2, attacks={'teeth': Attack(damage='1d3')})

    out = Out()

    attack(p1, p2, 'teeth', out, 3)
    assert p2.hp == 2
    attack(p2, p1, 'teeth', out, 3)
    assert p1.hp == 3
    attack(p1, p2, 'teeth', out, 3)
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

