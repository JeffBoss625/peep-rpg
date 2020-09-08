from lib.screen_layout import *
from lib.screen import *
import os
import time
import traceback

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
        w, h = self.term_size = os.get_terminal_size()
        layout = create_layout(Dim(h, w), 'prpg')
        row_panel = layout.panel(Orient.VERT, None, None)
        row_panel.window(STATS, Con(6, 40, 6, 40))

        maze_panel = row_panel.panel(Orient.HORI, None)
        maze_panel.window(MAZE, Con(25, 40, 0, 80))
        maze_panel.window(DEBUG, Con(0,30,0,50))

        row_panel.window(MESSAGES, Con(6, 40, 10, 80))

        init_screens(layout, curses_scr)
        self.root_win = layout.data

        self.root_layout = layout
        self.rebuild_screens()
        curses.curs_set(0)

    def rebuild_screens(self):
        self.root_layout.do_layout()
        self.win(ROOT).rebuild_screens()
        self.win(ROOT).scr.refresh()

    def size_to_terminal(self):
        if self.term_size == os.get_terminal_size():
            return

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        self.term_size = os.get_terminal_size()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            if self.term_size != os.get_terminal_size():
                # size changed, reset timer
                self.term_size = os.get_terminal_size()
                t0 = time.time()

        try:
            w, h = self.term_size
            curses.resizeterm(h, w)
            self.root_layout.dim.w = w
            self.root_layout.dim.h = h
            self.root_layout.clear_layout()
            self.root_layout.do_layout()
            self.rebuild_screens()

        except Exception as e:
            self.root_layout.log('resize failed: ' + str(e) + ''.join(traceback.format_tb(e.__traceback__)))

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
        if not msgwin.scr:
            return
        msgwin.write_lines(self.model.messages[-12:])
        msgwin.scr.border()

    def _paint_debug(self):
        dbgwin = self.win(DEBUG)
        if not dbgwin.scr:
            return
        dbgwin.write_lines(self.model.out[-12:])
        dbgwin.scr.border()

    def _paint_stats(self):
        p = self.model.player
        statwin = self.win(STATS)
        if not statwin.scr:
            return
        statwin.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])
        statwin.scr.border()

    def _paint_maze(self):
        mazewin = self.win(MAZE)
        if not mazewin.scr:
            return
        model = self.model
        mazewin.write_lines(model.maze)

        for p in model.peeps:
            mazewin.write_char(p.x, p.y, p.char, p.fgcolor, p.bgcolor)

        mazewin.scr.border()
        # win.move_to(x, y + len(model.maze))  # move cursor to end of maze
