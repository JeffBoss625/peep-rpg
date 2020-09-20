import os
import curses
from lib.logger import Logger
from lib.screen_layout import WinLayout, Pos, Con, Dim
from lib.screen import create_win
from lib.dummy_curses import DummyCurses

def create_root(dim, out=None, scr=None):
    root = WinLayout(None, 'root', Pos(0, 0), Con(dim.h, dim.w, dim.h, dim.w))
    root.dim = dim
    root.logger = Logger(out)

    if scr:
        curses_lib = curses
    else:
        curses_lib = DummyCurses(dim)
        scr = curses_lib.term
        root.curses = curses_lib

    root.data = create_win(root, curses_lib)
    root.data.scr = scr
    root.data.border = 0
    return root

# callback using curses.wrapper and providing an initialized root layout component to simplify
# startup.
def curses_wrapper(fn, out=None):
    w, h = os.get_terminal_size()
    dim = Dim(h, w)
    curses.wrapper(lambda scr: fn(create_root(dim, out, scr), curses))


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
