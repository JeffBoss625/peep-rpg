import math
from random import randint, random


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
    area = round(targetarea)
    chance = random() * area
    if chance > shldarea:
        return True
    if chance <= shldarea:
        return False

def where_hit(peep, shldarea):      #Which body part did the attack hit?
    head =    peep.body.parts['head'][0].size.h  * peep.body.parts['head'][0].size.w
    neck =    peep.body.parts['neck'][0].size.h  * peep.body.parts['neck'][0].size.w
    waist =   peep.body.parts['waist'][0].size.h * peep.body.parts['waist'][0].size.w
    torso =   peep.body.parts['torso'][0].size.h * peep.body.parts['torso'][0].size.w
    arm_r =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w
    arm_l =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w
    wrist_r = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w
    wrist_l = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w
    hand_r =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w
    hand_l =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w
    legs =    peep.body.parts['legs'][0].size.h  * peep.body.parts['legs'][0].size.w
    foot_r =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w
    foot_l =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w
    possible = head + neck + waist + torso + arm_r + arm_l + wrist_r + wrist_l + hand_r + hand_l + legs + foot_r + foot_l
    head =    peep.body.parts['head'][0].size.h  * peep.body.parts['head'][0].size.w
    neck =    peep.body.parts['neck'][0].size.h  * peep.body.parts['neck'][0].size.w + head
    waist =   peep.body.parts['waist'][0].size.h * peep.body.parts['waist'][0].size.w + neck
    torso =   peep.body.parts['torso'][0].size.h * peep.body.parts['torso'][0].size.w + waist
    arm_r =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w + torso
    arm_l =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w + arm_r
    wrist_r = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w + arm_l
    wrist_l = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w + wrist_r
    hand_r =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w + wrist_l
    hand_l =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w + hand_r
    legs =    peep.body.parts['legs'][0].size.h  * peep.body.parts['legs'][0].size.w + hand_l
    foot_r =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w + legs
    foot_l =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w + foot_r
    hit = random() * possible
    torso = torso - shldarea
    if torso < 0:
        arm_r = arm_r + torso
        torso = 0
    if arm_r < 0:
        legs = legs + arm_r
        legs = 0
    if legs < 0:
        legs = 0
    if hit <= head:
        return 'head'
    elif hit <= head:
        return 'head'
    elif hit <= neck:
        return 'neck'
    elif hit <= waist:
        return 'waist'
    elif hit <= torso:
        return 'torso'
    elif hit <= arm_r:
        return 'arm_r'
    elif hit <= arm_l:
        return 'arm_l'
    elif hit <= wrist_r:
        return 'wrist_r'
    elif hit <= wrist_l:
        return 'wrist_l'
    elif hit <= hand_r:
        return 'hand_r'
    elif hit <= hand_l:
        return 'hand_l'
    elif hit <= legs:
        return 'legs'
    elif hit <= foot_r:
        return 'foot_r'
    else:
        return 'foot_l'

def dmg_multiplier_from_part(where_hit, is_armor):  #dmg multiplier based on where attack lands
    dmg_multiplier = 1
    if is_armor:
        dmg_multiplier = 0.5
    if where_hit == "head":
        dmg_multiplier = dmg_multiplier * 2
    if where_hit == "neck":
        dmg_multiplier = dmg_multiplier * 1.85
    if where_hit == "waist":
        dmg_multiplier = dmg_multiplier * 1.3
    if where_hit == "torso":
        dmg_multiplier = dmg_multiplier * 1
    if where_hit == "arm_r":
        dmg_multiplier = dmg_multiplier * .85
    if where_hit == "arm_l":
        dmg_multiplier = dmg_multiplier * .85
    if where_hit == "wrist_r":
        dmg_multiplier = dmg_multiplier * .65
    if where_hit == "wrist_l":
        dmg_multiplier = dmg_multiplier * .65
    if where_hit == "hand_r":
        dmg_multiplier = dmg_multiplier * .3
    if where_hit == "hand_l":
        dmg_multiplier = dmg_multiplier * .3
    if where_hit == "legs":
        dmg_multiplier = dmg_multiplier * .75
    if where_hit == "foot_r":
        dmg_multiplier = dmg_multiplier * .1
    if where_hit == "foot_l":
        dmg_multiplier = dmg_multiplier * .1
    return dmg_multiplier

