from enum import Enum

# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
class Color(Enum):
    BLACK = 0,
    BLUE = 1,
    CYAN = 2,
    GREEN = 3,
    MAGENTA = 4,
    RED = 5,
    WHITE = 6,
    YELLOW = 7,
