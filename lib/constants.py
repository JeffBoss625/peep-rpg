# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
class Color:
    BLACK = 'BLACK'
    BLUE = 'BLUE'
    CYAN = 'CYAN'
    GREEN = 'GREEN'
    MAGENTA = 'MAGENTA'
    RED = 'RED'
    WHITE = 'WHITE'
    YELLOW = 'YELLOW'

    @staticmethod
    def curses_color(color):
        return 'COLOR_' + color


class Side:
    TOP = 'TOP'
    LEFT = 'LEFT'
    BOTTOM = 'BOTTOM'
    RIGHT = 'RIGHT'
