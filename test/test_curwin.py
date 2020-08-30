from lib.curwin import *
import sys

def write(s):
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
    root = rootwin(rootdim)
    col = root.panel(Orient.VERT, colpos, colcon)
    root.do_layout()

    ccon = col.con
    assert ccon == expcon
    cdim = col.dim
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

    # Positions
    [ Pos(1,1),     Con(5,10),    [Con(2,8,0,0), Con(3,5,0,0)], [Con(5,10,0,0), Dim(10,30)] ],
    [ Pos(2,0),     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Con(5,8,9,29),  Dim(9,29)] ],
    [ Pos(0,2),     Con(2,3),     [Con(2,8,4,29), Con(3,5,5,28)], [Con(5,8,9,29),  Dim(9,29)] ],
]

def test_layout_vertical():
    for t in FLOW_TESTS:
        yield check_flow_layout, Orient.VERT, Dim(10, 30), t[0], t[1], t[2], t[3][0], t[3][1]

# run same tests as test_layout_vertical() by using inverted input.
def test_layout_horizontal():
    for t in FLOW_TESTS:
        panpos = t[0].invert() if t[0] else None
        pancon = t[1].invert()
        children = list(map(lambda c: c.invert(), t[2]))
        expcon = t[3][0].invert()
        expdim = t[3][1].invert()

        yield check_flow_layout, Orient.HORI, Dim(30, 10), panpos, pancon, children, expcon, expdim

def check_flow_layout(orient, dim, pos, con, children_con, expcon, expdim):
    write('check_flow_layout({}, dim:[{}], pos:[{}], con:[{}], child_con:{})'.format(orient, dim, pos, con, children_con))
    root = rootwin(dim)
    panel = root.panel(orient, pos, con)
    for cc in children_con:
        panel.window(None, cc)
    root.do_layout()
    draw_win(root)


    # pcon = panel.con
    # assert pcon == expcon
    # pdim = panel.dim
    # assert pdim == expdim

# def print_win(v, win, xoff, yoff, depth):
#     print('{}, {}, {}, {}'.format(win, xoff, yoff, depth))

def draw_win(root):
    buf = [x[:] for x in [['.'] * root.dim.w] * root.dim.h]
    root.iterate_win(draw_one_win, buf)
    for i, line in enumerate(buf):
        write("{:<4} {}".format(i, ''.join(line)))

def draw_one_win(win, buf, xoff, yoff, depth):
    write('draw_win({}, off:[{}, {}], depth:{}'.format(win, xoff, yoff, depth))
    if not win.conf.border:
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

def render_curses(win, v, xoff, yoff, depth):
    write('render_curses({}, off:[{}, {}], depth:{}'.format(win, xoff, yoff, depth))
    win.data = win.winparent.data.derwin(win.dim.h, win.dim.w, win.pos.y, win.pos.x)
    if win.conf.border:
        win.data.border()
    return v

def test_paint():
    root = rootwin(Dim(12, 40))
    c1 = root.panel(Orient.VERT)

    w1 = c1.window('W1', Con(3, 8, 5, 0))
    r1 = w1.panel(Orient.HORI)
    w2 = r1.window('W2', Con(5, 5, 5, 5))
    w3 = r1.window('W3', Con(3, 3, 3, 7))

    c2 = c1.panel(Orient.VERT)
    w4 = c2.window('W4', Con(3, 7, 3, 8))
    w5 = c2.window('W5')

    root.do_layout()

    # rwin =
#     dim = Dim(12,40)
#     scr = Scr(None, Pos(), dim)
#     root = rootwin(scr)
#     root.dim = dim
#     # mainrow = root.addrow()
#     # mainrow.addwin(Con(8,4,8))
#     # mainrow.addwin(Con(4,4,6,5))
#     # mainrow.addwin(Con())
#
#     c1 = root.panel(Orient.VERT)
#
#     w1 = c1.window(Con(3, 8, 5, 0))
#     r1 = w1.panel(Orient.HORI)
#     w2 = r1.window(Con(5, 5, 5, 5))
#     w3 = r1.window(Con(3, 3, 3, 7))
#
#     c2 = c1.panel(Orient.VERT)
#     w4 = c2.window(Con(3, 7, 3, 8))
#     w5 = c2.window()
#
#     root.do_layout()
#
#     root.paint()
#     scr.refresh()
#
#     for line in scr.buflines():
#         print(line)

