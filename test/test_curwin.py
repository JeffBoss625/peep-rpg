from lib.curwin import *
from lib.printd import printd
import curses

def test_con():
    assert Con(4, 7) != Con()
    assert Con(4, 7) == Con(4, 7)
    assert Con(4, 7, 5, 12) == Con(4, 7, 5, 12)
    assert Con(4, 7, 5, 12) != Con(4, 7, 5, 13)

def test_addcol():
    tests = [
        # root       addcol                   [ expected column ]
        # dim,       pos,      con,           [ pos(),   con(),        dim() ]
        
        [ Dim(4,12), None,     None,          [ Con(0,0),     Dim(4,12)] ],
        [ Dim(5,12), None,     Con(2,3),      [ Con(2,3),     Dim(5,12)] ],
        [ Dim(5,12), None,     Con(2,3,4,7),  [ Con(2,3,4,7), Dim(4,7)] ],

        # position not enough to affect dimensions
        [ Dim(5,12), Pos(1,2), Con(2,3,4,7),  [ Con(2,3,4,7), Dim(4,7)] ],

        # position makes dimensions shrink
        [ Dim(5,12), Pos(2,5), Con(2,3,4,7),  [ Con(2,3,4,7), Dim(3,7)] ],
        [ Dim(5,12), Pos(2,6), Con(2,3,4,7),  [ Con(2,3,4,7), Dim(3,6)] ],
    ]

    for row in tests:
        yield check_col, row[0], row[1], row[2], row[3][0], row[3][1]

# note that running nose tests with "-d" gives assertion descriptions indlucing content of dataclasses
# when variables are resolved, so we call "cpos = col.pos()..." as separate steps revieal data discrepancies.
def check_col(rootdim, colpos, colcon, expcon, expdim):
    root = mockroot(rootdim)
    col = root.panel(Orient.VERT, colpos, colcon)

    ccon = col.con()
    assert ccon == expcon
    cdim = col.dim()
    assert cdim == expdim


FLOW_TESTS = [
    # addcol
    # pos,      con           children constraints,            [ expcon,       expdim ]

    # child constraints don't affect panel constraints. panel constraints don't affect dim(10,30)
    [ None,     Con(5,10),       [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,10,0,0), Dim(10,30)] ],
    [ None,     Con(5,20),       [Con(0,0,0,0), Con(0,0,0,0)], [Con(5,20,0,0), Dim(10,30)] ],
    [ None,     Con(5,20),       [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,20,0,0), Dim(10,30)] ],

    # child constraints factor into panel constraints, but not Dim)
    [ None,     Con(2,3),     [Con(2,8,0,0),  Con(3,5,0,0)], [Con(5,8,0,0),   Dim(10,30)] ],
    [ None,     Con(0,0),     [Con(2,8,9,29), Con(3,5,0,0)],  [Con(5,8,0,0),    Dim(10,30)] ],

    # child constraints don't affect panel constraints, but panel constraints affect dim
    [ None,     Con(5,10,8,25),  [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,10,8,25), Dim(8,25)] ],
    [ None,     Con(5,10,8,25),  [Con(2,8,3,0), Con(3,5,7,0)], [Con(5,10,8,25), Dim(8,25)] ],

    # child constraints affect panel constraints, and affect Dim
    [ None,     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Con(5,8,9,29),  Dim(9,29)] ],
    [ None,     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,29)], [Con(5,8,9,29),  Dim(9,29)] ],
]

def test_col_layout():
    for t in FLOW_TESTS:
        yield check_flow_layout, Orient.VERT, Dim(10, 30), t[0], t[1], t[2], t[3][0], t[3][1]

# run same tests as test_col_layout() by using inverted input.
def test_row_layout():
    for t in FLOW_TESTS:
        panpos = t[0].invert() if t[0] else None
        pancon = t[1].invert()
        children = map(lambda c: c.invert(), t[2])
        expcon = t[3][0].invert()
        expdim = t[3][1].invert()

        yield check_flow_layout, Orient.HORI, Dim(30, 10), panpos, pancon, children, expcon, expdim

def check_flow_layout(orient, rootdim, panpos, pancon, children_con, expcon, expdim):
    root = mockroot(rootdim)
    panel = root.panel(orient, panpos, pancon)
    for cc in children_con:
        panel.subwin(cc)
    pcon = panel.con()
    assert pcon == expcon
    pdim = panel.dim()
    assert pdim == expdim

def mockroot(dim):
    root = rootwin(None)
    root._dim = dim
    return root

class Scr:
    def __init__(self, parent, pos, dim):
        self._parent = parent
        self._pos = pos
        self._dim = dim
        self._border = False
        self.children = []
        self.buf = [[]]

    def __repr__(self):
        return 'Scr[pos[{}],dim[{}],bord:{}]'.format(self._pos, self._dim, self._border)

    def derwin(self, h, w, y, x):
        ret = Scr(self, Pos(y, x), Dim(h, w))
        self.children.append(ret)
        return ret

    def mvderwin(self, y, x):
        self._pos = Pos(y, x)

    def resize(self, h, w):
        self._dim = Dim(h, w)

    def pos(self):
        if not self._pos:
            self._pos = Pos(0,0)

        return self._pos

    def dim(self):
        return self._dim

    def border(self):
        self._border = True

    def refresh(self):
        self.buf = [x[:] for x in [['.'] * self._dim.w] * (self._dim.h)]
        self._render(0, 0, self)

    def _render(self, yoff, xoff, comp):
        printd('Scr._render off[{},{}], {}'.format(yoff, xoff, comp))
        buf = self.buf
        dim = comp.dim()
        if not dim.h or not dim.w:
            printd('no size: [{}]'.format(dim))
            return

        pos = comp.pos()
        yoff += pos.y
        xoff += pos.x
        if comp._border:
            for x in range(xoff, xoff + dim.w):
                buf[yoff][x] = '-'
                buf[yoff + dim.h-1][x] = '-'

            for y in range(yoff + 1, yoff + dim.h-1):
                buf[y][xoff] = '|'
                buf[y][xoff + dim.w-1] = '|'

        for c in comp.children:
            self._render(yoff, xoff, c)

    def buflines(self):
        ret = []
        for line in self.buf:
            ret.append(''.join(line))
        return ret

def test_paint():
    dim = Dim(12,40)
    scr = Scr(None, Pos(), dim)
    root = rootwin(scr)
    root._dim = dim
    # mainrow = root.addrow()
    # mainrow.addwin(Con(8,4,8))
    # mainrow.addwin(Con(4,4,6,5))
    # mainrow.addwin(Con())

    c1 = root.panel(Orient.VERT)

    w1 = c1.subwin(Con(3, 8, 5, 0))
    r1 = w1.panel(Orient.HORI)
    w2 = r1.subwin(Con(5, 5, 5, 5))
    w3 = r1.subwin(Con(3, 3, 3, 7))

    c2 = c1.panel(Orient.VERT)
    w4 = c2.subwin(Con(3, 7, 3, 8))
    w5 = c2.subwin()

    root.do_layout()

    w1.scr().border()
    w2.scr().border()
    w3.scr().border()
    w4.scr().border()
    w5.scr().border()
    root.paint()
    scr.refresh()

    for line in scr.buflines():
        print(line)

