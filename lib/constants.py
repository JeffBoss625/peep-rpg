# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
class COLOR:
    BLACK = 'BLACK'
    BLUE = 'BLUE'
    CYAN = 'CYAN'
    GREEN = 'GREEN'
    MAGENTA = 'MAGENTA'
    RED = 'RED'
    WHITE = 'WHITE'
    YELLOW = 'YELLOW'


def curses_color(color):
    return 'COLOR_' + color


class SIDE:
    TOP='TOP'
    LEFT='LEFT'
    BOTTOM='BOTTOM'
    RIGHT='RIGHT'
    CENTER='CENTER'


class Key:
    CTRL_Q = '\x11'


