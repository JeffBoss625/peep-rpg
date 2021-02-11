import os
import curses

from lib.logger import Logger
from lib.prpg_control import PrpgControl
from lib.win_layout import RootLayout, Dim
from lib.prpg_main import main
import lib.dungeons as models

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
    dungeon = models.create_dungeon('dungeon1')
    control = PrpgControl(root_layout, dungeon)
    main(control, dungeon)


curses.wrapper(cb)

