from lib.model import TextModel
from lib.screen import TextWindow
from lib.screen_layout import *
import sys



def printe(s):
    sys.stderr.write(s + "\n")

def test_con():
    assert Con(4, 7) != Con()
    assert Con(4, 7) == Con(4, 7)
    assert Con(4, 7, 5, 12) == Con(4, 7, 5, 12)
    assert Con(4, 7, 5, 12) != Con(4, 7, 5, 13)

def test_addcol():
    tests = [
        # root       addcol                   [ expected column ]
        # dim,       pos,      con,           [ pos(),   con(),        dim ]
        
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

# note that running nose tests with "-d" gives assertion descriptions including content of dataclasses
# when variables are resolved, so we call "cpos = col.pos()..." as separate steps reveal data discrepancies.
def check_col(rootdim, colpos, colcon, expcon, expdim):
    root = create_root(rootdim)
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
    # pos,      con           children constraints,            [ expcon,       expdim ]

    # child constraints don't affect panel constraints. panel constraints don't affect dim(10,30)
    [ None,     Con(5,10),       [Con(2,8,0,0), Con(3,5,0,0)], [Dim(10,30), Dim(4,30), Dim(6,30)] ],
    [ None,     Con(5,20),       [Con(0,0,0,0), Con(0,0,0,0)], [Dim(10,30), Dim(5,30), Dim(5,30)] ],

    # children dimensions limited by panel constraints
    [ None,     Con(5,10,9,25),  [Con(2,8,3,20), Con(3,5,0,0)], [Dim(9,25), Dim(3,20), Dim(6,25)] ],
    [ None,     Con(5,10,9,25),  [Con(2,8,0,0), Con(2,5,2,20)], [Dim(9,25), Dim(4,25), Dim(2,20)] ],
    [ None,     Con(5,10,9,25),  [Con(2,8,0,0), Con(2,5,0,0)], [Dim(9,25), Dim(4,25), Dim(5,25)] ],

    # children minimum size doesn't fit
    [ None,     Con(3,6,4,25),  [Con(4,8,0,0), Con(4,5,0,0)], [Dim(4,25), Dim(4,25), Dim(0,25)] ],
    [ None,     Con(3,6,5,25),  [Con(4,8,0,0), Con(4,5,0,0)], [Dim(5,25), Dim(4,25), Dim(1,25)] ],
    [ None,     Con(3,6,7,25),  [Con(4,8,0,0), Con(4,5,0,0)], [Dim(7,25), Dim(4,25), Dim(3,25)] ],

    # panel shrinks to fit child constraints
    [ None,     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Dim(9,29), Dim(4,29), Dim(5,28)] ],
    [ None,     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,29)], [Dim(9,29), Dim(4,29), Dim(5,29)] ],

    # Positions
    [ Pos(1,1),     Con(5,10),    [Con(2,8,0,0),  Con(3,5,0,0)],  [Dim(9,29), Dim(4,29), Dim(5,29)] ],

    # position causes panel to shrink
    [ Pos(2,0),     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Dim(8,29), Dim(3,29), Dim(5,28)] ],
    [ Pos(0,2),     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Dim(9,28), Dim(4,28), Dim(5,28)] ],
]

# def test_wide():
# [ Pos(0,2),     Con(12,100,12,100), [Con(5,3,10,6), Con(3,5,5,28)], [Con(5,8,9,29),  Dim(9,29)] ],


def test_layout_vertical():
    for t in FLOW_TESTS_10_30:
        yield check_flow_layout, Orient.VERT, Dim(10, 30), t[0], t[1], t[2], t[3][0], t[3][1:]

# run same tests as test_layout_vertical() by using inverted input.
def test_layout_horizontal():
    for t in FLOW_TESTS_10_30:
        pos = t[0].invert() if t[0] else None
        con = t[1].invert()
        children = list(c.invert() for c in t[2])
        expcon = t[3][0].invert()
        expdims = list(c.invert() for c in t[3][1:])

        yield check_flow_layout, Orient.HORI, Dim(30, 10), pos, con, children, expcon, expdims

def check_flow_layout(orient, dim, pos, con, children_con, exp_pdim, exp_cdims):
    root = RootLayout(dim)
    # root.log('check_flow_layout({}, dim:[{}], pos:[{}], con:[{}], child_con:{})'.format(orient, dim, pos, con, children_con))
    panel = root.panel('root-pan', orient, pos, con)
    for cc in children_con:
        panel.window(None, cc)

    root.do_layout()

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
    root = RootLayout(Dim(15, 100))
    hpan = root.panel('root-panel', Orient.HORI, None, None)

    w1 = hpan.window('w1', Con(4,10,5,20))
    w2 = hpan.window('w2', Con(3,5,8,10))

    w1.initwin(TextWindow, TextModel('model 1', 'window 1'))
    w2.initwin(TextWindow, TextModel('model 2', 'window 2'))
    root.do_layout()
    root.window.paint()
    root.window.doupdate()
    # print_win(root)

    assert root.info.comp_by_name['w1'].name == 'w1'
    assert root.info.comp_by_name['w2'].name == 'w2'
    assert root.info.comp_by_name['root'].name == 'root'
    assert hpan.con == Con(4,15,8,30)

    root.clear_layout()
    assert hpan.con is None

    root.do_layout()
    assert hpan.con == Con(4,15,8,30)

