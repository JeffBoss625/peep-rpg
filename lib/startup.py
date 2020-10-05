import curses
from lib.logger import Logger
from lib.prpg_screen import MainScreen
from lib.screen_layout import WinLayout, Pos, Con, Dim, RootLayout
from lib.dummy_curses import DummyCurses
import os

def create_root(dim=None, out=None):
    if scr:
        if dim:
            raise ValueError('when scr is specified, dim is not supported')
        curseslib = curses
        curses.get_terminal_size = os.get_terminal_size

    else:
        if not dim:
            dim = Dim(40,120)
        curseslib = DummyCurses(dim)
        scr = curseslib.term

    logger = Logger(out)

    root.window = MainScreen(border=0, scr=scr, curses=curseslib, logger=logger)
    return root

# callback using curses.wrapper and providing an initialized root layout component to simplify
# startup.
def curses_wrapper(fn, out=None):
    curses.get_terminal_size = os.get_terminal_size
    w, h = curses.get_terminal_size()
    curses.wrapper(lambda scr: fn(RootLayout(Dim(h,w), logger=Logger(out)), scr, curses))

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
