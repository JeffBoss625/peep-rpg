from lib.curwin import *

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
    col = root.addcol(colpos, colcon)

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
        yield check_flow_layout, Orient.VERTICAL, Dim(10,30), t[0], t[1], t[2], t[3][0], t[3][1]

# run same tests as test_col_layout() by using inverted input.
def test_row_layout():
    for t in FLOW_TESTS:
        panpos = t[0].invert() if t[0] else None
        pancon = t[1].invert()
        children = map(lambda c: c.invert(), t[2])
        expcon = t[3][0].invert()
        expdim = t[3][1].invert()

        yield check_flow_layout, Orient.HORIZONTAL, Dim(30,10), panpos, pancon, children, expcon, expdim

def check_flow_layout(orient, rootdim, panpos, pancon, children_con, expcon, expdim):
    root = mockroot(rootdim)
    panel = root.addcol(panpos, pancon) if orient == Orient.VERTICAL else root.addrow(panpos, pancon)
    for cc in children_con:
        panel.addwin(cc)
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

    def derwin(self, h, w, y, x):
        ret = Scr(self, Pos(y, x), Dim(h, w))
        self.children.append(ret)
        return ret

    def border(self):
        self._border = True

    def refresh(self):
        buf = [x[:] for x in [['.'] * self._dim.w] * self._dim.h]
        self._refresh(0, 0, buf)

    def _render(self, yoff, xoff, buf):
        dim = self._dim
        if not dim.h or not dim.w:
            return

        if self._border:
            dim = self._dim
            for x in range(xoff, xoff + dim.w):
                buf[yoff][x] = '-'
                buf[yoff + dim.h-1][x] = '-'

            for y in range(yoff + 1, yoff + dim.h-1):
                buf[y][xoff] = '|'
                buf[y][xoff + dim.w-1] = '|'
        self.buf = buf

    def _refresh(self, yoff, xoff, buf):
        pos = self._pos
        self._render(yoff + pos.y, xoff + pos.x, buf)
        for c in self.children:
            c._refresh(yoff + pos.y, xoff + pos.x, buf)

    def buflines(self):
        ret = []
        for line in self.buf:
            ret.append(''.join(line))
        return ret

def test_paint():
    dim = Dim(8,40)
    scr = Scr(None, Pos(), dim)
    root = rootwin(scr)
    root._dim = dim
    row = root.addrow()
    c1 = row.addcol()
    c2 = row.addcol()
    r1 = row.addrow()

    c1.addwin(Con(4,4,5,5))
    c1.addwin(Con(8,8))
    # c2.addwin(Con(4,3))
    # c2.addwin(Con(2,2,5,8))
    # r1.addwin(Con(3,3,4,4))

    root.paint()
    scr.refresh()

    for line in scr.buflines():
        print(line)