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
LOG = 'log'

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class PrpgScreen:
    def __init__(self, curses_scr, model):
        self.model = model
        w, h = self.term_size = os.get_terminal_size()
        layout = create_layout(Dim(h, w), 'prpg')
        row_panel = layout.panel(Orient.VERT, None, None)
        row_panel.window(STATS, Con(6, 40, 6, 40))

        maze_panel = row_panel.panel(Orient.HORI, None)
        maze_panel.window(MAZE, Con(25, 40, 0, 80))
        maze_panel.window(LOG, Con(0, 30, 0, 50))

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

    def get_key(self):
        return self.root_win.get_key()

    def win(self, name):
        return self.root_layout.info.win_by_name[name].data

    def clear(self):
        self.win(ROOT).clear()

    # paint the entire screen - all that is visible
    def paint(self):
        self.win(ROOT).clear()
        self._paint_stats()
        self._paint_maze()
        self._paint_messages()
        self._paint_log()

        self.win(ROOT).refresh()

    def _paint_messages(self):
        win = self.win(MESSAGES)
        if not win.scr:
            return
        win.write_lines(self.model.messages[-12:])
        win.scr.border()

    def _paint_log(self):
        win = self.win(LOG)
        if not win.scr:
            return
        win.write_lines(self.model.log_output[-12:])
        win.scr.border()

    def _paint_stats(self):
        p = self.model.player
        win = self.win(STATS)
        if not win.scr:
            return
        win.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])
        win.scr.border()

    def _paint_maze(self):
        win = self.win(MAZE)
        if not win.scr:
            return
        model = self.model
        win.write_lines(model.maze)

        for p in model.peeps:
            win.write_char(p.x, p.y, p.char, p.fgcolor, p.bgcolor)

        win.scr.border()