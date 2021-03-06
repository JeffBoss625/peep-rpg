from lib.model import TextModel
from lib.startup import dummy_root
from lib.window import TextWindow
from lib.win_layout import *
import sys



def printe(s):
    sys.stderr.write(s + "\n")

def test_con():
    assert Con(7,4) != Con()
    assert Con(7,4) == Con(7,4)
    assert Con(7,4,12,5) == Con(7,4,12,5)
    assert Con(7,4,12,5) != Con(7,4,13,5)

def test_addcol():
    tests = [
        # root       addcol                   [ expected column ]
        # dim,       pos,      con,           [ pos(),   con(),        dim ]
        
        [ Dim(12,4), None,     None,          [ Con(0,0),     Dim(12,4)] ],
        [ Dim(12,5), None,     Con(3,2),      [ Con(3,2),     Dim(12,5)] ],
        [ Dim(12,5), None,     Con(3,2,7,4),  [ Con(3,2,7,4), Dim(7,4)] ],

        # position not enough to affect dimensions
        [ Dim(12,5), Pos(2,1), Con(3,2,7,4),  [ Con(3,2,7,4), Dim(7,4)] ],

        # position makes dimensions shrink
        [ Dim(12,5), Pos(5,2), Con(3,2,7,4),  [ Con(3,2,7,4), Dim(7,3)] ],
        [ Dim(12,5), Pos(6,2), Con(3,2,7,4),  [ Con(3,2,7,4), Dim(6,3)] ],
    ]

    for row in tests:
        yield check_col, row[0], row[1], row[2], row[3][0], row[3][1]

# note that running nose tests with "-d" gives assertion descriptions including content of dataclasses
# when variables are resolved, so we call "cpos = col.pos()..." as separate steps reveal data discrepancies.
def check_col(rootdim, colpos, colcon, expcon, expdim):
    root = dummy_root(rootdim)
    col = root.panel('pan1', Orient.VERT, colpos, colcon)
    root.do_layout()

    ccon = col.con
    assert ccon == expcon
    cdim = col.dim
    assert cdim == expdim

def test_flow_calc_sizes():
    # avail_space, mins, maxs, expected_sizes
    tests = [
        [5, [4], [5], [5]],
        [4, [4], [5], [4]],
        [3, [4], [5], [3]],
        [5, [4,4], [8,8], [4,1]],
        [6, [4,4], [8,8], [4,2]],
        [7, [4,4], [8,8], [4,3]],
        [8, [4,4], [8,8], [4,4]],
        [9, [4,4], [8,8], [4,5]],
        [10, [4,4], [8,8], [5,5]],
        [3, [4,4,4], [5,6,7], [3,0,0]],
        [4, [4,4,4], [5,6,7], [4,0,0]],
        [5, [4,4,4], [5,6,7], [4,1,0]],
        [11, [4,4,4], [5,6,7], [4,4,3]],
        [12, [4,4,4], [5,6,7], [4,4,4]],
        [13, [4,4,4], [5,6,7], [4,4,5]],
        [20, [4,4,4], [5,6,7], [5,6,7]],
    ]

    for row in tests:
        yield check_flow_sizes, row[0], row[1], row[2], row[3]

def check_flow_sizes(avail, mins, maxs, exp):
    sizes = flow_calc_sizes(avail, mins, maxs)
    assert sizes == exp


# tests of flow layout within a 10x30 master window
FLOW_TESTS_10_30 = [
    # addcol
    # pos,      con           children constraints,            [ exp_parent_dim, exp_child_dims ]

    # child constraints don't affect panel constraints. panel constraints don't affect dim(10,30)
    [ None,     Con(10,5),       [Con(8,2,0,0), Con(5,3,0,0)], [Dim(30,10), Dim(30,4), Dim(30,6)] ],
    [ None,     Con(20,5),       [Con(0,0,0,0), Con(0,0,0,0)], [Dim(30,10), Dim(30,5), Dim(30,5)] ],

    # children dimensions limited by panel constraints
    [ None,     Con(10,5,25,9),  [Con(8,2,20,3), Con(5,3,0,0)], [Dim(25,9), Dim(20,3), Dim(25,6)] ],
    [ None,     Con(10,5,25,9),  [Con(8,2,0,0), Con(5,2,20,2)], [Dim(25,9), Dim(25,4), Dim(20,2)] ],
    [ None,     Con(10,5,25,9),  [Con(8,2,0,0), Con(5,2,0,0)], [Dim(25,9), Dim(25,4), Dim(25,5)] ],

    # children minimum size doesn't fit
    [ None,     Con(6,3,25,4),  [Con(8,4,0,0), Con(5,4,0,0)], [Dim(25,4), Dim(25,4), Dim(25,0)] ],
    [ None,     Con(6,3,25,5),  [Con(8,4,0,0), Con(5,4,0,0)], [Dim(25,5), Dim(25,4), Dim(25,1)] ],
    [ None,     Con(6,3,25,7),  [Con(8,4,0,0), Con(5,4,0,0)], [Dim(25,7), Dim(25,4), Dim(25,3)] ],

    # panel shrinks to fit child constraints
    [ None,     Con(3,2),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(29,9), Dim(29,4), Dim(28,5)] ],
    [ None,     Con(3,2),     [Con(8,2,29,4), Con(5,3,29,5)], [Dim(29,9), Dim(29,4), Dim(29,5)] ],

    # Positions
    [ Pos(1,1),     Con(10,5),    [Con(8,2,0,0),  Con(5,3,0,0)],  [Dim(29,9), Dim(29,4), Dim(29,5)] ],

    # position causes panel to shrink
    [ Pos(0,0),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(29,9), Dim(29,4), Dim(28,5)] ],
    [ Pos(2,0),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(28,9), Dim(28,4), Dim(28,5)] ],
    [ Pos(3,0),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(27,9), Dim(27,4), Dim(27,5)] ],
    [ Pos(3,1),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(27,9), Dim(27,4), Dim(27,5)] ],
    [ Pos(3,2),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(27,8), Dim(27,3), Dim(27,5)] ],
    [ Pos(3,3),     Con(),     [Con(8,2,29,4), Con(5,3,28,5)], [Dim(27,7), Dim(27,3), Dim(27,4)] ],
]

