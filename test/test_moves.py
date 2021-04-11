import lib.move as mlib
from lib.move import Direction
from lib.peeps import Peep, Attack
from lib.game import GameModel
from lib.game import elapse_time
import sys

def printe(s):
    sys.stderr.write(str(s))
    sys.stderr.write('\n')

def test_elapse_time():
    peeps = [
        Peep(name='p10', speed=10),
        Peep(name='p07', speed=7),
        Peep(name='p02', speed=2),
    ]
    data = (
        # fac  moves  tics remaining
        ( 1.0, [1,0,0], (0.0, 7.0, 2.0) ),
        ( 1.0, [1,1,0], (0.0, 4.0, 4.0) ),
        ( 1.0, [1,1,0], (0.0, 1.0, 6.0) ),
        ( 1.0, [1,0,0], (0.0, 8.0, 8.0) ),
        ( 1.0, [1,1,1], (0.0, 5.0, 0.0) ),
        ( 0.5, [0,0,0], (5.0, 8.5, 1.0) ),
        ( 0.1, [0,0,0], (6.0, 9.2, 1.2) ),
        ( 0.2, [0,1,0], (8.0, 0.6, 1.6) ),
        ( 0.3, [1,0,0], (1.0, 2.7, 2.2) ),
    )
    for t, expmoves, exptics in data:
        printe(f'{t} {expmoves} {exptics}')
        moves = elapse_time(peeps, t)
        tics = tuple(p.tics for p in peeps)
        assert moves == expmoves
        assert tics == exptics


def test_move_peep():
    peeps = [
        Peep(name='p1', pos=(0,0)),     # player information and state
        Peep(name='p1', pos=(0,2)),
        Peep(name='p1', pos=(4,3)),
    ]

    walls = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    player = peeps[0]
    model = GameModel(walls=walls, peeps=peeps)
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.RIGHT))
    assert player.pos == (1,0) # x changed!

    # Run into wall (right)
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.RIGHT))
    assert player.pos == (1,0)
    # Run into wall diagnally-right
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.DOWN_RIGHT))
    assert player.pos == (1,0)
    # Run into wall down
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.DOWN))
    assert player.pos == (1,0)
    # Move down left without collision
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.DOWN_LEFT))
    assert player.pos == (0,1)

def test_move_attack():
    peeps = [
        Peep(name='p1', pos=(0,1), attacks=(Attack(name='sword', damage='1d6'),)),
        Peep(name='m1', pos=(0,2), hp=5),
        Peep(name='m2', pos=(4,3), hp=10),
    ]
    player = peeps[0]

    walls = [
        '..####',
        '.#####',
        '.#....',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    model = GameModel(peeps=peeps, walls=walls)
    # Run into monster at [0,2]
    mlib.move_peep(model, player, mlib.adjacent_pos(player.pos, mlib.Direction.DOWN))
    assert player.pos == (0,1)


def test_handle_enemy_move():
    peeps = [
        Peep(name='p1', pos=(0,0)),
        Peep(name='m1', pos=(1,2)),
        Peep(name='m2', pos=(4,3)),
    ]

    walls = [
        '..####',
        '..####',
        '......',        # monster here on the left at [0,2].
        '......',        # monster here at [4,3]
    ]
    model = GameModel(peeps=peeps, walls=walls, player=peeps[0])
    enemy = peeps[1]
    dx = model.maze_model.player.pos[0] - enemy.pos[0]
    dy = model.maze_model.player.pos[0] - enemy.pos[0]
    edir = mlib.direction_from_vector(dx, dy)

    mlib.move_peep(model, enemy, mlib.adjacent_pos(enemy.pos, edir))
    assert enemy.pos == (0,1)
    mlib.move_peep(model, enemy, mlib.adjacent_pos(enemy.pos, edir))
    assert enemy.pos == (0,1)

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
