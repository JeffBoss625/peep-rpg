import os
import curses

import lib.items.clothes as clothes
import lib.items.armor as armor
from lib.logger import Logger
from lib.win_layout import RootLayout, Dim
from lib.prpg_main import main
from lib.peep_types import create_peep
from lib.prpg_model import GameModel
import lib.dungeons as dungeons


# note - to set terminal size on windows machines: os.system("mode con cols=120 lines=40")
#       on mac: os.system("resize -s 40 120")  (rows, cols)
#       on linux:
#           import termios
#           import struct
#           import fcntl
#
#           def set_winsize(fd, row, col, xpix=0, ypix=0):
#               fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", row, col, xpix, ypix))
#
#       or (less robust):
#           import sys
#           sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=32, cols=100))

w, h = os.get_terminal_size()
def cb(scr):
    root_layout = RootLayout(dim=Dim(w,h), border=0, logger=Logger(__file__), scr=scr, curses=curses)
    game = GameModel(create_peep('human', name='Super Dad'))
    game.player.body.wear(clothes.cloak(1.1, 1.1))
    game.player.body.wear(armor.helm(1.15, 1.1))
    game.player.body.wear(armor.shield(1.4, 1.1))

    game.goto_level(1, placement='<')

    main(root_layout, game)


curses.wrapper(cb)