# def test_wide():
# [ Pos(0,2),     Con(100,12,100,12), [Con(3,5,6,10), Con(5,3,28,5)], [Con(8,5,29,9),  Dim(29,9)] ],


def test_layout_vertical():
    for t in FLOW_TESTS_10_30:
        yield check_flow_layout, Orient.VERT, Dim(30,10), t[0], t[1], t[2], t[3][0], t[3][1:]

# run same tests as test_layout_vertical() by using inverted input.
def test_layout_horizontal():
    for t in FLOW_TESTS_10_30:
        pos = t[0].invert() if t[0] else None
        con = t[1].invert()
        children = list(c.invert() for c in t[2])
        exp_parent_dim = t[3][0].invert()
        exp_child_dims = list(c.invert() for c in t[3][1:])

        yield check_flow_layout, Orient.HORI, Dim(10,30), pos, con, children, exp_parent_dim, exp_child_dims

def check_flow_layout(orient, dim, pos, con, children_con, exp_pdim, exp_cdims):
    root = dummy_root(dim)
    # root.log(f'check_flow_layout({orient} dim:[{dim}] pos:[{pos}] con:[{con}] child_con:{children_con})')
    panel = root.panel('root-pan', orient, pos, con)
    for cc in children_con:
        panel.window(None, cc)
    for c in panel.children:
        c.initwin(TextWindow, model=TextModel(['hi']))

    root.do_layout()
    # root.window.paint()

    pdim = panel.dim
    assert pdim == exp_pdim

    dims = list(c.dim for c in panel.children)
    assert dims == exp_cdims


# def print_win(v, win, xoff, yoff, depth):
#     print('{}, {}, {}, {}'.format(win, xoff, yoff, depth))

def print_win(root):
    buf = [x[:] for x in [['.'] * root.dim.w] * root.dim.h]
    root.iterate_win(print_one_win, buf)
    for i, line in enumerate(buf):
        printe("{:<4} {}".format(i, ''.join(line)))

def print_one_win(win, buf, xoff, yoff, depth):
    # printe('print_one_win({}, off:[{}, {}], depth:{}'.format(win, xoff, yoff, depth))
    if not win.window.border:
        return buf

    dim = win.dim
    pos = win.pos
    xoff += pos.x
    yoff += pos.y
    xlim = xoff + dim.w
    ylim = yoff + dim.h
    for x in range(xoff, xlim):
        buf[yoff][x] = '-'
        buf[ylim-1][x] = '-'

    for y in range(yoff, ylim):
        buf[y][xoff] = '|'
        buf[y][xlim-1] = '|'

    return buf

def test_paint():
    printe('')
    root = dummy_root(Dim(100,15))
    hpan = root.panel('root-panel', Orient.HORI, None, None)

    w1 = hpan.window('w1', Con(10,4,20,5))
    w2 = hpan.window('w2', Con(5,3,10,8))

    w1.initwin(TextWindow, model=TextModel('model 1', 'window 1'))
    w2.initwin(TextWindow, model=TextModel('model 2', 'window 2'))
    root.do_layout()
    # root.window.paint()

    assert root.info.comp_by_name['w1'].name == 'w1'
    assert root.info.comp_by_name['w2'].name == 'w2'
    assert root.info.comp_by_name['root'].name == 'root'
    assert hpan.con == Con(15,4,30,8)

    root.clear_layout()
    assert hpan.con is None

    root.do_layout()
    assert hpan.con == Con(15,4,30,8)

