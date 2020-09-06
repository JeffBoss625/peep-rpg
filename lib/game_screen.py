from lib.term import Term
from lib.winlayout import *
from lib.curwin import *
import os

# windows
STATS = 'stats'
MAZE = 'maze'
MESSAGES = 'messages'

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class Screen:
    def __init__(self, curses_scr, model):
        self.term = Term(curses_scr)
        self.model = model
        w, h = os.terminal_size
        root = rootwin(Dim(h, w), 'prpg')
        hpan = root.panel(Orient.HORI)
        hpan.window(STATS, Con(8, 20, 8, 20))
        hpan.window(MAZE, Con(40, 40))
        hpan.window(MESSAGES, Con(8,20))
        root.data = CurWin(root, curses_scr)

        self.root = root
        self.reset_layout()

    def reset_layout(self):
        self.root.do_layout()
        self.root.data.create_child_screens()

    # print messages and standard output
    def print(self, *args):
        line = ' '.join([str(a) for a in args])
        self.model.message(line)
        self.paint()

    def get_key(self):
        return self.term.get_key()

    # paint the entire screen - all that is visible
    def paint(self):
        term = self.term
        term.clear()

        self._paint_stats()
        self._paint_maze()
        self._paint_messages()

        term.move_to(0,0)
        term.refresh()

    def _paint_messages(self):
        win = self.root[MESSAGES].data
        win.write_lines(self.model.messages[-12:])

    def _paint_stats(self):
        p = self.model.player
        self._term.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])

    def _paint_maze(self):
        term = self._term
        model = self.model
        x, y = term.get_xy()

        term.write_lines(model.maze)

        for p in model.peeps:
            term.move_to(x + p.x, y + p.y)
            term.write_char(p.char,  p.fgcolor, p.bgcolor)

        term.move_to(x, y + len(model.maze))  # move cursor to end of maze
