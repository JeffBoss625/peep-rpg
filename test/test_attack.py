import lib.attack as attacklib

def test_attack():
    p1 = {'hp': 3, 'peep': {'name': 'p1', 'weapons': {'teeth': {'damage': '1d3'}}}}
    p2 = {
        'hp': 2,
        'peep': {
            'name': 'm1',
            'weapons': {
                'teeth': {
                    'damage': '1d3'
                }
            }
        },

    }
    attacklib.attack(p1, p2, 'teeth', 3)
    assert p2['hp'] == 1
    attacklib.attack(p2, p1, 'teeth', 3)
    assert p1['hp'] == 2
    attacklib.attack(p1, p2, 'teeth', 3)
    assert p2['hp'] == 0