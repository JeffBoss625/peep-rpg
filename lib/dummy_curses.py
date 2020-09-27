from lib.constants import Key
from lib.screen_layout import Dim, Pos, Con
import sys

def printe(s):
    sys.stderr.write(s + "\n")

# substitute window implementing curses window behavior as printed output to terminal stderr, for debugging.
class DummyCursesWindow:
    def __init__(self, parent, pos, dim):
        self.parent = parent
        self.pos = Pos(pos.y, pos.x)
        self.con = None
        if parent:
            self.buf = parent.buf
            self.dim = Dim(dim.h, dim.w)
        else:
            self.resize(dim.h, dim.w)

    def __repr__(self):
        return 'DummyWin(pos:[{}],dim:[{}])'.format(self.pos, self.dim)

    def resize(self, h, w):
        if self.parent:
            raise ValueError("resize() supported only for root")

        self.dim = Dim(h, w)
        self.buf = [x[:] for x in [['.'] * self.dim.w] * self.dim.h]

    def clear(self):
        dim = self.dim
        buf = self.buf
        xoff, yoff = self.xyoff()
        xlim = xoff + dim.w
        ylim = yoff + dim.h
        for y in range(yoff, ylim):
            for x in range(xoff, xlim):
                buf[y][x] = '.'

    def border(self):
        # printe('border({})'.format(self))
        dim = self.dim
        buf = self.buf
        xoff, yoff = self.xyoff()
        xlim = xoff + dim.w
        ylim = yoff + dim.h
        for x in range(xoff, xlim):
            buf[yoff][x] = '-'
            buf[ylim-1][x] = '-'

        for y in range(yoff, ylim):
            buf[y][xoff] = '|'
            buf[y][xlim-1] = '|'

    def refresh(self):
        raise NotImplementedError("use noutrefresh() instead")

    def noutrefresh(self):
        pass

    def root(self):
        ret = self
        while ret.parent:
            ret = ret.parent
        return ret

    def doupdate(self):
        self.root()._doupdate()

    def _doupdate(self):
        for i, line in enumerate(self.buf):
            printe("{:<3} {}".format(i, ''.join(line)))
        printe('')

    def derwin(self, h, w, y, x):
        return DummyCursesWindow(self, Pos(y, x), Dim(h, w))

    def xyoff(self):
        win = self
        x = y = 0
        while win:
            x += win.pos.x
            y += win.pos.y
            win = win.parent
        return x, y

    def getmaxyx(self):
        return self.dim.h, self.dim.w

    def addstr(self, y, x, s, _color_pair=None):
        xoff, yoff = self.xyoff()
        y += yoff
        x += xoff
        for xi in range(0, len(s)):
            self.buf[y][x + xi] = s[xi]

    def getkey(self):
        try:
            ret = input('->')
            return ret[0]
        except KeyboardInterrupt:
            printe('KeyboardInterrupt')
            return Key.CTRL_Q

class DummyCurses:
    COLOR_BLACK = 0
    COLOR_BLUE = 4
    COLOR_CYAN = 6
    COLOR_GREEN = 2
    COLOR_MAGENTA = 5
    COLOR_RED = 1
    COLOR_WHITE = 7
    COLOR_YELLOW = 3

    def __init__(self, dim):
        self.term = DummyCursesWindow(None, Pos(), dim)
        self.term.curses = self

    def resizeterm(self, h, w):
        self.term.resize(h, w)

    def get_terminal_size(self):
        return self.term.dim.w, self.term.dim.h

    def doupdate(self):
        self.term.doupdate()

    def raw(self):
        pass

    def curs_set(self, _n):
        pass

    def init_pair(self, _n, _fgc, _bgc):
        pass

    def color_pair(self, _n):
        pass

