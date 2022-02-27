import random
from lib.logger import Logger
from lib.peep_types import create_peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as dungeons
from lib.constants import Key
from lib.win_layout import Dim


def assert_game(game, keys, paint=False):
    root_layout = dummy_root(dim=Dim(110, 21), logger=Logger('dbg.py'))
    control = PrpgControl(root_layout, game, pack=True)

    def get_key():
        if paint:
            control.root_layout.window.paint()
        ret = keys.pop(0)
        return ret

    control.get_key = get_key
    main(control)


def test_find_rooms():
    random.seed = 1
    game = dungeons.create_game({
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%....####....######%.........%%%%%%%%%%%%%',
            '%....####....######%.........%%%%%%%%%%%%%',
            '%....####....####..#.........%%%%%%%%%%%%%',
            '%............####..#.........%%%%%%%%%%%%%',
            '%....####....####............%%%%%%%%%%%%%',
            '%....####..........#.........%%%%%%%%%%%%%',
            '%....####....#######.........%%%%%%%%%%%%%',
            '%....####....#######.........%%%%%%%%%%%%%',
            '%###########.###############.%%%%%%%%%%%%%',
            '%###########.###############.%%%%%%%%%%%%%',
            '%###########.................%%%%%%%%%%%%%',
            '%#############.##############%%%%%%%%%%%%%',
            '%#############.##############%#####.#####%',
            '%#########.........##########%###....####%',
            '%#####..................#####%#........##%',
            '%###....................................#%',
            '%####....................####%#........##%',
            '%#####..................#####%###....####%',
            '%#########.........##########%#####.#####%',
            '%#############.##############%%%%%%%%%%%%%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1, 1)),
        ]
    })
    assert_game(game, ['a', '*', 't', '.', '.', Key.CTRL_Q], paint=True)

def find_dir(maze, pos):
    can = []
    down = (pos[1]+1, pos[0])
    up = (pos[1]-1, pos[0])
    left = (pos[1], pos[0] - 1)
    right = {pos[1], pos[0] + 1}
    if maze[down] == ".":
        can.append(down)
    if maze[up] == '.':
        can.append(up)
    if maze[left] == '.':
        can.append(left)
    if maze[right] == ".":
        can.append(right)
    return(can)

def find_rooms(maze, start):
    facing = None
    hall = []
    pos = start
    been = []
    while maze[pos[1]][pos[0] - 1] == '.':
        pos[0] = pos[0] + 1
    while pos not in been:


        while facing == 'up':
            while maze[pos[1] - 1][pos[0]] == '.' and maze[pos[1]][pos[0] - 1] == '#':  # FACING UP
                if maze[pos[1]][pos[0] + 1] == '#':
                    # mark exit
                    pos[0] = pos[0] + 1
                    pos[1] = pos[1] + 1
                    facing = 'right'
                    break
                # been here
                been.append(pos)
                pos[1] = pos[1] + 1
            if facing == 'up':
                if maze[pos[1] - 1][pos[0]] == '#':
                    facing = 'right'
                else:
                    facing = 'left'
                    pos[0] = pos[0] - 1

        while facing == 'down':
            while maze[pos[1] + 1][pos[0]] == '.' and maze[pos[1]][pos[0] + 1] == '#':  # FACING DOWN
                if maze[pos[1]][pos[0] - 1] == '#':
                    # mark exit
                    pos[0] = pos[0] - 1
                    pos[1] = pos[1] - 1
                    facing = 'right'
                    break
                # been here
                been.append(pos)
                pos[1] = pos[1] + 1
            if facing == 'down':
                if maze[pos[1] + 1][pos[0]] == '#':
                    facing = 'left'
                else:
                    facing = 'right'
                    pos[0] = pos[0] - 1

        while facing == 'right':
            while maze[pos[1]][pos[0] + 1] == '.' and maze[pos[1] - 1][pos[0]] == '#':  # FACING RIGHT
                if maze[pos[1] + 1][pos[0]] == '#':
                    # mark exit
                    pos[0] = pos[0] - 1
                    pos[1] = pos[1] + 1
                    facing = 'down'
                    break
                # been here
                been.append(pos)
                pos[1] = pos[1] + 1
            if facing == 'right':
                if maze[pos[1]][pos[0] + 1] == '#':
                    facing = 'down'
                else:
                    facing = 'up'
                    pos[0] = pos[0] - 1

        while facing == "left":
            while maze[pos[1]][pos[0] - 1] == '.' and maze[pos[1] + 1][pos[0]] == '#':  # FACING LEFT
                if maze[pos[1] - 1][pos[0]] == '#':
                    # mark exit
                    pos[0] = pos[0] + 1
                    pos[1] = pos[1] - 1
                    facing = 'up'
                    break
                # been here
                been.append(pos)
                pos[1] = pos[1] + 1
            if facing == 'left':
                if maze[pos[1]][pos[0] - 1] == '#':
                    facing = 'up'
                else:
                    facing = 'down'
                    pos[0] = pos[0] - 1
