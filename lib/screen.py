# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
from lib.constants import Color, Side
from lib.screen_layout import WIN, WinLayout

IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

# abstraction wrapping a curses screen.
class Screen:
    def __init__(self, winfo, curses):
        self.winfo = winfo      # layout window information
        self.curses = curses    # curses library - allow dummy lib injection
        self.border = 1
        self.x_margin = 1
        self.y_margin = 1
        self.scr = None               # curses.window or lib.DummyWin

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair
        self.model = None

    def __repr__(self):
        return '{}: margin:[{},{}] scr:{}'.format(self.winfo, self.x_margin, self.y_margin, self.scr)
    #
    # TREE Navigation/Initialization functions
    #

    # delete and rebuild curses screens using layout information in winfo (recursive on children)
    def rebuild_screens(self):
        self.winfo.iterate_win(_rebuild_screen, self.winfo.root())

    #
    # CURSES Interface
    #
    def clear(self):
        self.scr.clear()

    def derwin(self, dim, pos):
        # self.log('derwin({}, {}, {})'.format(self, dim, pos))
        ret = self.scr.derwin(dim.h, dim.w, pos.y, pos.x)
        if self.border:
            ret.border()
        return ret

    def getmax_wh(self):
        max_y, max_x = self.scr.getmaxyx()
        max_h = max_y - self.y_margin * 2
        max_w = max_x - self.x_margin * 2
        if max_h < 0 or max_h < 0:
            return 0, 0

        return max_w, max_h

    def log(self, *args):
        self.winfo.log(args)

    def write_lines(self, lines, trunc_x=Side.RIGHT, trunc_y=Side.BOTTOM):
        if not len(lines):
            return
        scr = self.scr
        max_w, max_h = self.getmax_wh()
        if not max_h:
            return

        # scr.clear()
        x = self.x_margin
        y = self.y_margin

        nlines = len(lines)
        if nlines > max_h:
            if trunc_y == Side.BOTTOM:
                lines = lines[:max_h]
            else: # Side.TOP
                lines = lines[nlines - max_h:]

        for i, line in enumerate(lines):
            if len(line) > max_w:
                if trunc_x == Side.RIGHT:
                    line = line[0:max_w - 1]
                else: # Side.LEFT
                    line = line[len(line) - max_w:]
            scr.addstr(y+i, x, line)

    # curses.window.refresh() calls curses.window.noutrefresh() and curses.doupate() and is not efficient for
    # calling on all subwindows.
    # Call window.paint() and then curses.doupdate() from the main screen loop instead.
    def paint(self):
        if not self.scr:
            return
        if not self.model:
            raise RuntimeError('no model for screen {}'.format(self.winfo.name))
        if not self.model._dirty:
            return

        if self.border:
            self.scr.border()
        self.do_paint()
        self.scr.noutrefresh()

    def do_paint(self):
        pass
        # raise NotImplementedError()

    def paint_all(self):
        self.winfo.iterate_win(lambda win, v, c: {win.paint()})

    def get_key(self):
        while 1:
            try:
                ret = self.scr.getkey()
                if ret not in IGNORED_KEYS:
                    return ret

            except Exception as e:
                # self.winfo.log('get_key failed: type:"{}", trace: {}'.format(
                #     str(e),
                #     ''.join(traceback.format_tb(e.__traceback__)))
                # )
                pass        # ignore interrupts to getkey() following resize events etc.

    def write_char(self, x, y, char, fg=Color.WHITE, bg=Color.BLACK):
        max_w, max_h = self.getmax_wh()
        if x >= max_w or y >= max_h:
            return

        cpair = self.color_pair(fg, bg)
        self.scr.addstr(y + self.y_margin, x + self.x_margin, char, cpair)

    def color_pair(self, fg, bg):
        curses = self.curses
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            fgc = getattr(curses, Color.curses_color(fg))
            bgc = getattr(curses, Color.curses_color(bg))
            curses.init_pair(self.color_pair_count, fgc, bgc)
            self.color_pairs[key] = curses.color_pair(self.color_pair_count)

        return self.color_pairs[key]

# delete and re-create derived curses windows ("screens") using parent windows/screens
def _rebuild_screen(winfo, _v, _d):
    if not winfo.winparent:         # don't build root screen - root screen is fixed
        return

    if winfo.data.scr:
        del winfo.data.scr
        winfo.data.scr = None # allow .scr to be checked

    winfo.data.scr = winfo.winparent.data.derwin(winfo.dim, winfo.pos)
    if winfo.data.border:
        winfo.data.scr.border()

class TextScreen(Screen):
    def __init__(self, winfo, curses):
        super().__init__(winfo, curses)
        self.trunc_x = winfo.params.get('trunc_x', Side.RIGHT)
        self.trunc_y = winfo.params.get('trunc_y', Side.BOTTOM)

    def do_paint(self):
        self.write_lines(self.model.text, self.trunc_x, self.trunc_y)

class MazeScreen(Screen):
    def __init__(self, winfo, curses):
        super().__init__(winfo, curses)

    def do_paint(self):
        self.write_lines(self.model.maze.text, Side.RIGHT, Side.BOTTOM)

        for p in self.model.peeps.peeps:
            self.write_char(p.x, p.y, p.char, p.fgcolor, p.bgcolor)

class PlayerStatsScreen(Screen):
    def __init__(self, winfo, curses):
        super().__init__(winfo, curses)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])



# build windows for children
def _create_child_data(winfo, curses, _depth):
    if winfo.wintype == WIN.FIXED:
        winfo.data = Screen(winfo, curses)
    elif winfo.wintype == WIN.TEXT:
        winfo.data = TextScreen(winfo, curses)
    elif winfo.wintype == WIN.MAZE:
        winfo.data = MazeScreen(winfo, curses)
    elif winfo.wintype == WIN.STATS:
        winfo.data = PlayerStatsScreen(winfo, curses)
    else:
        raise ValueError('unknown wintype "{}"'.format(winfo.wintype))
    return curses

# initialize Win wrappers, populating all WinInfo with wrappers and set up root screen.
def create_win_data(winfo, scr, curses):
    # set up root
    _create_child_data(winfo, curses, 0)
    winfo.data.scr = scr
    winfo.data.border = 0

    for c in winfo.children:
        c.iterate_win(_create_child_data, curses)



