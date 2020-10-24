from lib.stat import *

def test_calc_deflection():
    data = (
        # defl, skill   weight  str     dex    round, exp
        #       ratio   ratio
        (0.5,   1.0,    1.0,    1.0,    1.0,   3,    0.5),
        (0.5,   1.5,    1.0,    1.0,    1.0,   3,    0.667),
        (0.5,   1.0,    1.5,    1.0,    1.0,   3,    0.6),
        (0.5,   1.0,    1.0,    1.5,    1.0,   3,    0.6),
        (0.5,   1.0,    1.0,    1.0,    1.5,   3,    0.667),

        (0.5,   1.5,    1.5,    1.0,    1.0,   3,    0.733),
        (0.5,   1.0,    1.5,    1.5,    1.0,   3,    0.68),
        (0.5,   1.0,    1.0,    1.5,    1.5,   3,    0.733),

        (0.5,   1.5,    1.5,    1.5,    1.0,   3,    0.787),
        (0.5,   1.0,    1.5,    1.5,    1.5,   3,    0.787),

        (0.5,   1.5,    1.5,    1.5,    1.5,   3,    0.858),

        (0.3,   1.5,    1.5,    1.5,    1.5,   3,    0.764),

        (0.3,   3.0,    1.5,    0.2,    2.0,   3,    0.817),
        (0.3,   3.0,    1.5,    0.2,    1.0,   3,    0.675),
        (0.3,   0.3,    1.5,    0.2,    1.0,   3,    0.067),
    )
    for defl, skill, weight, str, dex, roundto, exp in data:
        d = calc_deflection(defl, skill, weight, PlayerStats(str=str, dex=dex), roundto=roundto)
        assert d == exp

def test_adjust_stat():
    data = (
        # stat pct  exp
        ( 1.0, 1.0, 1.0 ),
        ( 1.0, 0.5, 1.0 ),

        ( 0.5, 1.0, 0.5 ),
        ( 0.5, 0.2, 0.9 ),
        ( 0.5, 0.5, 0.75 ),
        ( 0.5, 1.5, 0.333 ),
        ( 0.5, 2.0, 0.25 ),
        ( 0.5, 3.0, 0.167 ),

        ( 0.8, 0.5, 0.9 ),


        ( 1.2, 0.5, 1.1 ),
        ( 2.0, 0.5, 1.5 ),
        ( 3.0, 0.3, 1.6 ),
        ( 3.0, 0.5, 2.0 ),
        ( 3.0, 0.9, 2.8 ),

        ( 3.0, 1.5, 4.0 ),
        ( 3.0, 2.0, 5.0 ),
        ( 3.0, 3.0, 7.0 ),
    )
    for stat, pct, exp in data:
        s = round(adjust_stat(stat, pct), 3)
        assert s == exp

def test_calc_pct():
    data = (
        # pct    stat   statadj    exp
        ( 1.0,   1.0,   1.0,       1.0 ),
        ( 1.0,   0.5,   1.0,       1.0 ),
        ( 1.0,   1.0,   0.5,       1.0 ),

        ( 0.5,   1.0,   0,         0.5 ),
        ( 0.5,   0.5,   0,         0.25 ),
        ( 0.5,   1.5,   0,         0.667 ),
        ( 0.5,   1.5,   0.5,       0.6 ),
    )
    for pct, stat, statadj, exp in data:
        if statadj:
            p = calc_pct(pct, stat, statadj)
        else:
            p = calc_pct(pct, stat)

        p = round(p, 3)
        assert p == exp

