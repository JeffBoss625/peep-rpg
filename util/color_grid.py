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

# CGA COLOR NAMES
# 0 = Black     8 = Gray
# 1 = Blue      9 = Light Blue
# 2 = Green     A = Light Green
# 3 = Aqua      B = Light Aqua
# 4 = Red       C = Light Red
# 5 = Purple    D = Light Purple
# 6 = Yellow    E = Light Yellow
# 7 = White	    F = Bright White

class COLOR:
    BLACK   = 'black'
    BLUE    = 'blue'
    GREEN   = 'green'
    AQUA    = 'aqua'
    RED     = 'red'
    PURPLE  = 'purple'
    YELLOW  = 'yellow'
    WHITE   = 'white'

    GRAY = 'gray'
    LT_BLUE   = 'lt_blue'
    LT_GREEN  = 'lt_green'
    LT_AQUA   = 'lt_aqua'
    LT_RED    = 'lt_red'
    LT_PURPLE = 'lt_purple'
    LT_YELLOW = 'lt_yellow'
    LT_WHITE  = 'lt_white'


COLOR8 = {
    'black'   : curses.COLOR_BLACK,
    'blue'    : curses.COLOR_BLUE,
    'green'   : curses.COLOR_GREEN,
    'aqua'    : curses.COLOR_CYAN,
    'red'     : curses.COLOR_RED,
    'purple'  : curses.COLOR_MAGENTA,
    'yellow'  : curses.COLOR_YELLOW,
    'white'   : curses.COLOR_WHITE,
}

COLOR16 = {
    'win32': {
        'gray'  : 8,
        'lt_blue': 9,
        'lt_green': 10,
        'lt_aqua': 11,
        'lt_red': 12,
        'lt_purple': 13,
        'lt_yellow': 14,
        'lt_white': 15,
    },
    # darwin is used also as the defualt (linux...)
    'darwin': {
        'gray'  : 8,
        'lt_blue': 12,
        'lt_green': 10,
        'lt_aqua': 14,
        'lt_red': 9,
        'lt_purple': 13,
        'lt_yellow': 11,
        'lt_white': 15,
    }
}

def set_pairs(bg, os_name):
    i = 0
    for k in COLOR8.keys():
        i += 1
        curses.init_pair(i, COLOR8[k], COLOR8[bg])

    if os_name not in COLOR16:
        os_name = 'darwin'
    c16 = COLOR16[os_name]
    for k in c16.keys():
        i += 1
        curses.init_pair(i, c16[k], COLOR8[bg])

    for i in range(16, 255):
        curses.init_pair(i+1, i, 0)

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
        h, w = 22, 80
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
        set_pairs(COLOR.BLACK, sys.platform)
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
                test_win.addstr(1, 3, f'{curses.COLORS} colors supported', cp(0))
                for i in range(256):
                    row = i // 16
                    x = i % 16
                    hx = hex(i)[2:].upper()
                    if len(hx) == 1:
                        hx = '0' + hx
                    test_win.addstr(3 + row, 5 + x * 4, hx, cp(i + 1))

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
