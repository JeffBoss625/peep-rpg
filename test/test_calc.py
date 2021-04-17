import math
from dataclasses import dataclass
from random import randint
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


def calc_humanoid_area(height):
    width = height/3
    return width*height

def calc_rndshld(diameter):
    return (diameter/2) ** 2 * math.pi

def calc_rectshld(height, width):
    return height * width

def calc_shld_block(shldarea, targetarea):
    area = round(targetarea)
    chance = randint(1, area)
    if chance > shldarea:
        return False
    if chance <= shldarea:
        return True

def where_hit(area, shldarea):      #Which body part did the attack hit?
    head = .0825 * area
    legs = .1675 * area
    torso = .75 * area
    torso = torso - shldarea
    if torso < 0:
        legs = legs + torso
        torso = 0
    totarea = head + legs + torso
    hit = randint(1, totarea)
    if hit <= head:
        return 'head'
    elif hit <= legs+head:
        return 'legs'
    else:
        return 'torso'

def hit_helm():                 #calc if attack hits helmet
    random = randint(1, 100)
    if random > 15:
        return 'helmet'
    else:
        return 'head'

def dmg_multiplier_from_part(where_hit):  #dmg multiplier based on where attack lands
    if where_hit == 'head':
        return 2
    if where_hit == 'torso':
        return 1
    if where_hit == 'legs':
        return .75
    if where_hit == 'helmet':
        return .3
    if where_hit == 'shield':
        return .15

def calc_dmg_multiplier(dst, shield):
    area = calc_humanoid_area(dst.height)
    if shield != 'None':
        if shield.type == 'round':
            shldarea = calc_rndshld(shield.width)
        else:        #shield is rectangular
            shldarea = calc_rectshld(shield.height, shield.width)
        hit = calc_shld_block(area, shldarea)
        if hit:
            part_of_body = where_hit(area, shldarea)
            if part_of_body == 'head':
                part_of_body = hit_helm()          #Did it hit helmet if area of hit is head
            return dmg_multiplier_from_part(part_of_body)
        else:
            return dmg_multiplier_from_part('shield')
    else:
        part_of_body = where_hit(area, 0)       #No shield, so no shld_area
        return dmg_multiplier_from_part(part_of_body)

class target:
    height: int=9

class shield:
    type: str='rect'
    height: int=3
    width: int=3


# def test_calc_dmg_multiplier():
#     print(calc_dmg_multiplier(target, shield))
#     print(calc_dmg_multiplier(target, shield))
#     print(calc_dmg_multiplier(target, shield))
#     print(calc_dmg_multiplier(target, shield))
#     print(calc_dmg_multiplier(target, shield))
