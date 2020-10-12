from lib.items.material import *


def test_calc_layer_prot():
    tests = (
        (0.48, 1, 0.48),
        (0.48, 2, 0.24),
        (0.48, 3, 0.16),
        (0.48, 4, 0.12),
        (0.48, 5, 0.096),
        (0.48, 6, 0.08),
    )
    for uexposure, nlayers, exp in tests:
        res = calc_prot_layers(uexposure, nlayers)
        assert res == exp

def test_stop_factor():
    tests = (
        (1, 0.98, 1.5, 2, 1.0),
        (2, 0.98, 1.5, 2, 0.871),
        (3, 0.98, 1.5, 2, 0.72),
        (4, 0.98, 1.5, 2, 0.575),
        (5, 0.98, 1.5, 2, 0.448),
        (6, 0.98, 1.5, 2, 0.343),
        (7, 0.98, 1.5, 2, 0.257),
        (8, 0.98, 1.5, 2, 0.191),
        (9, 0.98, 1.5, 2, 0.139),

        (1, 0.98, 1.5, 4, 1.0),
        (2, 0.98, 1.5, 4, 0.759),
        (3, 0.98, 1.5, 4, 0.518),
        (4, 0.98, 1.5, 4, 0.331),
        (5, 0.98, 1.5, 4, 0.201),
        (6, 0.98, 1.5, 4, 0.117),
        (7, 0.98, 1.5, 4, 0.066),
        (8, 0.98, 1.5, 4, 0.036),
        (9, 0.98, 1.5, 4, 0.019),
    )
    for nlayers, compound, log_base, exponent, exp in tests:
        res = stop_factor(nlayers, compound=compound, log_base=log_base, exponent=exponent)
        res = round(res, 3)
        assert res == exp

def test_merge_different_layers():
    tests = (
        (0.48, 0.48, 0.24 ),
        (0.48, 0.24, 0.36 ),
        (0.48, 0.16, 0.4  ),
        (0.48, 0.12, 0.42 ),
        (0.48, 0.09, 0.435),
        (0.48, 0.08, 0.44 ),
    )
    for e1, e2, exp in tests:
        res = merge_different_layers(e1, e2)
        assert res == exp
