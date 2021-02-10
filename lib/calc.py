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

# src_peep is the peep from which target distances are calculated. targets is a list of objects with .pos attributes.
def target_list(src_peep, targets):
    tuples = []
    for t in targets:
        if t.pos != src_peep.pos and t.hp > 0:
            dis = distance(src_peep.pos, t.pos)
            ang = angle (src_peep.pos, t.pos)
            tuples.append((dis, ang, t))
    tuples.sort()
    return list(t[2] for t in tuples)
