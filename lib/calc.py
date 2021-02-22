import math
from random import randint


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
        if t.pos != src_peep.pos and t.hp > 0 and t.type != 'wall':    #is targetable
            dis = distance(src_peep.pos, t.pos)
            ang = angle (src_peep.pos, t.pos)
            tuples.append((dis, ang, t))
    tuples.sort()
    return list(t[2] for t in tuples)

def calc_humanoid_area(height):
    width = height/3
    return width*height

def calc_rndshld(diameter):
    return (diameter/2) ** 2 * math.pi

def calc_rectshld(height, width):
    return height * width

def calc_shld_block(shldarea, targetarea):
    chance = randint(1, targetarea)
    if chance > shldarea:
        return False
    if chance >= shldarea:
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
        return dmg_multiplier_from_part(where_hit)
