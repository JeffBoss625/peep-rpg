# a simple app that launches the game with the 'find_rooms' plug in function to try out
# live plotting
import os
import curses

import random

from lib.find_path import find_rooms
from lib.logger import Logger
from lib.peep_types import create_peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
import lib.dungeons as dungeons
from lib.win_layout import Dim
from lib.win_layout import RootLayout

w, h = os.get_terminal_size()
def cb(scr):
    random.seed = 1

    root_layout = RootLayout(dim=Dim(w,h), border=0, logger=Logger(__file__), scr=scr, curses=curses)
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

    control = PrpgControl(root_layout, game)
    control.input_override['x'] = find_rooms
    main(control)
    # game.maze_model.items = [clothes.belt(pos=(2,2))]
    # root_layout.window.paint(force=True)


curses.wrapper(cb)

