#!/usr/bin/python

import curses

def get_wch(stdscr):
    while 1:
        try:
            ret = stdscr.get_wch()
            if ret != curses.KEY_RESIZE:
                return ret

        except Exception as e:
            pass        # ignore interrupts to getkey() following resize events etc.



def c_main(stdscr: 'curses._CursesWindow') -> int:
    if curses.has_colors():
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        if curses.can_change_color():
            curses.init_color(
                210,
                200,
                200,
                158 * 1000 // 0xff,
            )

        curses.init_pair(3, 210, curses.COLOR_BLUE)

    name = ''
    name_done = False
    while True:
        stdscr.addstr(0, 0, 'what is your name? ', curses.color_pair(3))
        stdscr.clrtoeol()
        stdscr.addstr(name)
        if name_done:
            stdscr.addstr(1, 0, f'Hi {name}.', curses.color_pair(3))

        char = get_wch(stdscr)
        if name_done:
            return 0

        if isinstance(char, str) and char.isprintable():
            name += char
        elif char == curses.KEY_BACKSPACE or char == '\x7f':
            name = name[:-1]
        elif char == '\n':
            name_done = True
        else:
            raise AssertionError(repr(char))


def main() -> int:
    return curses.wrapper(c_main)

if __name__ == '__main__':
    exit(main())
