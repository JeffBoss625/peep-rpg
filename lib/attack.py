import random


def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }


def attack(src, dst, weapon_name, seed=0):
    src_orig = src['peep']      # src original state (name, weapons, original hit points...)
    dst_orig = dst['peep']      # dst original state (name, weapons, original hit points...)
    dst_cur = dst               # dst current rapidly-changing state (current hit points, position...)
    ret = []
    if seed > 0:
        random.seed(seed)
    ret.append("The " + src_orig['name'] + " attacks with " + weapon_name + "!")

    src_weapon = src_orig['weapons'][weapon_name]
    if not src_weapon: raise ReferenceError(src_orig['name'] + ' has no weapon called' + weapon_name)
    dice_info = parse_dice(src_weapon['damage'])
    tot_hp_loss = 0
    for i in range(1, dice_info['num_dice'] + 1):
        hp_loss = random.randint(1, dice_info['num_sides'])
        # print("i:" + str(i) + " hp_loss:" + str(hp_loss))
        tot_hp_loss += hp_loss
    dst_cur['hp'] = dst_cur['hp'] - tot_hp_loss
    ret.append('the ' + dst_orig['name'] + ' has ' + str(dst_cur['hp']) + 'hp left!')
    if dst_cur['hp'] <= 0:
        ret.append('the ' + dst_orig['name'] + ' has died to the ' + src_orig['name'] + "'s " + weapon_name + '!')
    return ret


if __name__ == '__main__':
    print("HERE")
