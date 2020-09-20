from lib.screen_layout import *
from lib.screen import *
import time
import traceback

# windows
STATS = 'stats'
MAZE = 'maze'
MESSAGES = 'messages'
ROOT = 'root'
LOG = 'log'
BILLBOARD = 'billboard'

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class PrpgScreen:
    def __init__(self, root, curses, model):
        self.root = root
        self.curses = curses
        self.model = model

        main_panel = root.panel('main_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(STATS, Con(6, 40), wintype=WIN.STATS)

        # Center Row
        center = main_panel.panel('center_panel', Orient.HORI, None)
        left_center = center.panel('leftcenter_panel', Orient.VERT, None)
        left_center.window(BILLBOARD, Con(4,0,4,0), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)
        left_center.window(MAZE, Con(25, 20), wintype=WIN.MAZE)
        center.window(MESSAGES, Con(6, 40), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)

        # Bottom Row
        main_panel.window(LOG, Con(4, 30), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)

        root.do_layout()
        init_delegates(root, curses)
        self.connect_models()
        root.data.rebuild_screens()
        curses.curs_set(0)

    def connect_models(self):
        # connect models to screens
        self.win(MESSAGES).model = self.model.message_model
        self.win(LOG).model = self.model.log_model
        self.win(MAZE).model = self.model.maze
        self.win(STATS).model = self.model.peeps
        self.win(ROOT).model = self.model
        self.win(BILLBOARD).model = self.model.billboard

    def size_to_terminal(self):
        if self.term_size == self.curses.get_terminal_size():
            return

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        self.term_size = self.curses.get_terminal_size()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            if self.term_size != self.curses.get_terminal_size():
                # size changed, reset timer
                self.term_size = self.curses.get_terminal_size()
                t0 = time.time()

        try:
            w, h = self.term_size
            self.curses.resizeterm(h, w)
            self.root.dim.w = w
            self.root.dim.h = h
            self.root.clear_layout()
            self.root.do_layout()
            self.root.data.rebuild_screens()

        except Exception as e:
            self.root.log('resize failed: ' + str(e) + ''.join(traceback.format_tb(e.__traceback__)))

    def get_key(self):
        return self.win(ROOT).get_key()

    def win(self, name):
        return self.root.info.win_by_name[name].data

    # paint the entire screen - all that is visible
    def paint(self):
        self.win(ROOT).clear()
        self.win(ROOT).paint()
        self.win(STATS).paint()
        self.win(MAZE).paint()
        self.win(MESSAGES).paint()
        self.win(LOG).paint()
        self.win(BILLBOARD).paint()

        self.curses.doupdate()

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
