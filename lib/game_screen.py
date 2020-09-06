from lib.winlayout import *
from lib.curwin import *
import os

# windows
STATS = 'stats'
MAZE = 'maze'
MESSAGES = 'messages'
ROOT = 'root'
DEBUG = 'debug'

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class Screen:
    def __init__(self, curses_scr, model):
        self.model = model
        w, h = os.get_terminal_size()
        root_layout = create_layout(Dim(h, w), 'prpg')
        row_panel = root_layout.panel(Orient.VERT, None, None)
        row_panel.window(STATS, Con(6, 40, 6, 40))

        maze_panel = row_panel.panel(Orient.HORI, None)
        maze_panel.window(MAZE, Con(25, 40, 0, 80))
        maze_panel.window(DEBUG, Con(0,30,0,50))

        row_panel.window(MESSAGES, Con(6, 40, 10, 80))

        init_win(root_layout, curses_scr)
        self.root_win = root_layout.data

        self.root_layout = root_layout
        self.rebuild_screens()
        curses.curs_set(0)

    def rebuild_screens(self):
        self.root_layout.do_layout()
        self.win(ROOT).rebuild_screens()
        self.win(ROOT).scr.refresh()

    # print messages and standard output
    def print(self, *args):
        line = ' '.join([str(a) for a in args])
        self.model.message(line)
        self.paint()

    def get_key(self):
        return self.root_win.get_key()

    def win(self, name):
        return self.root_layout.info.win_by_name[name].data

    # paint the entire screen - all that is visible
    def paint(self):
        root = self.win(ROOT)
        root.clear()

        self._paint_stats()
        self._paint_maze()
        self._paint_messages()
        self._paint_debug()

        root.refresh()

    def _paint_messages(self):
        msgwin = self.win(MESSAGES)
        msgwin.write_lines(self.model.messages[-12:])
        msgwin.scr.border()

    def _paint_debug(self):
        msgwin = self.win(DEBUG)
        msgwin.write_lines(self.model.messages[-12:])
        msgwin.scr.border()

    def _paint_stats(self):
        p = self.model.player
        statwin = self.win(STATS)
        self.root_layout.log('_paint_stats({})'.format(statwin))
        statwin.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])
        statwin.scr.border()

    def _paint_maze(self):
        mazewin = self.win(MAZE)
        model = self.model
        mazewin.write_lines(model.maze)

        for p in model.peeps:
            mazewin.move_to(p.x, p.y)
            mazewin.write_char(p.char, p.fgcolor, p.bgcolor)

        mazewin.scr.border()
        # win.move_to(x, y + len(model.maze))  # move cursor to end of maze
