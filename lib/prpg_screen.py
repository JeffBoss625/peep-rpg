from lib.screen_layout import *
from lib.screen import *

# windows
STATS = 'stats'
MAZE = 'maze'
MESSAGES = 'messages'
ROOT = 'root'
LOG = 'log'
BILLBOARD = 'billboard'

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class PrpgScreen:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.term_size = None

        main_panel = root.panel('main_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(STATS, Con(6,40,6,0), wintype=WIN.STATS)

        # Center Row
        center = main_panel.panel('center_panel', Orient.HORI, None)
        left_center = center.panel('leftcenter_panel', Orient.VERT, None)
        left_center.window(BILLBOARD,   Con(4,30,4,40), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)
        left_center.window(MAZE,        Con(25,30,30,40), wintype=WIN.MAZE)
        center.window(MESSAGES,         Con(6,40,34,0), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)

        # Bottom Row
        main_panel.window(LOG, Con(4,30), wintype=WIN.TEXT, trunc_y=Side.BOTTOM)
        root.do_layout()
        sync_delegates(root)
        self.connect_models()
        root.data.rebuild_screens()
        root.data.curses.curs_set(0)

    def connect_models(self):
        # connect models to screens
        self.win(MESSAGES).model = self.model.message_model
        self.win(LOG).model = self.model.log_model
        self.win(MAZE).model = self.model.maze
        self.win(STATS).model = self.model.peeps
        self.win(ROOT).model = self.model
        self.win(BILLBOARD).model = self.model.billboard

    def size_to_terminal(self):
        win = self.root.data
        w, h = win.size_to_terminal()
        self.root.dim = Dim(h,w)
        self.root.con = Con(h,w,h,w)
        self.root.clear_layout()
        self.root.do_layout()
        sync_delegates(self.root)
        self.root.data.rebuild_screens()

    def get_key(self):
        return self.win(ROOT).get_key()

    def win(self, name):
        return self.root.info.comp_by_name[name].data

    # paint the entire screen - all that is visible
    def paint(self):
        self.win(ROOT).clear()
        self.win(ROOT).paint()
        self.win(STATS).paint()
        self.win(MAZE).paint()
        self.win(MESSAGES).paint()
        self.win(LOG).paint()
        self.win(BILLBOARD).paint()

        self.root.data.curses.doupdate()

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
