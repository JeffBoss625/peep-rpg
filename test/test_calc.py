import math

def distance(p1, p2):
    dis_x = abs(p1[0] - p2[0])
    dis_y = abs(p1[1] - p2[1])
    if dis_x == 0 or dis_y == 0:
        ret = dis_x + dis_y
        return ret
    sq_dis_x = dis_x ** 2
    sq_dis_y = dis_y ** 2
    tobe = sq_dis_x + sq_dis_y
    ret = math.sqrt(tobe)
    return ret

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


def angle(p1, p2):
    radangle = math.atan2(p1[1] - p2[1], p1[0] - p2[0])
    angle = radangle * 180 / math.pi
    if angle < 0:
        angle += 360
    angle -= 90
    if angle < 0:
        angle += 360
    ret = angle
    return ret

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
