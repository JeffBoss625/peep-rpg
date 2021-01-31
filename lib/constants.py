# Color constants correspond to curses lib basic colors of the same name pattern (name is used for lookup in curses)
#
#    curses.COLOR_BLACK
#    curses.COLOR_BLUE
#    etc...
#
class COLOR:
    BLACK = 'black'
    BLUE = 'blue'
    CYAN = 'cyan'
    GREEN = 'green'
    MAGENTA = 'magenta'
    RED = 'red'
    WHITE = 'white'
    YELLOW = 'yellow'


def curses_color(color):
    return 'COLOR_' + color.upper()


class SIDE:
    TOP = 'TOP'
    LEFT = 'LEFT'
    BOTTOM = 'BOTTOM'
    RIGHT = 'RIGHT'
    CENTER = 'CENTER'

class FACING:
    FRONT = 'FRONT'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'
    BACK = 'BACK'

class Key:
    CTRL_Q = '\x11'

class GAME_SETTINGS:
    REGEN_RATE =        0.01   # Normal % heal per turn
    BASEEXPTOLEVEL =    2.00   # base xp is 100 to level 2
    LEVELUPFACTOR =     2.00   # Altered by other factors
    BASE_KILL_EXP =     1.00   # basic experience for killing a monster (before modifications)
