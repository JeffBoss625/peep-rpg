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

    def write_lines(self, lines):
        scr = self.scr
        y, x = scr.getyx()
        for i, line in enumerate(lines):
            scr.move(y+i, x)
            scr.addstr(line)

        scr.move(y + len(lines), x)

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

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class Screen:
    def __init__(self, curses_scr, model):
        self._term = Term(curses_scr)
        self.model = model
        self.model.out = self  # allow the model itself to be used for term printed output

    # print messages and standard output
    def print(self, *args):
        line = ' '.join([str(a) for a in args])
        self.model.message(line)
        self.repaint()

    def get_key(self):
        return self._term.get_key()

    # repaint the entire screen - all that is visible
    def repaint(self):
        term = self._term
        model = self.model
        x_margin = 3
        y_margin = 3
        term.clear()

        term.move_to(x_margin, y_margin)
        self._draw_stats()

        term.move(0, y_margin)
        self._draw_maze_area()

        term.move(0, y_margin)
        term.move_to(len(model.maze[0]) + x_margin * 2, y_margin)
        term.write_lines(model.messages[-12:])

        term.move_to(0, 0)
        term.refresh()

    def _draw_stats(self):
        p = self.model.player
        self._term.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])

    def _draw_maze_area(self):
        term = self._term
        model = self.model
        x, y = term.get_xy()

        term.write_lines(model.maze)

        for p in model.peeps:
            term.move_to(x + p.x, y + p.y)
            term.write_char(p.char,  p.fgcolor, p.bgcolor)

        term.move_to(x, y + len(model.maze))  # move cursor to end of maze
