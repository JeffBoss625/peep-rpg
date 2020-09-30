# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
from dataclasses import dataclass

from lib.util import DotDict

COLOR = DotDict(
    BLACK='BLACK',
    BLUE='BLUE',
    CYAN='CYAN',
    GREEN='GREEN',
    MAGENTA='MAGENTA',
    RED='RED',
    WHITE='WHITE',
    YELLOW='YELLOW',
)


def curses_color(color):
    return 'COLOR_' + color


SIDE = DotDict(
    TOP='TOP',
    LEFT='LEFT',
    BOTTOM='BOTTOM',
    RIGHT='RIGHT',
    CENTER='CENTER',
)

class Key:
    CTRL_Q = '\x11'


if __name__ == '__main__':
    print(COLOR.values())
