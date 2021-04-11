import random

from lib.logger import Logger
from lib.prpg_control import PrpgControl
from lib.startup import dummy_root
from lib.target import *
import lib.dungeons as dungeons
from lib.peep_types import create_peep
from lib.win_layout import Dim


def test_line_points():
    data = (
        ((6,6), (8,0), ()),
        # ((3,3), (0,3), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (0,2), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (0,1), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (0,0), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (1,0), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (2,0), ((3, 3), (2, 3), (1, 3), (0, 3))),
        # ((3,3), (3,0), ((3, 3), (3, 2), (3, 1), (3, 0))),
        # ((3,3), (6,3), ((3, 3), (4, 3), (5, 3), (6, 3))),
        # ((3,3), (3,6), ((3, 3), (3, 4), (3, 5), (3, 6))),
    )

    for p1, p2, exp in data:
        points = tuple(line_points(p1,p2))
        print(f'line_points({p1}, {p2}) = {points}')

        # assert points == exp

def test_draw_target():
    data = (
        (0, -4),
        (1, -4),
        (2, -4),
        (3, -4),
        (4, -4),
        (4, -3),
        (4, -2),
        (4, -1),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (3, 4),
        (2, 4),
        (1, 4),
        (0, 4),
        (-1, 4),
        (-2, 4),
        (-3, 4),
        (-4, 4),
        (-4, 3),
        (-4, 2),
        (-4, 1),
        (-4, 0),
        (-4, -1),
        (-4, -2),
        (-4, -3),
        (-4, -4),
        (-3, -4),
        (-2, -4),
        (-1, -4),
        (0, -4),
    )
    random.seed = 1
    game = dungeons.create_game({
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%......................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(6,6)),
        ]
    })
    root_layout = dummy_root(dim=Dim(100, 22), logger=Logger('dbg.py'))
    control = PrpgControl(root_layout, game)
    player = game.maze.peeps[0]
    for target in data:
        tp = (player.pos[0] + target[0], player.pos[1] + target[1])
        game.maze.target = tuple(line_points(player.pos, tp))
        control.root_layout.window.paint()