def calc_dmg_multiplier(dst, shield):
    area = body_area(dst)
    if shield != 'None':
        if shield.type == 'round':
            shldarea = calc_rndshld(shield.width)
        else:        #shield is rectangular
            shldarea = calc_rectshld(shield.height, shield.width)
        hit = calc_shld_block(shldarea, area)
        if hit:
            part_of_body = where_hit(dst, shldarea)
            l_r = None
            if part_of_body == 'arm_r':
                part_of_body = 'arm'
                l_r = 'right'
            elif part_of_body == 'arm_l':
                part_of_body = 'arm'
                l_r = 'left'
            elif part_of_body == 'wrist_r':
                part_of_body = 'wrist'
                l_r = 'right'
            elif part_of_body == 'wrist_l':
                part_of_body = 'wrist'
                l_r = 'left'
            elif part_of_body == 'foot_r':
                part_of_body = 'foot'
                l_r = 'right'
            elif part_of_body == 'foot_l':
                part_of_body = 'foot'
                l_r = 'left'
            elif part_of_body == 'hand_r':
                part_of_body = 'hand'
                l_r = 'right'
            elif part_of_body == 'hand_l':
                part_of_body = 'hand'
                l_r = 'left'
            if dst.body.protection(part_of_body, l_r):
                return (dmg_multiplier_from_part(part_of_body, True), part_of_body)
            else:
                return (dmg_multiplier_from_part(part_of_body, False), part_of_body)
        else:
            return (0.15, 'shield')
    else:
        part_of_body = where_hit(dst, 0)
        l_r = None
        if part_of_body == 'arm_r':
            part_of_body = 'arm'
            l_r = 'right'
        elif part_of_body == 'arm_l':
            part_of_body = 'arm'
            l_r = 'left'
        elif part_of_body == 'wrist_r':
            part_of_body = 'wrist'
            l_r = 'right'
        elif part_of_body == 'wrist_l':
            part_of_body = 'wrist'
            l_r = 'left'
        elif part_of_body == 'foot_r':
            part_of_body = 'foot'
            l_r = 'right'
        elif part_of_body == 'foot_l':
            part_of_body = 'foot'
            l_r = 'left'
        elif part_of_body == 'hand_r':
            part_of_body = 'hand'
            l_r = 'right'
        elif part_of_body == 'hand_l':
            part_of_body = 'hand'
            l_r = 'left'
        if dst.body.protection(part_of_body, l_r):
            return (dmg_multiplier_from_part(part_of_body, True), part_of_body)
        else:
            return (dmg_multiplier_from_part(part_of_body, False), part_of_body)


def body_area(peep):
    head =    peep.body.parts['head'][0].size.h  * peep.body.parts['head'][0].size.w
    neck =    peep.body.parts['neck'][0].size.h  * peep.body.parts['neck'][0].size.w
    waist =   peep.body.parts['waist'][0].size.h * peep.body.parts['waist'][0].size.w
    torso =   peep.body.parts['torso'][0].size.h * peep.body.parts['torso'][0].size.w
    arm_r =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w
    arm_l =   peep.body.parts['arm'][0].size.h   * peep.body.parts['arm'][0].size.w
    wrist_r = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w
    wrist_l = peep.body.parts['wrist'][0].size.h * peep.body.parts['wrist'][0].size.w
    hand_r =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w
    hand_l =  peep.body.parts['hand'][0].size.h  * peep.body.parts['hand'][0].size.w
    legs =    peep.body.parts['legs'][0].size.h  * peep.body.parts['legs'][0].size.w
    foot_r =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w
    foot_l =  peep.body.parts['foot'][0].size.h  * peep.body.parts['foot'][0].size.w
    possible = head + neck + waist + torso + arm_r + arm_l + wrist_r + wrist_l + hand_r + hand_l + legs + foot_r + foot_l
    return possible