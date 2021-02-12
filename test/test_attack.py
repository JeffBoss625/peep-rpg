from lib.attack import calc_deflection, attack_dst
from lib.pclass import level_calc
from lib.peeps import Attack, Peep
from lib.stat import PlayerStats
import random
import math

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
    p1 = Peep(name='p1', hp=4, attacks=(Attack('teeth', damage='1d3'),))
    m1 = Peep(name='m1', hp=5, attacks=(Attack('kick', damage='1d3'),))

    out = Out()
    random.seed(5)
    attack_dst(p1, m1, p1.attacks[0], out)
    assert m1.hp == 3
    attack_dst(m1, p1, m1.attacks[0], out)
    assert p1.hp == 1
    attack_dst(p1, m1, p1.attacks[0], out)
    assert m1.hp == 2

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

def xptolevel_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base*math.pow(factor, i)
        ret += addon
    return ret

def test_xptolevel_calc():
    data = (
        (1, 2, 100, 100),
        (2, 2, 100, 300),
        (3, 2, 100, 700),
        (1, 2.5, 100, 100),
        (2, 2.5, 100, 350),
        (3, 2.5, 100, 975),
    )
    for level, factor, base, exp in data:
        lc = xptolevel_calc(level, factor, base)
        # print(lc)
        assert lc == exp

def test_level_calc():
    data = (
        (0, 2, 1),
        (1, 2, 1),
        (99, 2, 1),
        (100, 2, 2),
        (101, 2, 2),
        (299, 2, 2),
        (300, 2, 3),
        (301, 2, 3),
        (699, 2, 3),
        (700, 2, 4),
        (701, 2, 4),
        (1499, 2, 4),
    )
    for xp, factor, exp in data:
        lc = level_calc(xp, factor, 100)
        print(f'level_calc({xp}, {factor}) = {lc} (expected {exp})')
        # assert lc == exp
