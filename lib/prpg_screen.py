from lib.screen_layout import *
from lib.screen import *

# windows
STATS = 'stats'
MAZE = 'maze'
MESSAGES = 'messages'
MAIN = 'main'
LOG = 'log'
BANNER = 'banner'

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
        maze_h = len(model.maze.walls.text) + 2
        maze_w = len(model.maze.walls.text[0]) + 2
        banner_h = 4
        center = main_panel.panel('center_panel', Orient.HORI, None)
        left_center = center.panel('leftcenter_panel', Orient.VERT, None)

        left_center.window(BANNER,   Con(banner_h, maze_w,  banner_h,    60),    wintype=WIN.TEXT, trunc_y=Side.TOP)
        left_center.window(MAZE,        Con(maze_h,      maze_w,  30,             60),    wintype=WIN.MAZE, align_x=Side.CENTER, align_y = Side.CENTER)

        center.window(MESSAGES,         Con(6,           maze_w,  30+banner_h, 0),     wintype=WIN.TEXT, trunc_y=Side.TOP)

        # Bottom Row
        main_panel.window(LOG, Con(4,30), wintype=WIN.TEXT, trunc_y=Side.TOP)
        root.do_layout()
        sync_delegates(root)
        self.connect_models()
        root.data.rebuild_screens()

    def connect_models(self):
        # connect models to screens
        self.win(MESSAGES).model = self.model.message_model
        self.win(LOG).model = self.model.log_model
        self.win(MAZE).model = self.model.maze
        self.win(STATS).model = self.model.maze
        self.win(MAIN).model = self.model
        self.win(BANNER).model = self.model.banner

        log = self.win(LOG).model

        def log_event_fn(model, msg, **kwds):
            name = getattr(model, '"name" ', '')
            log.print(f'{msg}: {model.__class__.__name__} {name}{kwds}')

        self.win(MAZE).model.subscribe(log_event_fn)

    def size_to_terminal(self):
        win = self.root.data
        win.size_to_terminal()
        h = win.dim.h
        w = win.dim.w
        self.root.dim = Dim(h,w)
        self.root.con = Con(h,w,h,w)
        self.root.clear_layout()
        self.root.do_layout()
        sync_delegates(self.root)
        self.root.data.rebuild_screens()

    def get_key(self):
        return self.win(MAIN).get_key()

    def win(self, name):
        return self.root.info.comp_by_name[name].data

    # paint the entire screen - all that is visible
    def paint(self, force=False):
        self.win(MAIN).paint(force=force)

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
