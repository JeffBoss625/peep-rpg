import lib.attack as attacklib
from lib.peep import Peep, Attack

def test_attack():
    p1 = Peep(name='p1', hp=3, attacks={'teeth': Attack(damage='1d3')})
    p2 = Peep(name='m1', hp=2, attacks={'teeth': Attack(damage='1d3')})

    attacklib.attack(p1, p2, 'teeth', 3)
    assert p2.hp == 1
    attacklib.attack(p2, p1, 'teeth', 3)
    assert p1.hp == 2
    attacklib.attack(p1, p2, 'teeth', 3)
    assert p2.hp == 0