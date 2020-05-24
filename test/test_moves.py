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
        '.#####',
    ]
    assert movelib.check_wall_collide(maze, 0, 0) is None
    assert movelib.check_wall_collide(maze, 1, 0) is None
    wall = movelib.check_wall_collide(maze, 2, 0)
    assert wall['type'] == 'wall'
    assert movelib.check_wall_collide(maze, 0, 1) is None

def test_handle_player_move():
    player_info = {'name': 'p1'}
    player = {'peep': player_info, 'x': 0, 'y': 0}     # player information and state
    peeps = [
        player,
        {'peep': {'name': 'm1'}, 'x': 0, 'y': 2, 'hp': 5},
        {'peep': {'name': 'm1'}, 'x': 4, 'y': 3},
    ]

    maze = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    movelib.move_peep(peeps, maze, player, movelib.Direction.RIGHT)
    assert player['x'] == 1 # x changed!
    assert player['y'] == 0

    # Run into wall (right)
    movelib.move_peep(peeps, maze, player, movelib.Direction.RIGHT)
    assert player['x'] == 1
    assert player['y'] == 0
    # Run into wall diagnally-right
    movelib.move_peep(peeps, maze, player, movelib.Direction.DOWN_RIGHT)
    assert player['x'] == 1
    assert player['y'] == 0
    # Run into wall down
    movelib.move_peep(peeps, maze, player, movelib.Direction.DOWN)
    assert player['x'] == 1
    assert player['y'] == 0
    # Move down left without collision
    movelib.move_peep(peeps, maze, player, movelib.Direction.DOWN_LEFT)
    assert player['x'] == 0
    assert player['y'] == 1

def test_player_move_attack():
    player_info = {'name': 'p1', 'weapons': {'sword': {'damage': '1d6'}}}
    player = {'peep': player_info, 'x': 0, 'y': 1}     # player information and state
    peeps = [
        player,
        {'peep': {'name': 'm1'}, 'x': 0, 'y': 2, 'hp': 5},
        {'peep': {'name': 'm1'}, 'x': 4, 'y': 3},
    ]

    maze = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    # Run into monster at [0,2]
    movelib.move_peep(peeps, maze, player, movelib.Direction.DOWN)
    assert player['x'] == 0
    assert player['y'] == 1



def test_handle_enemy_move():
    peeps = [
        {'peep': {'name': 'p1'}, 'x': 0, 'y': 0},
        {'peep': {'name': 'm1'}, 'x': 1, 'y': 2},
        {'peep': {'name': 'm1'}, 'x': 4, 'y': 3},
    ]

    maze = [
        '..####',
        '..####',
        '......',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    enemy = peeps[1]
    player = peeps[0]
    dx = player['x'] - enemy['x']
    dy = player['y'] - enemy['y']
    edir = movelib.direction_from_vector(dx, dy)

    movelib.move_peep(peeps, maze, enemy, edir)
    assert enemy['x'] == 0
    assert enemy['y'] == 1
    movelib.move_peep(peeps, maze, enemy, edir)
    assert enemy['x'] == 0
    assert enemy['y'] == 1
# def test_move_player():
#     maze = [
#         '..####'
#         '.#####'
#     ]
#     player = {'peep': {'name': 'p1', 'speed': 10, 'tics': 0}}
