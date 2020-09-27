from lib.screen_layout import *
from lib.screen import *

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class PrpgScreen:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.term_size = None

        main_panel = root.panel('main_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(Win.STATS, Con(6, 40, 6, 0), wintype=PlayerStatsScreen)

        # Center Row
        maze_h = len(model.maze.walls.text) + 2
        maze_w = len(model.maze.walls.text[0]) + 2
        banner_h = 4
        center = main_panel.panel('center_panel', Orient.HORI, None)
        left_center = center.panel('leftcenter_panel', Orient.VERT, None)

        left_center.window(Win.BANNER, Con(banner_h, maze_w,  banner_h,    60), wintype=TextScreen, trunc_y=Side.TOP)
        left_center.window(Win.MAZE, Con(maze_h,      maze_w,  30,             60), wintype=MazeScreen, align_x=Side.CENTER, align_y = Side.CENTER)

        center.window(Win.MESSAGES, Con(6,           maze_w,  30+banner_h, 0), wintype=TextScreen, trunc_y=Side.TOP)

        # Bottom Row
        main_panel.window(Win.LOG, Con(4,30), wintype=TextScreen, trunc_y=Side.TOP)

        root.do_layout()
        sync_delegates(root)
        root.data.rebuild_screens()
        root.data.model = model

        def log_event_fn(m, msg, **kwds):
            name = getattr(m, '"name" ', '')
            model.log_model.print(f'{msg}: {m.__class__.__name__} {name}{kwds}')

        model.maze.subscribe(log_event_fn)

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

        win.rebuild_screens()

    def get_key(self):
        return self.root.data.get_key()

    # paint the entire screen - all that is visible
    def paint(self, force=False):
        self.root.data.paint(force=force)

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
