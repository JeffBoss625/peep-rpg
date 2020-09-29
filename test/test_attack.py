import lib.attack as attacklib
from lib.peeps import Attack, Peep


class Out:
    def __init__(self):
        self.args = []

    def message(self, *args):
        self.args.append(args)

    def log(self, *args):
        self.args.append(args)

def test_attack():
    p1 = Peep(name='p1', hp=3, attacks={'teeth': Attack(damage='1d3')})
    p2 = Peep(name='m1', hp=2, attacks={'teeth': Attack(damage='1d3')})

    out = Out()

    attacklib.attack(p1, p2, 'teeth', out, 3)
    assert p2.hp == 2
    attacklib.attack(p2, p1, 'teeth', out, 3)
    assert p1.hp == 3
    attacklib.attack(p1, p2, 'teeth', out, 3)
    assert p2.hp == 2

    # try this.... not changing.
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attacklib.attack(p1, p2, 'teeth', out, 3)
    # attacklib.attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
