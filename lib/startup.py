import curses
from lib.logger import Logger
from lib.prpg_screen import MainScreen
from lib.screen_layout import WinLayout, Pos, Con, Dim
from lib.dummy_curses import DummyCurses
import os

def create_root(dim=None, out=None, scr=None, name='root'):
    if scr:
        if dim:
            raise ValueError('when scr is specified, dim is not supported')
        curseslib = curses
        curses.get_terminal_size = os.get_terminal_size
        w, h = os.get_terminal_size()
        dim = Dim(h, w)
    else:
        if not dim:
            dim = Dim(40,120)
        curseslib = DummyCurses(dim)
        scr = curseslib.term

    logger = Logger(out)
    root = WinLayout(None, name, Pos(0, 0), Con(dim.h, dim.w, dim.h, dim.w), logger=logger)
    root.dim = dim

    root.data = MainScreen(border=0, scr=scr, curses=curseslib, logger=logger)
    root.data.term_size = dim.w, dim.h
    return root

# callback using curses.wrapper and providing an initialized root layout component to simplify
# startup.
def curses_wrapper(fn, name='root', out=None):
    curses.wrapper(lambda scr: fn(create_root(name=name, out=out, scr=scr)))

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
