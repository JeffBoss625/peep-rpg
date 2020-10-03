# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import sys
from dataclasses import dataclass, field

from lib.constants import COLOR, SIDE, curses_color
from lib.screen_layout import Pos, Dim, min0

def printe(s):
    sys.stderr.write(s + "\n")


IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

@dataclass
class RootInfo:
    win_count: int = 0
    win_by_name: dict = field(default_factory=dict)

# abstraction wrapping a curses screen.
class Screen:
    def __init__(self, name, parent, params):
        self.name = name
        self.params = params
        self.parent = parent
        self.children = []

        self.border = params.get('border', 1)
        self.x_margin = params.get('x_margin', 1)
        self.y_margin = params.get('y_margin', 1)
        self.curses = params.get('curses', None)        # curses library or lib.DummyCurses
        self.scr = params.get('scr', None)              # curses.window or lib.DummyWin

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair
        self.model = None
        self.needs_paint = True
        # self.dim = None
        # self.pos = None     # todo: manage these from layout manager

        self.logger = None

        if parent:
            self.curses = parent.curses
            parent.children.append(self)

        # store consolidated window information in the root object
        if parent:
            root = parent
            while root.parent:
                root = root.parent
        else:
            self.info = RootInfo()
            root = self

        root.info.win_count += 1
        self.id = root.info.win_count
        if not self.name:
            self.name = f'comp{self.id}'
        if hasattr(root.info.win_by_name, self.name):
            raise ValueError(f'multiple components with the same name: "{self.name}"')

        root.info.win_by_name[self.name] = self


    def __repr__(self):
        return 'Window"{}": margin:[{},{}] scr:{}'.format(self.name, self.x_margin, self.y_margin, self.scr)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        if not hasattr(self, '__model') or m != getattr(self, '__model', None):
            self.__model = m

            if m:
                def update_fn(_model, _msg, **_kwds):
                    self.needs_paint = True
                m.subscribe(update_fn)
                self.needs_paint = True

    def update_layout(self, pos, dim, logger):
        self.pos = pos
        self.dim = dim
        self.logger = logger

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
            if c.dim.w and c.dim.h:
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

    def write_lines(self, lines, **params):
        trunc_x = params.get('trunc_x', SIDE.RIGHT)
        trunc_y = params.get('trunc_y', SIDE.BOTTOM)
        align_x = params.get('align_x', SIDE.LEFT)
        align_y = params.get('align_y', SIDE.TOP)
        text_w = params.get('text_w', 0)    # if set, use this as the fixed text width for alignment and truncation

        if not len(lines):
            return
        max_w, max_h = self.getmax_wh()
        if not max_h:
            return
        trunc_w = min0(text_w, max_w)

        nlines = len(lines)
        if nlines > max_h:
            if trunc_y == SIDE.BOTTOM:
                lines = lines[:max_h]
            else: # Side.TOP
                lines = lines[nlines - max_h:]

        y = align_y_offset(align_y, self.y_margin, len(lines), max_h)

        scr = self.scr
        for i, line in enumerate(lines):
            if len(line) > trunc_w:
                if trunc_x == SIDE.RIGHT:
                    line = line[0:trunc_w - 1]
                else: # Side.LEFT
                    line = line[len(line) - max_w:]

            if len(line) >= max_w:
                x = self.x_margin
            else:
                x = align_x_offset(align_x, self.x_margin, len(line), max_w)

            # self.log(f'addstr({y+i}, {x}, {len(line)})')
            scr.addstr(y+i, x, line)

    # curses.window.refresh() calls curses.window.noutrefresh() and curses.doupate() and is not efficient for
    # calling on all subwindows.
    # Call window.paint() and then curses.doupdate() from the main screen loop instead.
    def paint(self, force=False):
        if not self.scr:
            printe('no scr to paint in {}'.format(self.name))
            return
        if self.parent and not self.model:
            raise RuntimeError('no model to paint in {}'.format(self.name))
        if self.dim.w == 0 or self.dim.h == 0:
            return
        # if not self.needs_paint and not force:
        #     return

        self.clear()
        for c in self.children:
            c.paint(force)

        if self.border:
            self.scr.border()
        self.do_paint()
        # self.write_lines([' "' + self.winfo.name + '" '])
        self.scr.noutrefresh()
        self.needs_paint = False
        if self.parent is None:
            self.doupdate()

    def do_paint(self):
        pass

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

    def write_char(self, x, y, char, fg=COLOR.WHITE, bg=COLOR.BLACK, **params):
        max_w, max_h = self.getmax_wh()
        if x >= max_w or y >= max_h:
            return

        align_x = params.get('align_x', SIDE.LEFT)
        align_y = params.get('align_y', SIDE.TOP)
        text_w = min(params.get('text_w', 1), max_w)
        text_h = min(params.get('text_h', 1), max_h)

        cpair = self.color_pair(fg, bg)
        xoff = align_x_offset(align_x, self.x_margin, text_w, max_w)
        # self.log(f'align_y_offset({align_y}, {self.y_margin}, 1, {max_h})')
        yoff = align_y_offset(align_y, self.y_margin, text_h, max_h)
        # self.log(f'addstr({yoff} + {y}, {xoff} + {x}, {char})')
        self.scr.addstr(yoff + y, xoff + x, char, cpair)

    def color_pair(self, fg, bg):
        curses = self.curses
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            fgc = getattr(curses, curses_color(fg))
            bgc = getattr(curses, curses_color(bg))
            curses.init_pair(self.color_pair_count, fgc, bgc)
            self.color_pairs[key] = curses.color_pair(self.color_pair_count)

        return self.color_pairs[key]

    # required factory function for layout interface
    def create_child_window(self, name, params):
        wintype = params.get('wintype', None)

        if wintype is None:
            wintype = BlankScreen
        return wintype(name, self, params)


# align_x_offset only called when linelen < max_w
def align_x_offset(align_x, margin_x, linelen, max_w):
    if align_x == SIDE.LEFT:
        return margin_x
    elif align_x == SIDE.RIGHT:
        return max_w - linelen
    elif align_x == SIDE.CENTER:
        return margin_x + int(max_w/2) - int(linelen/2)
    else:
        raise ValueError(f'illegal value for align_x: "{align_x}"')

def align_y_offset(align_y, margin_y, nlines, max_h):
    if align_y == SIDE.TOP:
        return margin_y
    elif align_y == SIDE.BOTTOM:
        return max_h - nlines
    elif align_y == SIDE.CENTER:
        return margin_y + int(max_h/2) - int(nlines/2)
    else:
        raise ValueError(f'illegal value for align_y: "{align_y}"')


class TextScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)

    def do_paint(self):
        self.write_lines(self.model.text, **self.params)

class BlankScreen(Screen):
    def __init__(self, name, parent, params):
        super().__init__(name, parent, params)


# After root layout and all children are defined, call sync_delegates() on root layout to
# build and/or refresh delegate screen dimensions
def sync_delegates(root):
    root.data.update_layout(Pos(0,0), Dim(root.dim.h, root.dim.w), root.logger)

    # initialize window delegates of children
    def assign_win(layout, _v, _d):
        if not layout.data:
            layout.data = layout.winparent.data.create_child_window(layout.name, layout.params)

        layout.data.dim = Dim(layout.dim.h, layout.dim.w)
        layout.data.pos = Pos(layout.pos.y, layout.pos.x)
    for c in root.children:
        c.iterate_win(assign_win)

    return root


