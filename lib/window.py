# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
from dataclasses import dataclass, field

from lib.constants import COLOR, SIDE, curses_color
from lib.util import min0


IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

@dataclass
class RootInfo:
    win_count: int = 0
    win_by_name: dict = field(default_factory=dict)

# abstraction wrapping a curses window.
class Window:
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
        self.model = params.get('model', None)

        self.needs_paint = True

        if self.model:
            def update_fn(_model, _msg, **_kwds):
                self.needs_paint = True
            self.model.subscribe(update_fn)

        if parent:
            self.curses = parent.curses
            parent.children.append(self)
        else:
            self.curses = params.get('curses')
            self.curses.color_pairs = {}
            self.curses.color_pair_count = 0

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
        return f'Window"{self.name}": margin:[{self.x_margin} {self.y_margin}] scr:{self.scr}'

    # delete and rebuild curses windows using layout information (recursive on children. root window
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
        # self.log(f'clear({self}')
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
        self.root().logger.log(s)

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
    # Call window.paint() and then curses.doupdate() from the main loop instead.
    def paint(self, force=False):
        # self.log(f'paint({self}, {force})')
        if not self.scr:
            self.log(f'no scr to paint in {self.name}')
            return
        if self.parent and not self.model:
            raise RuntimeError(f'no model to paint in {self.name}')

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
                # self.log(f'get_key failed: type:"{str(e)}", trace: {"".join(traceback.format_tb(e.__traceback__))}')
                pass        # ignore interrupts to getkey() following resize events etc.

    def xy_offset(self, x, y, slen, **params):
        max_w, max_h = self.getmax_wh()
        if x + slen > max_w or y >= max_h:
            return -1

        align_x = params.get('align_x', SIDE.LEFT)
        align_y = params.get('align_y', SIDE.TOP)
        text_w = min(params.get('text_w', 1), max_w)
        text_h = min(params.get('text_h', 1), max_h)
        xoff = align_x_offset(align_x, self.x_margin, text_w, max_w)
        # self.log(f'align_y_offset({align_y}, {self.y_margin}, 1, {max_h})')
        yoff = align_y_offset(align_y, self.y_margin, text_h, max_h)
        # self.log(f'addstr({yoff} + {y}, {xoff} + {x}, {char})')
        return xoff, yoff

    def change_attr(self, x, y, n, attr, **params):
        xoff, yoff = self.xy_offset(x, y, n, **params)
        if xoff == -1:
            return
        self.scr.chgat(yoff + y, xoff + x, n, attr)

    def write_str(self, x, y, s, fg=COLOR.WHITE, bg=COLOR.BLACK, **params):
        slen = len(s)
        xoff, yoff = self.xy_offset(x, y, slen, **params)
        if xoff == -1:
            return slen

        cpair = self.color_pair(fg, bg)
        self.scr.addstr(yoff + y, xoff + x, s, cpair)
        return slen

    def color_pair(self, fg, bg):
        curses = self.curses
        key = (fg, bg)
        if key not in curses.color_pairs:
            curses.color_pair_count += 1
            fgc = getattr(curses, curses_color(fg))
            bgc = getattr(curses, curses_color(bg))
            curses.init_pair(curses.color_pair_count, fgc, bgc)
            curses.color_pairs[key] = curses.color_pair(curses.color_pair_count)

        return curses.color_pairs[key]

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


class TextWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        self.write_lines(self.model.text, **self.params)

class RootWindow(Window):
    def __init__(self, name, **params):
        self.dim = params['dim']
        self.logger = params['logger']
        super().__init__(name, None, **params)

    # called after main terminal window is resized by a user, but before layouts are recalculated.
    def handle_resizing(self, w, h):
        self.curses.resizeterm(h, w)    # note curses inverted h and w





