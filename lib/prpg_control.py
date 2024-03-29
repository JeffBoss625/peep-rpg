from lib.constants import Key
from lib.prpg_window import *
from lib.win_layout import Con, Orient


class WIN:
    TITLE = 'title'
    STATS = 'stats'
    PLAYER = 'player'
    EQUIP = 'equip'
    MAZE = 'maze'
    MESSAGES = 'messages'
    ROOT = 'root'
    BANNER = 'banner'

#
class PrpgControl:
    def __init__(self, root_layout, game, pack=False):
        self.root_layout = root_layout
        self.game_model = game

        main_panel = root_layout.panel('root_panel', Orient.VERT, None, None)

        # Top Row
        main_panel.window(WIN.TITLE, Con(40,3,0,3))

        # Center Row
        center = main_panel.panel('center_panel', Orient.HORI, None)

        center_col1 = center.panel('center_col1', Orient.VERT, None)
        hmin = 7 if pack else 12
        hmax = hmin
        center_col1.window(WIN.PLAYER, Con(30,hmin,30,hmax))
        hmin = 10 if pack else 20
        hmax = hmin if pack else 0
        center_col1.window(WIN.STATS, Con(30,hmin,30,hmax))

        maze_h = len(game.maze_model.walls.text) + 2
        maze_w = len(game.maze_model.walls.text[0]) + 2

        banner_h = 4
        center_col2 = center.panel('center_col2', Orient.VERT, None)
        center_col2.window(WIN.BANNER, Con(maze_w,banner_h,0,banner_h))
        hmin = maze_h
        hmax = hmin if pack else 0
        center_col2.window(WIN.MAZE, Con(maze_w,hmin,0,hmax))

        hmin = 6
        hmax = hmin if pack else 0
        center.window(WIN.EQUIP, Con(10,6,0,hmax))

        # Bottom Row
        main_panel.window(WIN.MESSAGES, Con(30,6))

        init_windows(root_layout)
        self.set_model(game)
        self.root_win = root_layout.window

        root_layout.do_layout()           # reset layouts to current terminal size and builds curses windows

        def log_event_fn(m, msg, **kwds):
            name = getattr(m, '"name" ', '')
            game.log_model.print(f'{msg}: {m.__class__.__name__} {name}{kwds}')

        # model.maze_model.subscribe(log_event_fn)
        self.root_win.curses.raw()
        self.root_win.curses.curs_set(0)

        self.input_override = {}        # plug-in functions to execute for specific key events (for testing)

    def _win(self, name):
        return self.root_layout.info.comp_by_name[name].window

    def set_model(self, game):
        self._win(WIN.BANNER).set_model(game.banner_model)
        self._win(WIN.MESSAGES).set_model(game.message_model)
        self._win(WIN.STATS).set_model(game)
        self._win(WIN.PLAYER).set_model(game)
        self._win(WIN.TITLE).set_model(game.player)
        self._win(WIN.EQUIP).set_model(game)
        self._win(WIN.MAZE).set_model(game.maze_model)

        def handle_game_update(model, _etype, **kargs):
            if model == game and kargs.get('key', '') == 'maze_model':
                self._win(WIN.MAZE).set_model(kargs['new'])

        game.subscribe(handle_game_update)

        self.game_model = game

    def win(self, name):
        return self.root_layout.info.comp_by_name[name]

    def get_ch(self):
        self.root_layout.window.paint()
        return self.root_layout.window.get_ch()

    def get_key(self):
        self.root_layout.window.paint()
        return self.root_layout.window.get_key()
        # return self.win(WIN.MAZE).window.get_key()

    def player_died(self):
        self.game_model.banner('  YOU DIED! (press "q" to exit)')
        while self.get_key() not in ('q', Key.CTRL_Q):
            pass

    def resize_handler(self, _signum, _frame):
        try:
            if self.root_layout.handle_resizing():
                self.root_win.paint(force=True)

        except Exception as e:
            self.root_layout.log(e)

    def choose_item(self, msg, items):
        idx_line = tuple((index, f'{item.name}') for index, item in enumerate(items))
        idx = self.show_lines(msg, idx_line, True)
        if idx == -1:
            return None
        return items[idx]

    def show_lines(self, msg, lines, choose):
        lmarg = '  '
        rmarg = '  '
        textblock = ['', lmarg + msg + rmarg]
        justlen = max(len(line) for line in lines)
        for index, line in lines:
            s = lmarg + f' {chr(index + 97)}) {line.rjust(justlen)}' + rmarg
            textblock.append(s)
        textblock.append('')
        maxw = max((len(line) for line in textblock))
        textblock = (line.ljust(maxw) for line in textblock)
        self.game_model.maze_model.overlay.replace(textblock)
        if choose:
            ret = self.choose_line(msg, lines, textblock)
            return ret

    def choose_line(self, msg, lines, textblock):
        ret = -1
        while ret < 0 or ret > len(lines)-1:
            key_in = self.get_key()
            if ord(key_in) == 27:
                ret = -1
                break
            else:
                ret = ord(key_in) - 97
        self.game_model.maze_model.overlay.replace([])
        return ret


def init_windows(root_layout):
    def win(name):
        return root_layout.info.comp_by_name[name]

    # custom windows
    win(WIN.TITLE).initwin(TitleWindow, trunc_y=SIDE.TOP)
    win(WIN.PLAYER).initwin(PlayerWindow)
    win(WIN.EQUIP).initwin(EquipWindow)
    win(WIN.STATS).initwin(StatsWindow)
    win(WIN.MAZE).initwin(MazeWindow, align_x=SIDE.CENTER, align_y=SIDE.CENTER)

    # standard windows
    win(WIN.BANNER).initwin(TextWindow, trunc_y=SIDE.TOP)
    win(WIN.MESSAGES).initwin(TextWindow, trunc_y=SIDE.TOP)


# if __name__ == '__main__':
#     model = PrpgModel(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
#     win = PrpgWindow(None, model)
