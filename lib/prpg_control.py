from lib.constants import Key
from lib.prpg_window import *
from lib.win_layout import Con, Orient


class WIN:
    TITLE = 'title'
    STATS = 'stats'
    EQUIP = 'equip'
    MAZE = 'maze'
    MESSAGES = 'messages'
    ROOT = 'root'
    LOG = 'log'
    BANNER = 'banner'

#
class PrpgControl:
    def __init__(self, root_layout, model):
        self.root_layout = root_layout
        self.model = model

        main_panel = root_layout.panel('root_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(WIN.TITLE, Con(40,3,0,3))

        # Center Row
        maze_h = len(model.maze.walls.text) + 2
        maze_w = len(model.maze.walls.text[0]) + 2
        banner_h = 4
        center = main_panel.panel('center_panel', Orient.HORI, None)

        center_col1 = center.panel('center_col1', Orient.VERT, None)
        center_col1.window(WIN.STATS, Con(30,10,30,10))
        center_col1.window(WIN.EQUIP, Con(30,20,30,0))

        center_col2 = center.panel('center_col2', Orient.VERT, None)
        center_col2.window(WIN.BANNER, Con(maze_w,banner_h,60,banner_h))
        center_col2.window(WIN.MAZE, Con(maze_w,maze_h,60,0))

        center.window(WIN.MESSAGES, Con(maze_w,6,0,0))

        # Bottom Row
        main_panel.window(WIN.LOG, Con(30,4))

        init_windows(root_layout, model)
        self.root_win = root_layout.window

        root_layout.do_layout()           # reset layouts to current terminal size and builds curses windows

        def log_event_fn(m, msg, **kwds):
            name = getattr(m, '"name" ', '')
            model.log_model.print(f'{msg}: {m.__class__.__name__} {name}{kwds}')

        # model.maze.subscribe(log_event_fn)
        self.root_win.curses.raw()
        self.root_win.curses.curs_set(0)

    def get_key(self):
        self.root_layout.window.paint()
        return self.root_layout.window.get_key()

    def player_died(self):
        self.model.banner('  YOU DIED! (press "q" to exit)')
        while self.get_key() not in ('q', Key.CTRL_Q):
            pass

    def resize_handler(self, _signum, _frame):
        try:
            if self.root_layout.handle_resizing():
                self.root_win.paint(force=True)

        except Exception as e:
            self.root_layout.log(e)



def init_windows(root_layout, model):
    def win(name):
        return root_layout.info.comp_by_name[name]

    # custom windows
    win(WIN.TITLE).initwin(TitleWindow, model=model.title, trunc_y=SIDE.TOP)
    win(WIN.STATS).initwin(StatsWindow, model=model.maze)
    win(WIN.EQUIP).initwin(EquipWindow, model=model.equip)
    win(WIN.MAZE).initwin(MazeWindow, model=model.maze, align_x=SIDE.CENTER, align_y=SIDE.CENTER)

    # standard windows
    win(WIN.BANNER).initwin(TextWindow, model=model.banner_model, trunc_y=SIDE.TOP)
    win(WIN.MESSAGES).initwin(TextWindow, model=model.message_model, trunc_y=SIDE.TOP)
    win(WIN.LOG).initwin(TextWindow, model=model.log_model, trunc_y=SIDE.TOP)

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     win = PrpgWindow(None, model)
