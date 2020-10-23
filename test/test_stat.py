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
        (0.3,   0.3,    1.5,    0.2,    1.0,   3,    0.068),
    )
    for defl, skill, weight, str, dex, roundto, exp in data:
        d = calc_deflection(defl, skill, weight, PlayerStats(str=str, dex=dex), roundto=roundto)
        assert d == exp

def test_adjust_stat():
    data = (
        # stat pct  exp
        ( 1.0, 1.0, 1.0 ),
        ( 1.0, 0.5, 1.0 ),
        ( 0.8, 0.5, 0.9 ),
        ( 1.2, 0.5, 1.1 ),
        ( 3.0, 0.5, 2.0 ),
    )
    for stat, pct, exp in data:
        s = adjust_stat(stat, pct)
        assert s == round(exp, 3)

