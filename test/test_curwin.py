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


def test_col_layout():
    tests = [
        # addcol
        # pos,      con           children constraints,         [ expcon,       expdim ]

        # child constraints fall within existing constraints (have no effect)
        [ None,     Con(5,20),    [Con(0,0,0,0), Con(0,0,0,0)], [Con(5,20,0,0), Dim(10,30)] ],
        [ None,     Con(5,20),    [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,20,0,0), Dim(10,30)] ],
        [ None,     Con(5,10),    [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,10,0,0), Dim(10,30)] ],

        # child constraints do not fit within other constraints, but not Dim)
        [ None,     Con(2,3),     [Con(2,8,0,0),  Con(3,5,0,0)], [Con(5,8,0,0),   Dim(10,30)] ],

        # child constraints do not fit within other constraints, and do affect Dim
        [ None,     Con(2,3),     [Con(2,8,9,29), Con(3,5,0,0)],  [Con(5,8,9,29),  Dim(9,29)] ],
        [ None,     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,29)], [Con(5,8,9,29),  Dim(9,29)] ],

    ]

    for row in tests:
        root = mockroot(Dim(10,30))
        yield check_col_layout, root, row[0], row[1], row[2], row[3][0], row[3][1]

def check_col_layout(root, colpos, colcon, children_con, expcon, expdim):
    col = root.addcol(colpos, colcon)
    for cc in children_con:
        col.addwin(cc)
    ccon = col.con()
    assert ccon == expcon
    cdim = col.dim()
    assert cdim == expdim

def mockroot(dim):
    root = rootwin(None)
    root._dim = dim
    return root
