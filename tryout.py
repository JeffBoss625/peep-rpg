import curses
import signal
from lib.curwin import *

def main(scr):
    curses.raw()
    root = rootwin(scr)

    while 1:
        h.paint()
        scr.refresh()
        c = scr.getch()
        if c == ord('q'):
            break


curses.wrapper(main)