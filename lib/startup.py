import curses
from lib.logger import Logger
from lib.screen_layout import WinLayout, Pos, Con, Dim
from lib.screen import create_win, WIN
from lib.dummy_curses import DummyCurses
import os

def create_root(dim, out=None, scr=None):
    if scr:
        curseslib = curses
        curses.get_terminal_size = os.get_terminal_size
    else:
        curseslib = DummyCurses(dim)
        scr = curseslib.term

    root = WinLayout(None, 'root', Pos(0, 0), Con(dim.h, dim.w, dim.h, dim.w), wintype=WIN.MAIN, border=0, scr=scr, curses=curseslib)
    root.dim = dim
    root.logger = Logger(out)

    root.data = create_win(None, root.name, root.params)
    root.data.term_size = dim.w, dim.h
    return root

# callback using curses.wrapper and providing an initialized root layout component to simplify
# startup.
def curses_wrapper(fn, out=None):
    w, h = os.get_terminal_size()
    dim = Dim(h, w)
    curses.wrapper(lambda scr: fn(create_root(dim, out, scr)))


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
