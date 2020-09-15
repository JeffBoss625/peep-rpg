import sys

def printe(s):
    sys.stderr.write(s + "\n")

class DummyScreen:
    def __init__(self, dim):
        self.dim = dim
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
        self.noutupdate()
        self.doupdate()

    def noutupdate(self):
        pass

    def doupdate(self):
        for i, line in enumerate(self.buf):
            printe("{:<4} {}".format(i, ''.join(line)))
        printe('')

    def derwin(self, h, w, y, x):
        return self

    def getmaxyx(self):
        return self.dim.h, self.dim.w

    def addstr(self, y, x, s):
        for xi in range(0, len(s)):
            self.buf[y][x + xi] = s[xi]
