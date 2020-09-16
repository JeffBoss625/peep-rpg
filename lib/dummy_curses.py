from lib.screen_layout import Dim
import sys

COLOR_BLACK = 0
COLOR_BLUE = 4
COLOR_CYAN = 6
COLOR_GREEN = 2
COLOR_MAGENTA = 5
COLOR_RED = 1
COLOR_WHITE = 7
COLOR_YELLOW = 3

def printe(s):
    sys.stderr.write(s + "\n")

class DummyWin:
    def __init__(self, dim, parent):
        self.dim = dim
        self.parent = parent
        self.buf = [x[:] for x in [['.'] * dim.w] * dim.h]

    def clear(self):
        self.buf = [x[:] for x in [['.'] * self.dim.w] * self.dim.h]

    def border(self):
        dim = self.dim
        buf = self.buf
        xoff = 0        # todo: use offset position from parent
        yoff = 0
        xlim = xoff + dim.w
        ylim = yoff + dim.h
        for x in range(xoff, xlim):
            buf[yoff][x] = '-'
            buf[ylim-1][x] = '-'

        for y in range(yoff, ylim):
            buf[y][xoff] = '|'
            buf[y][xlim-1] = '|'

    def refresh(self):
        self.noutrefresh()

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
            printe("{:<4} {}".format(i, ''.join(line)))
        printe('')

    def derwin(self, h, w, y, x):
        return self

    def getmaxyx(self):
        return self.dim.h, self.dim.w

    def addstr(self, y, x, s, color=COLOR_WHITE):
        for xi in range(0, len(s)):
            self.buf[y][x + xi] = s[xi]


DEFAULT_DIM = Dim(40,80)
TERM = DummyWin(DEFAULT_DIM, None)

def wrapper(fn):
    fn(TERM)

def doupdate():
    TERM.doupdate()

def raw():
    pass

def get_terminal_size():
    return DEFAULT_DIM.w, DEFAULT_DIM.h

def curs_set(n):
    pass

def init_pair(n, fgc, bgc):
    pass

def color_pair(n):
    pass

