# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import sys
from dataclasses import dataclass, field

from lib.constants import COLOR, SIDE, curses_color
from lib.screen_layout import min0


def printe(s):
    sys.stderr.write(s + "\n")


IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

@dataclass
class RootInfo:
    win_count: int = 0
    win_by_name: dict = field(default_factory=dict)

# abstraction wrapping a curses window.
class Screen:
    def __init__(self, name, parent, **params):
        self.name = name
        self.params = params
        self.parent = parent
        self.children = []

        self.border = params.get('border')
        self.x_margin = params.get('x_margin')
        self.y_margin = params.get('y_margin')
        self.curses = params.get('curses', None)        # curses library or instance of lib.DummyCurses
        self.scr = params.get('scr', None)              # curses root window or instance of lib.DummyWin

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair
        self.needs_paint = True

        self._logger = params.get('logger', None)
        self.model = params.get('model', None)

        if self.model:
            def update_fn(_model, _msg, **_kwds):
                self.needs_paint = True
            self.model.subscribe(update_fn)

        if parent:
            self.curses = parent.curses
            parent.children.append(self)
        else:
            self.curses = params.get('curses')

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

    # delete and rebuild curses screens using layout information (recursive on children. root screen
    # is kept intact.)
    def layout_change(self, parent, pos, dim):
        if parent is None:
            raise ValueError('root changes to pos and dim not supported')
        if self.scr:
            del self.scr
            self.scr = None

        if dim.w and dim.h:
            self.scr = parent.derwin(dim, pos)

    #
    # TREE Navigation/Initialization functions
    #
    def root(self):
        ret = self
        while ret.parent:
            ret = ret.parent
        return ret

    #
    # CURSES Interface
    #
    def clear(self):
        self.log(f'clear({self}')
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

    # todo: move _logger to root
    def logger(self):
        if not self._logger:
            self._logger = self.root()._logger
        return self._logger

    def log(self, s):
        self.logger().log(s)

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
        self.log(f'paint({self}, {force})')
        if not self.scr:
            self.log(f'no scr to paint in {self.name}')
            return
        if self.parent and not self.model:
            raise RuntimeError('no model to paint in {}'.format(self.name))

        if self.needs_paint or force:
            self.clear()
            if self.border:
                self.scr.border()
            force = True    # force children to paint

        for c in self.children:
            c.paint(force)

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
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        self.write_lines(self.model.text, **self.params)

class RootScreen(Screen):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    # called after main terminal window is resized by a user, but before layouts are recalculated.
    def handle_resizing(self, w, h):
        self.curses.resizeterm(w, h)





