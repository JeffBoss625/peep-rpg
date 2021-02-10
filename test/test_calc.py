import math

from lib.calc import angle, distance

def test_distance():
    data = (
        ([0, 0], [1, 0], 1),
        ([0, 0], [0, 1], 1),
        ([0, 0], [1, 1], 1.41),
        ([0, 0], [2, 0], 2),
        ([0, 0], [0, 2], 2),
        ([0, 0], [2, 2], 2.83),
        ([2, 2], [2, 0], 2),
        ([2, 2], [4, 2], 2),
        ([2, 2], [2, 4], 2),
        ([2, 2], [0, 2], 2),
        ([2, 2], [4, 4], 2.83),
        ([2, 2], [0, 0], 2.83),
        ([2, 2], [4, 0], 2.83),
        ([2, 2], [0, 4], 2.83),
        ([0, 0], [3, 2], 3.61),
        ([0, 0], [5, 7], 8.6),
    )
    for p1, p2, exp in data:
        lc = round(distance(p1, p2), 2)
        # print(f'distance({p1}, {p2}) = {lc} (expected {exp})')
        assert lc == exp

def test_angle():
    data = (
        ([1, 1], [1, 0], 0),
        ([1, 1], [2, 0], 45),
        ([1, 1], [2, 1], 90),
        ([1, 1], [2, 2], 135),
        ([1, 1], [1, 2], 180),
        ([1, 1], [0, 2], 225),
        ([1, 1], [0, 1], 270),
        ([1, 1], [0, 0], 315),
        ([1, 15], [0, 0], 356.19),
        ([1, 15], [2, 0], 3.81),
    )
    for p1, p2, exp in data:
        lc = round(angle(p1, p2), 2)
        # print(f'angle({p1}, {p2}) = {lc} (expected {exp})')
        assert lc == exp


def target_list(positions, origin):
    list = []
    for i, p in enumerate(positions):
        dis = distance(origin, p)
        ang = angle (origin, p)
        list.append((dis, ang, i))
    list.sort()
    return list

def test_target_list():
    data = (
        ([(0, 0), (1, 1), (3, 3), (4, 4), (7, 8), (9, 10), (0, 5), (5, 0)], [0, 0], 0),
    )
    for positions, origin, exp in data:
        lc = target_list(positions, origin)
        print(f'target_list({positions}, {origin}) = {lc} (expected {exp})')
        # assert lc == exp
