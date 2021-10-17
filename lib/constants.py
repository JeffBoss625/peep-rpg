# Text attribute flags from _curses.py
# Copied here to prevent application from direct curses linkage (debug/dummy mode etc)
class TEXTA:
    # ALTCHARSET = 4194304
    # ATTRIBUTES = 4294967040
    # BLINK = 524288
    BOLD = 2097152
    # CHARTEXT = 255
    # COLOR = 65280
    DIM = 1048576
    # HORIZONTAL = 33554432
    INVIS = 8388608
    # LEFT = 67108864
    # LOW = 134217728
    # NORMAL = 0
    # PROTECT = 16777216
    REVERSE = 262144
    # RIGHT = 268435456
    # STANDOUT = 65536
    # TOP = 536870912
    UNDERLINE = 131072
    # VERTICAL = 1073741824

# Color constants matching available curses colors (facilitates configuration settings with simple case)
class COLOR:
    BLACK = 'black'
    BLUE = 'blue'
    CYAN = 'cyan'
    GREEN = 'green'
    MAGENTA = 'magenta'
    RED = 'red'
    WHITE = 'white'
    YELLOW = 'yellow'

class ASCII_CHARS:
    MONEY = '$'
    SWORD = '|'
    BOW = '{'
    ARROW = '-'
    FIRE = '*'
    SHIELD = '0'
    BOOT = '='
    GAUNTLETS = '"'
    CHESTPLATE = '+'
    STAIR_UP = '<'
    STAIR_DOWN = '>'

class FANCY_CHARS:
    MONEY = '¢'
    SWORD = '|'
    BOW = '{'
    ARROW = '→'
    FIRE = '☼'
    SHIELD = 'Θ'
    BOOT = '╚'
    GAUNTLETS = ''
    CHESTPLATE = ''
    STAIR_UP = '<'
    STAIR_DOWN = '>'

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
    # ESC = '\x1b'

class GAME_SETTINGS:
    REGEN_RATE =        0.01   # Normal % heal per turn
    BASE_EXP_TO_LEVEL = 100.00   # base xp is 100 to level 2
    LEVEL_UP_FACTOR =     2.00   # Altered by other factors
    BASE_KILL_EXP =     1.00   # basic experience for killing a monster (before modifications)
    CHARS = ASCII_CHARS
