import curses
from lib.logger import Logger
from lib.screen_layout import Dim, RootLayout
import os

# callback using curses.wrapper and providing an initialized root layout component to simplify
# startup.
def curses_wrapper(fn, out=None):
    w, h = os.get_terminal_size()
    curses.wrapper(lambda scr: fn(RootLayout(dim=Dim(h,w), border=0, logger=Logger(out), scr=scr, curses=curses)))

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
