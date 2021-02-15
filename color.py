#!/usr/bin/python

# color picker from Christopher Ferrin's stackflow answer:
# https://stackoverflow.com/questions/18551558/how-to-use-terminal-color-palette-with-curses
from traceback import format_exc
import sys, os, curses
import locale

locale.setlocale(locale.LC_ALL, '')
os.environ.setdefault('ESCDELAY', '250')
os.environ["NCURSES_NO_UTF8_ACS"] = "1"

move_dirs = {
    curses.KEY_DOWN: (1, 0),
    curses.KEY_UP: (-1, 0),
    curses.KEY_RIGHT: (0, 1),
    curses.KEY_LEFT: (0, -1),
    ord('s'): (1, 0),
    ord('w'): (-1, 0),
    ord('d'): (0, 1),
    ord('a'): (0, -1),
}

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


def set_pairs(fg, bg):
    curses.init_pair(1, fg, colors['black'])
    curses.init_pair(2, fg, colors['yellow'])
    curses.init_pair(3, fg, colors['white'])
    curses.init_pair(4, fg, colors['red'])
    curses.init_pair(5, colors['black'], bg)
    curses.init_pair(6, colors['yellow'], bg)
    curses.init_pair(7, colors['white'], bg)
    curses.init_pair(8, colors['red'], bg)


def main_loop(stdscr):
    try:
        curses.curs_set(1)  # set curses options and variables
        curses.noecho()
        curses.cbreak()
        maxc = curses.COLORS
        maxy, maxx = stdscr.getmaxyx()
        if maxy < 10 or maxx < 65:
            with SuspendCurses():
                print('Terminal window needs to be at least 10h by 65w')
                print('Current h:{0}  and w:{1}'.format(maxy, maxx))
            return 1

        stdscr.refresh()
        h, w = 10, 65
        test_win = curses.newwin(h, w, 0, 0)
        stdscr.nodelay(1)
        test_win.leaveok(0)
        test_win.keypad(1)
        test_win.bkgd(' ', cp(0))
        test_win.box()
        cursor = [2, 0]
        test_win.move(2, 2 + cursor[1] * 20)
        fgcol, bgcol = 1, 1
        set_pairs(fgcol, bgcol)
        test_win.refresh()
        cursor_bounds = ((0, 0), (0, 1))
        teststr = '! @ # $ % ^ & *     _ + - = '
        k, newk = 1, 2
        exit = False
        while not exit:
            if k > -1:
                test_win.clear()
                if k in move_dirs.keys():  # move cursor left or right with wrapping
                    cursor[1] += move_dirs[k][1]
                    if cursor[1] > cursor_bounds[1][1]: cursor[1] = cursor_bounds[1][0]
                    if cursor[1] < cursor_bounds[1][0]: cursor[1] = cursor_bounds[1][1]
                if k == ord('-'):  # decr currently selected attr
                    if cursor[1] == 0:
                        fgcol -= 1
                        if fgcol < 0: fgcol = maxc - 1
                    else:
                        bgcol -= 1
                        if bgcol < 0: bgcol = maxc - 1
                    set_pairs(fgcol, bgcol)
                if k == ord('+') or k == ord('='):  # incr currently selected attr
                    if cursor[1] == 0:
                        fgcol += 1
                        if fgcol > maxc - 1: fgcol = 0
                    else:
                        bgcol += 1
                        if bgcol > maxc - 1: bgcol = 0
                    set_pairs(fgcol, bgcol)
                if k in (ord('q'), 27):
                    exit = True
                test_win.addstr(1, 10, '{0} colors supported'.format(maxc), cp(0))
                test_win.addstr(2, 2, 'FG: {0}  '.format(fgcol), cp(0))
                test_win.addstr(2, 32, 'BG: {0}  '.format(bgcol), cp(0))
                for i in range(1, 5):
                    test_win.addstr(3 + i, 2, teststr, cp(i))
                    test_win.addstr(3 + i, 32, teststr, cp(i + 4))
                test_win.move(1, 2 + cursor[1] * 30)
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
