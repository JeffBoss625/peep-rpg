import lib.move as mlib
from lib.move import Direction
from lib.model import Peep, Attack
from lib.prpg_model import PrpgModel

def test_elapse_time():
    peeps = [
        Peep(name='p1', speed=10),
        Peep(name='p2', speed=7),
    ]
    moves = mlib.elapse_time(peeps)
    assert peeps[0].tics == 0
    assert peeps[1].tics == 7

def test_maze_at_xy():
    maze = [
        '..####',
        '.#####',
    ]
    assert mlib.maze_at_xy(maze, 0, 0) is None
    assert mlib.maze_at_xy(maze, 1, 0) is None
    wall = mlib.maze_at_xy(maze, 2, 0)
    assert wall.type == 'wall'
    assert mlib.maze_at_xy(maze, 0, 1) is None

def test_move_peep():
    peeps = [
        Peep(name='p1', x=0, y=0),     # player information and state
        Peep(name='p1', x=0, y=2),
        Peep(name='p1', x=4, y=3),
    ]

    walls = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    player = peeps[0]
    model = PrpgModel(walls=walls, peeps=peeps)
    mlib.move_peep(model, player, mlib.Direction.RIGHT)
    assert player.x == 1 # x changed!
    assert player.y == 0

    # Run into wall (right)
    mlib.move_peep(model, player, mlib.Direction.RIGHT)
    assert player.x == 1
    assert player.y == 0
    # Run into wall diagnally-right
    mlib.move_peep(model, player, mlib.Direction.DOWN_RIGHT)
    assert player.x == 1
    assert player.y == 0
    # Run into wall down
    mlib.move_peep(model, player, mlib.Direction.DOWN)
    assert player.x == 1
    assert player.y == 0
    # Move down left without collision
    mlib.move_peep(model, player, mlib.Direction.DOWN_LEFT)
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
    model = PrpgModel(peeps=peeps, maze=maze)
    # Run into monster at [0,2]
    mlib.move_peep(model, player, mlib.Direction.DOWN)
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
    model = PrpgModel(peeps=peeps, maze=maze, player=peeps[0])
    enemy = peeps[1]
    dx = model.player_model.x - enemy.x
    dy = model.player_model.y - enemy.y
    edir = mlib.direction_from_vector(dx, dy)

    mlib.move_peep(model, enemy, edir)
    assert enemy.x == 0
    assert enemy.y == 1
    mlib.move_peep(model, enemy, edir)
    assert enemy.x == 0
    assert enemy.y == 1

def test_direction_relative():

    assert mlib.direction_relative(Direction.UP, 0) == Direction.UP
    assert mlib.direction_relative(Direction.UP, 1) == Direction.UP_RIGHT
    assert mlib.direction_relative(Direction.UP, 2) == Direction.RIGHT
    assert mlib.direction_relative(Direction.UP, 3) == Direction.DOWN_RIGHT
    assert mlib.direction_relative(Direction.UP, 4) == Direction.DOWN
    assert mlib.direction_relative(Direction.UP, 5) == Direction.DOWN_LEFT
    assert mlib.direction_relative(Direction.UP, 6) == Direction.LEFT
    assert mlib.direction_relative(Direction.UP, 7) == Direction.UP_LEFT
    assert mlib.direction_relative(Direction.UP, 8) == Direction.UP
    assert mlib.direction_relative(Direction.UP, 9) == Direction.UP_RIGHT

    assert mlib.direction_relative(Direction.DOWN, 0) == Direction.DOWN
    assert mlib.direction_relative(Direction.DOWN, 1) == Direction.DOWN_LEFT
    assert mlib.direction_relative(Direction.DOWN, 2) == Direction.LEFT
    assert mlib.direction_relative(Direction.DOWN, 3) == Direction.UP_LEFT
    assert mlib.direction_relative(Direction.DOWN, 4) == Direction.UP
    assert mlib.direction_relative(Direction.DOWN, 5) == Direction.UP_RIGHT

    assert mlib.direction_relative(Direction.DOWN, -1) == Direction.DOWN_RIGHT
    assert mlib.direction_relative(Direction.DOWN, -2) == Direction.RIGHT
    assert mlib.direction_relative(Direction.DOWN, -3) == Direction.UP_RIGHT
    assert mlib.direction_relative(Direction.DOWN, -4) == Direction.UP
    assert mlib.direction_relative(Direction.DOWN, -5) == Direction.UP_LEFT
    assert mlib.direction_relative(Direction.DOWN, -6) == Direction.LEFT
    assert mlib.direction_relative(Direction.DOWN, -7) == Direction.DOWN_LEFT
    assert mlib.direction_relative(Direction.DOWN, -8) == Direction.DOWN
    assert mlib.direction_relative(Direction.DOWN, -9) == Direction.DOWN_RIGHT
    assert mlib.direction_relative(Direction.DOWN, -10) == Direction.RIGHT
