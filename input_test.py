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


def set_pairs(bg, ncolors):
    for i, fg in enumerate(range(ncolors)):
        curses.init_pair(i+1, fg, bg)


def main_loop(stdscr):
    try:
        curses.curs_set(1)  # set curses options and variables
        curses.noecho()
        curses.cbreak()
        maxc = curses.COLORS
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
        fgcol, bgcol = 0, 0
        set_pairs(bgcol, maxc)
        test_win.refresh()
        k, newk = 1, 2
        done = False
        while not done:
            if k > -1:
                test_win.clear()
                if k == ord('-'):  # decr currently selected attr
                    fgcol -= 1
                    if fgcol < 0: fgcol = maxc - 1
                    set_pairs(fgcol, maxc)
                if k == ord('+') or k == ord('='):  # incr currently selected attr
                    fgcol += 1
                    if fgcol > maxc - 1: fgcol = 0
                    set_pairs(fgcol, maxc)
                if k in (ord('q'), 27):
                    done = True
                test_win.addstr(1, 10, f'{maxc} colors supported', cp(0))
                test_win.addstr(2, 2, f'FG: {fgcol}  ', cp(0))
                nrows = math.ceil(maxc/32)
                for y in range(nrows):
                    for x in range(32):
                        test_win.addstr(4 + y, 3 + x*2, 'A ', cp(y*32 + x + 1))
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
