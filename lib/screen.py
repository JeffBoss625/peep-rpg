# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import time
import sys

from lib.constants import Color, Side
from lib.logger import Logger
from lib.screen_layout import WIN, Pos, Dim, Con


def printe(s):
    sys.stderr.write(s + "\n")

IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

# abstraction wrapping a curses screen.
class Screen:
    def __init__(self, name, params):
        self.name = name
        self.params = params
        self.parent = None
        self.children = []

        self.border = params.get('border', 1)
        self.x_margin = params.get('x_margin', 1)
        self.y_margin = params.get('y_margin', 1)
        self.curses = params.get('curses', None)        # curses library or lib.DummyCurses
        self.scr = params.get('scr', None)              # curses.window or lib.DummyWin

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair
        self.model = None
        # self.dim = None
        # self.pos = None     # todo: manage these from layout manager

        self.logger = None

    def __repr__(self):
        return 'Window"{}": margin:[{},{}] scr:{}'.format(self.name, self.x_margin, self.y_margin, self.scr)

    #
    # TREE Navigation/Initialization functions
    #
    def root(self):
        ret = self
        while ret.parent:
            ret = ret.parent
        return ret

    # delete and rebuild curses screens using layout information (recursive on children. root screen
    # is kept intact.)
    def rebuild_screens(self):
        for c in self.children:
            if c.scr:
                del c.scr
                c.scr = None
            c.scr = self.derwin(c.dim, c.pos)
            c.rebuild_screens()

    #
    # CURSES Interface
    #
    def clear(self):
        self.scr.clear()

    def derwin(self, dim, pos):
        # self.log(f'derwin({self}, {dim}, {pos})')
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

    def log(self, s):
        if not self.logger:
            self.logger = self.root().logger

        self.logger.log(s)

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
            printe('no scr to paint in {}'.format(self.name))
            return
        if self.parent and not self.model:
            raise RuntimeError('no model to paint in {}'.format(self.name))

        if self.border:
            self.scr.border()
        self.do_paint()
        # self.write_lines([' "' + self.winfo.name + '" '])
        self.scr.noutrefresh()

    def do_paint(self):
        pass
        # raise NotImplementedError()

    def paint_all(self):
        self.paint()
        for c in self.children:
            c.paint_all()

    def doupdate(self):
        self.curses.doupdate()

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

    def size_to_terminal(self):
        if self.parent:
            raise ValueError(f'resize_term is only valid on the root screen, not "{self.name}"')

        curses = self.curses
        if getattr(self, 'term_size', None) == curses.get_terminal_size():
            return

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        self.term_size = curses.get_terminal_size()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            if self.term_size != curses.get_terminal_size():
                # size changed, reset timer
                self.term_size = curses.get_terminal_size()
                t0 = time.time()

        w, h = self.term_size
        curses.resizeterm(h, w)
        self.dim = Dim(h, w)
        # self.log(f'size_to_terminal: screen "{self.name}" updated to {self.dim}')
        return w, h

class TextScreen(Screen):
    def __init__(self, name, params):
        super().__init__(name, params)
        self.trunc_x = params.get('trunc_x', Side.RIGHT)
        self.trunc_y = params.get('trunc_y', Side.BOTTOM)

    def do_paint(self):
        self.write_lines(self.model.text, self.trunc_x, self.trunc_y)

class MazeScreen(Screen):
    def __init__(self, name, params):
        super().__init__(name, params)

    def do_paint(self):
        self.write_lines(self.model.maze.text, Side.RIGHT, Side.BOTTOM)

        for p in self.model.peeps.peeps:
            self.write_char(p.x, p.y, p.char, p.fgcolor, p.bgcolor)

class PlayerStatsScreen(Screen):
    def __init__(self, name, params):
        super().__init__(name, params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])

def create_win(parent, name, params):
    wintype = params.get('wintype', WIN.FIXED)

    if wintype == WIN.FIXED:
        ret = Screen(name, params)
    elif wintype == WIN.TEXT:
        ret = TextScreen(name, params)
    elif wintype == WIN.MAZE:
        ret = MazeScreen(name, params)
    elif wintype == WIN.STATS:
        ret = PlayerStatsScreen(name, params)
    else:
        raise ValueError('unknown wintype "{}"'.format(wintype))

    if parent:
        ret.parent = parent
        ret.parent.children.append(ret)
        ret.curses = parent.curses

    return ret

# After root layout and all children are defined, call sync_delegates() on root layout to
# build and/or refresh delegate screen dimensions
def sync_delegates(root):
    root.data.dim = Dim(root.dim.h, root.dim.w)
    root.data.pos = Pos(0,0)
    root.data.logger = root.logger

    # initialize window delegates of children
    def assign_win(layout, _v, _d):
        if not layout.data:
            layout.data = create_win(layout.winparent.data, layout.name, layout.params)

        layout.data.dim = Dim(layout.dim.h, layout.dim.w)
        layout.data.pos = Pos(layout.pos.y, layout.pos.x)
    for c in root.children:
        c.iterate_win(assign_win)

    return root


