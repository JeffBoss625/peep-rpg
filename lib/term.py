import curses as curselib
from lib.constants import Color

# Term simplifies the interface with curses terminal. It narrows usage to only what is needed
class Term:
    def __init__(self, scr):
        self.scr = scr
        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair

    def clear(self):
        self.scr.clear()

    def refresh(self):
        self.scr.refresh()

    def get_key(self):
        return self.scr.getkey()

    def get_xy(self):
        y, x = self.scr.getyx()
        return x, y

    # Relative move of cursor
    def move(self, dx, dy):
        y, x = self.scr.getyx()
        self.scr.move(y + dy, x + dx)

    # Absolute move of cursor
    def move_to(self, x, y):
        self.scr.move(y, x)


    def write_char(self, char, fg=Color.WHITE, bg=Color.BLACK):
        cpair = self.color_pair(fg, bg)
        self.scr.addstr(char, cpair)

    def color_pair(self, fg, bg):
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            fgc = getattr(curselib, 'COLOR_' + fg.name)
            bgc = getattr(curselib, 'COLOR_' + bg.name)
            curselib.init_pair(self.color_pair_count, fgc, bgc)
            self.color_pairs[key] = curselib.color_pair(self.color_pair_count)

        return self.color_pairs[key]

