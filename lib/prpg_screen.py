from lib.screen_layout import *
from lib.screen import *
import time

class MazeScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)

    def do_paint(self):
        text_h = len(self.model.walls.text)
        text_w = len(self.model.walls.text[0])
        params = {**self.params, **{'text_w': text_w, 'text_h': text_h}}
        self.write_lines(self.model.walls.text, **params)

        for p in self.model.peeps:
            self.write_char(p.pos[0], p.pos[1], p.char, p.fgcolor, p.bgcolor, **params)

class TitleBarScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)

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
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            'hp:     ' + str(p.hp) + '/' + str(p.maxhp),
            # 'speed:  ' + str(p.speed),
            # 'height: ' + str(p.body.size.h)
        ])

class EquipScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            'equip',
        ])

# windows
class Win:
    TITLE_BAR = 'title_bar'
    STATS = 'stats'
    EQUIP = 'equip'
    MAZE = 'maze'
    MESSAGES = 'messages'
    MAIN = 'main'
    LOG = 'log'
    BANNER = 'banner'

class MainScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)
        w, h = self.curses.get_terminal_size()
        self.dim = Dim(h, w)

    # Handle a series of resizing calls (rubber-banding like calls as the user drags the terminal window boundary),
    # using a time interval to skip overly-rapid changes.
    # Return the final size of the terminal as a Dim() instance.
    def handle_resizing(self):
        curses = self.curses
        term_size = (self.dim.w, self.dim.h)
        if term_size == curses.get_terminal_size():
            return self.dim.copy()

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        term_size = curses.get_terminal_size()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            if term_size != curses.get_terminal_size():
                # size changed, reset timer
                term_size = curses.get_terminal_size()
                t0 = time.time()

        w, h = term_size
        curses.resizeterm(h, w)
        self.dim = Dim(h, w)
        return self.dim.copy()
        # self.log(f'size_to_terminal: screen "{self.name}" updated to {self.dim}')



# An abstraction of a terminal game screen with controls to refresh and update what is shown
class PrpgControl:
    def __init__(self, root_layout, model):
        self.root_layout = root_layout
        self.main_screen = root_layout.data
        self.model = model

        main_panel = root_layout.panel('main_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(Win.TITLE_BAR, Con(3, 40, 3, 0), wintype=TitleBarScreen)

        # Center Row
        maze_h = len(model.maze.walls.text) + 2
        maze_w = len(model.maze.walls.text[0]) + 2
        banner_h = 4
        center = main_panel.panel('center_panel', Orient.HORI, None)

        center_col1 = center.panel('center_col1', Orient.VERT, None)
        center_col1.window(Win.STATS, Con(10,30,10,30), wintype=StatsScreen)
        center_col1.window(Win.EQUIP, Con(20,30,0,30), wintype=EquipScreen)

        center_col2 = center.panel('center_col2', Orient.VERT, None)
        center_col2.window(Win.BANNER, Con(banner_h, maze_w,  banner_h, 60), wintype=TextScreen, trunc_y=SIDE.TOP)
        center_col2.window(Win.MAZE, Con(maze_h,      maze_w,  30,      60), wintype=MazeScreen, align_x=SIDE.CENTER, align_y=SIDE.CENTER)

        center.window(Win.MESSAGES, Con(6,           maze_w,  30+banner_h, 0), wintype=TextScreen, trunc_y=SIDE.TOP)

        # Bottom Row
        main_panel.window(Win.LOG, Con(4,30), wintype=TextScreen, trunc_y=SIDE.TOP)

        root_layout.size_to_terminal()           # reset layouts to current terminal size and builds curses windows
        self.connect_models(self.main_screen, self.model)

        def log_event_fn(m, msg, **kwds):
            name = getattr(m, '"name" ', '')
            model.log_model.print(f'{msg}: {m.__class__.__name__} {name}{kwds}')

        model.maze.subscribe(log_event_fn)

    @staticmethod
    def connect_models(main_screen, model):
        by_name = main_screen.info.win_by_name
        by_name[Win.MESSAGES].model = model.message_model
        by_name[Win.LOG].model = model.log_model
        by_name[Win.MAZE].model = model.maze
        by_name[Win.TITLE_BAR].model = model.maze
        by_name[Win.BANNER].model = model.banner_model
        by_name[Win.STATS].model = model.maze
        by_name[Win.EQUIP].model = model.equip

    def get_key(self):
        self.root_layout.data.paint()
        return self.root_layout.data.get_key()

# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     screen = PrpgScreen(None, model)
