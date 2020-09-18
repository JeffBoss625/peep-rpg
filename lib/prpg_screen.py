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
    def __init__(self, curses_scr, curses, model):
        self.model = model
        self.curses = curses

        # Setup Main Panel
        w, h = self.term_size = curses.get_terminal_size()
        self.root_layout = layout = create_layout(Dim(h, w), 'prpg')
        main_panel = layout.panel(Orient.VERT, None, None)

        # Top Row
        main_panel.window(STATS, Con(6, 40, 6, 40), wintype=WIN.STATS)

        # Center Row
        center = main_panel.panel(Orient.HORI, None)
        left_center = center.panel(Orient.VERT, None)
        left_center.window(BILLBOARD, Con(0,4,0,4), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)
        left_center.window(MAZE, Con(25, 30, 0, 60), wintype=WIN.MAZE)
        center.window(MESSAGES, Con(6, 40), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)

        # Bottom Row
        main_panel.window(LOG, Con(0, 30), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)
        self.root_layout.do_layout()

        create_win_data(layout, curses_scr, curses)
        self.connect_models()

        self.win(ROOT).rebuild_screens()
        curses.curs_set(0)

    def connect_models(self):
        # connect models to screens
        self.win(MESSAGES).model = self.model.message_model
        self.win(LOG).model = self.model.log_model
        self.win(MAZE).model = self.model.maze
        self.win(STATS).model = self.model.peeps
        self.win(ROOT).model = self.model

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
            self.root_layout.dim.w = w
            self.root_layout.dim.h = h
            self.root_layout.clear_layout()
            self.root_layout.do_layout()
            self.root_layout.data.rebuild_screens()

        except Exception as e:
            self.root_layout.log('resize failed: ' + str(e) + ''.join(traceback.format_tb(e.__traceback__)))

    def get_key(self):
        return self.win(ROOT).get_key()

    def win(self, name):
        return self.root_layout.info.win_by_name[name].data

    # paint the entire screen - all that is visible
    def paint(self):
        self.win(ROOT).clear()
        self.win(STATS).paint()
        self.win(MAZE).paint()
        self.win(MESSAGES).paint()
        self.win(LOG).paint()

        self.win(ROOT).paint()

        self.curses.doupdate()

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
