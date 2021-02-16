#!/usr/bin/python

# color picker from Christopher Ferrin's stackflow answer:
# https://stackoverflow.com/questions/18551558/how-to-use-terminal-color-palette-with-curses
from traceback import format_exc

import math
import sys, os, curses
import locale

locale.setlocale(locale.LC_ALL, '')
os.environ.setdefault('ESCDELAY', '250')
os.environ["NCURSES_NO_UTF8_ACS"] = "1"

colors = {'white': curses.COLOR_WHITE, 'red': curses.COLOR_RED, 'green': curses.COLOR_GREEN,
          'yellow': curses.COLOR_YELLOW, 'blue': curses.COLOR_BLUE, 'magenta': curses.COLOR_MAGENTA,
          'cyan': curses.COLOR_CYAN, 'black': curses.COLOR_BLACK}


class SuspendCurses():
    def __enter__(self):
        curses.endwin()

    def __exit__(self, exc_type, exc_val, tb):
        newscr = curses.initscr()
        newscr.refresh()
        curses.doupdate()


def cp(i):
    return curses.color_pair(i)

class COLOR:
    BLACK   = 'black'
    BLUE    = 'blue'
    CYAN    = 'cyan'
    GREEN   = 'green'
    MAGENTA = 'magenta'
    RED     = 'red'
    WHITE   = 'white'
    YELLOW  = 'yellow'
    GRAY = 'gray'
    LT_BLUE = 'lt_blue'
    LT_GREEN = 'lt_green'
    LT_AQUA = 'lt_aqua'
    LT_RED = 'lt_red'
    LT_PURPLE = 'lt_purple'

COLOR8 = {
    'black'   : curses.COLOR_BLACK,
    'blue'    : curses.COLOR_BLUE,
    'cyan'    : curses.COLOR_CYAN,
    'green'   : curses.COLOR_GREEN,
    'magenta' : curses.COLOR_MAGENTA,
    'red'     : curses.COLOR_RED,
    'white'   : curses.COLOR_WHITE,
    'yellow'  : curses.COLOR_YELLOW,
}


def set_pairs(bg):
    i = 1
    for k in COLOR8.keys():
        curses.init_pair(i, COLOR8[k], COLOR8[bg])
        i += 1
    for i in range(8, 16):
        curses.init_pair(i + 1, i, COLOR8[bg])

def main_loop(stdscr):
    try:
        if not curses.can_change_color():
            with SuspendCurses():
                print(f'no color change support')
            return 1

        curses.curs_set(1)  # set curses options and variables
        curses.noecho()
        curses.cbreak()
        maxy, maxx = stdscr.getmaxyx()
        h, w = 24, 80
        if maxy < h or maxx < w:
            with SuspendCurses():
                print(f'Terminal window needs to be at least {h} by {w}')
                print(f'Current h:{maxy}  and w:{maxx}')
            return 1

        stdscr.refresh()
        test_win = curses.newwin(h, w, 0, 0)
        stdscr.nodelay(1)
        test_win.leaveok(0)
        test_win.keypad(1)
        test_win.bkgd(' ', cp(0))
        test_win.box()
        test_win.move(2, 2)
        set_pairs(COLOR.BLACK)
        test_win.refresh()
        # maxc = curses.COLORS
        maxc = len(COLOR8)
        k, newk = 1, 2
        done = False
        while not done:
            if k > -1:
                test_win.clear()
                if k in (ord('q'), 27):
                    done = True
                test_win.addstr(1, 3, f'{len(COLOR8)} colors supported', cp(0))
                for x in range(8):
                    test_win.addstr(3, 2 + x * 2, 'A ', cp(x + 1))
                for x in range(8):
                    test_win.addstr(4, 2 + x * 2, 'A ', cp(x + 9))
                test_win.move(1, 2)
                test_win.box()
                test_win.refresh()
                curses.napms(10)
            newk = stdscr.getch()
            if newk != k:
                k = newk
    except KeyboardInterrupt:
        pass
    except:
        with SuspendCurses():
            print(format_exc())
        return 1

    return 0


if __name__ == '__main__':
    ret = 1
    try:
        ret = curses.wrapper(main_loop)
    except Exception as e:
        print(e)
    finally:
        print('Exit status ' + str(ret))
        sys.exit(ret)
