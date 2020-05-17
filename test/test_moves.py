import lib.moves as movelib

def test_elapse_time():
    peeps = [
        {'peep': {'name': 'p1', 'speed': 10, 'tics': 0}},
        {'peep': {'name': 'p2', 'speed': 7, 'tics': 0}}
    ]
    moves = movelib.elapse_time(peeps)
    assert peeps[0]['peep']['tics'] == 0
    assert peeps[1]['peep']['tics'] == 7

def test_check_wall_collide():
    maze = [
        '..####',
        '.#####'
    ]
    assert movelib.check_wall_collide(maze, 0, 1) == ''
    assert movelib.check_wall_collide(maze, 0, 2) == 'RAN INTO WALL'

def test_handle_player_move():
    maze = [
        '..####',
        '.#####'
    ]
    player = {'x': 0, 'y': 0}
    movelib.handle_player_move(maze, player, movelib.Direction.RIGHT)
    assert player['x'] == 1
    assert player['y'] == 0
    # Run into wall to the right
    movelib.handle_player_move(maze, player, movelib.Direction.RIGHT)
    assert player['x'] == 1
    assert player['y'] == 0
    # Run into wall to the right
    movelib.handle_player_move(maze, player, movelib.Direction.DOWN_RIGHT)
    assert player['x'] == 1
    assert player['y'] == 0


# def test_move_player():
#     maze = [
#         '..####'
#         '.#####'
#     ]
#     player = {'peep': {'name': 'p1', 'speed': 10, 'tics': 0}}
