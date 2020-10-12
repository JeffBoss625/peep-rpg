from lib.screen_layout import *
from lib.screen import *

class MazeScreen(Screen):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        text_h = len(self.model.walls.text)
        text_w = len(self.model.walls.text[0])
        params = {**self.params, **{'text_w': text_w, 'text_h': text_h}}
        self.write_lines(self.model.walls.text, **params)

        for p in self.model.peeps:
            self.write_char(p.pos[0], p.pos[1], p.char, p.fgcolor, p.bgcolor, **params)

class TitleScreen(Screen):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            # class
            # level
            # height
            # age
        ])

class StatsScreen(Screen):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            'hp:     ' + str(p.hp) + '/' + str(p.maxhp),
            # 'speed:  ' + str(p.speed),
            # 'height: ' + str(p.body.size.h)
        ])

class EquipScreen(Screen):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            'equip',
        ])

# windows
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
        main_panel.window(WIN.TITLE, Con(3, 40, 3, 0))

        # Center Row
        maze_h = len(model.maze.walls.text) + 2
        maze_w = len(model.maze.walls.text[0]) + 2
        banner_h = 4
        center = main_panel.panel('center_panel', Orient.HORI, None)

        center_col1 = center.panel('center_col1', Orient.VERT, None)
        center_col1.window(WIN.STATS, Con(10, 30, 10, 30))
        center_col1.window(WIN.EQUIP, Con(20, 30, 0, 30))

        center_col2 = center.panel('center_col2', Orient.VERT, None)
        center_col2.window(WIN.BANNER, Con(banner_h, maze_w, banner_h, 60))
        center_col2.window(WIN.MAZE, Con(maze_h, maze_w, 0, 60))

        center.window(WIN.MESSAGES, Con(6, maze_w, 0, 0))

        # Bottom Row
        main_panel.window(WIN.LOG, Con(4, 30))

        init_windows(root_layout, model)
        self.main_screen = root_layout.window

        root_layout.do_layout()           # reset layouts to current terminal size and builds curses windows

        def log_event_fn(m, msg, **kwds):
            name = getattr(m, '"name" ', '')
            model.log_model.print(f'{msg}: {m.__class__.__name__} {name}{kwds}')

        model.maze.subscribe(log_event_fn)
        self.main_screen.curses.raw()
        self.main_screen.curses.curs_set(0)

    def get_key(self):
        self.root_layout.window.paint()
        return self.root_layout.window.get_key()

    def resize_handler(self, _signum, _frame):
        try:
            if self.root_layout.handle_resizing():
                self.main_screen.paint(force=True)

        except Exception as e:
            self.root_layout.log(e)



def init_windows(root_layout, model):
    def win(name):
        return root_layout.info.comp_by_name[name]

    # custom windows
    win(WIN.TITLE).initwin(TitleScreen, model=model.title, trunc_y=SIDE.TOP)
    win(WIN.STATS).initwin(StatsScreen, model=model.maze)
    win(WIN.EQUIP).initwin(EquipScreen, model=model.equip)
    win(WIN.MAZE).initwin( MazeScreen,  model=model.maze, align_x=SIDE.CENTER, align_y=SIDE.CENTER)

    # standard windows
    win(WIN.BANNER).initwin(  TextScreen, model=model.banner_model, trunc_y=SIDE.TOP)
    win(WIN.MESSAGES).initwin(TextScreen, model=model.message_model, trunc_y=SIDE.TOP)
    win(WIN.LOG).initwin(     TextScreen, model=model.log_model, trunc_y=SIDE.TOP)

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
