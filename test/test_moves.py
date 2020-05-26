import lib.move as movelib
from lib.peep import Peep, Attack
from lib.model import Model
from lib.output import Hector

def test_elapse_time():
    peeps = [
        Peep(name='p1', speed=10),
        Peep(name='p2', speed=7),
    ]
    moves = movelib.elapse_time(peeps)
    assert peeps[0].tics == 0
    assert peeps[1].tics == 7

def test_maze_at_xy():
    maze = [
        '..####',
        '.#####',
    ]
    assert movelib.maze_at_xy(maze, 0, 0) is None
    assert movelib.maze_at_xy(maze, 1, 0) is None
    wall = movelib.maze_at_xy(maze, 2, 0)
    assert wall.type == 'wall'
    assert movelib.maze_at_xy(maze, 0, 1) is None

def test_move_peep():
    peeps = [
        Peep(name='p1', x=0, y=0),     # player information and state
        Peep(name='p1', x=0, y=2),
        Peep(name='p1', x=4, y=3),
    ]

    maze = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    player = peeps[0]
    model = Model(peeps=peeps, maze=maze, out=Hector())
    movelib.move_peep(model, player, movelib.Direction.RIGHT)
    assert player.x == 1 # x changed!
    assert player.y == 0

    # Run into wall (right)
    movelib.move_peep(model, player, movelib.Direction.RIGHT)
    assert player.x == 1
    assert player.y == 0
    # Run into wall diagnally-right
    movelib.move_peep(model, player, movelib.Direction.DOWN_RIGHT)
    assert player.x == 1
    assert player.y == 0
    # Run into wall down
    movelib.move_peep(model, player, movelib.Direction.DOWN)
    assert player.x == 1
    assert player.y == 0
    # Move down left without collision
    movelib.move_peep(model, player, movelib.Direction.DOWN_LEFT)
    assert player.x == 0
    assert player.y == 1

def test_move_attack():
    peeps = [
        Peep(name='p1', x=0, y=1, attacks={'sword': Attack(damage='1d6')}),
        Peep(name='m1', x=0, y=2, hp=5),
        Peep(name='m2', x=4, y=3, hp=10),
    ]
    player = peeps[0]

    maze = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    out = Hector()
    model = Model(peeps=peeps, maze=maze, out=Hector())
    # Run into monster at [0,2]
    movelib.move_peep(model, player, movelib.Direction.DOWN)
    assert player.x == 0
    assert player.y == 1


def test_handle_enemy_move():
    peeps = [
        Peep(name='p1', x=0, y=0),
        Peep(name='m1', x=1, y=2),
        Peep(name='m2', x=4, y=3),
    ]

    maze = [
        '..####',
        '..####',
        '......',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    model = Model(peeps=peeps, maze=maze, player=peeps[0], out=Hector())
    enemy = peeps[1]
    dx = model.player.x - enemy.x
    dy = model.player.y - enemy.y
    edir = movelib.direction_from_vector(dx, dy)

    movelib.move_peep(model, enemy, edir)
    assert enemy.x == 0
    assert enemy.y == 1
    movelib.move_peep(model, enemy, edir)
    assert enemy.x == 0
    assert enemy.y == 1
# def test_move_player():
#     maze = [
#         '..####'
#         '.#####'
#     ]
#     player = {'peep': {'name': 'p1', 'speed': 10, 'tics': 0}}
