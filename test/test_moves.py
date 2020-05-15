import lib.moves


def test_elapse_time():
    peeps = [
        {'peep': {'name': 'p1', 'speed': 10, 'tics': 0}},
        {'peep': {'name': 'p2', 'speed': 7, 'tics': 0}}
    ]
    moves = lib.moves.elapse_time(peeps)
    assert peeps[0]['peep']['tics'] == 0
    assert peeps[1]['peep']['tics'] == 7
