from lib.constants import Key
from lib.win_layout import Dim, Pos
import sys

def printe(s):
    sys.stderr.write(s + "\n")

# substitute window implementing curses window behavior as printed output to terminal stderr, for debugging.
class DummyCursesWindow:
    def __init__(self, parent, pos, dim):
        self.parent = parent
        self.pos = Pos(pos.x, pos.y)
        self.con = None
        if parent:
            self.buf = parent.buf
            self.dim = Dim(dim.w, dim.h)
        else:
            self.resize(dim.h, dim.w)

    def __repr__(self):
        return f'DummyWin(pos:[{self.pos}],dim:[{self.dim}])'

    # note the inverted dimensions (h, w) for curses
    def resize(self, h, w):
        if self.parent:
            raise ValueError("resize() supported only for root")

        self.dim = Dim(w, h)
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
        if not self.buf:
            printe('<EMPTY_BUFFER>')
            return

        num_line = ''
        for i in range(len(self.buf[0])):
            num_line += str((i+1) % 10)

        printe('    ' + num_line)
        for i, line in enumerate(self.buf):
            printe(f"{i+1:<3} {''.join(line)}")
        printe('    ' + num_line)
        printe('')

    def derwin(self, h, w, y, x):
        return DummyCursesWindow(self, Pos(x, y), Dim(w, h))

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

    def chgat(self, y, x, n, attr):
        pass

    def addstr(self, y, x, s, _attrib=0):
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

    def move(self, y, x):
        pass

class DummyCurses:
    COLOR_BLACK = 0
    COLOR_RED = 1
    COLOR_GREEN = 2
    COLOR_YELLOW = 3
    COLOR_BLUE = 4
    COLOR_MAGENTA = 5
    COLOR_CYAN = 6
    COLOR_WHITE = 7

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

    def chgat(self, *args):
        pass

    def init_pair(self, _n, _fgc, _bgc):
        pass

    def color_pair(self, _n):
        return 1


