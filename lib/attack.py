import random


def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }


def attack(src, dst, weapon_name, seed=0):
    ret = []
    if seed > 0:
        random.seed(seed)
    ret.append("The " + src['name'] + " attacks with " + weapon_name + "!")
    weapon = src['weapons'][weapon_name]
    if not weapon: raise ReferenceError(src['name'] + ' has no weapon called' + weapon_name)
    dice_info = parse_dice(weapon['damage'])
    tot_hp_loss = 0
    for i in range(1, dice_info['num_dice'] + 1):
        hp_loss = random.randint(1, dice_info['num_sides'])
        # print("i:" + str(i) + " hp_loss:" + str(hp_loss))
        tot_hp_loss += hp_loss
    health_left = dst['hp'] - tot_hp_loss
    ret.append('the ' + dst['name'] + ' has ' + str(health_left) + 'hp left!')
    if health_left <= 0:
        ret.append('the ' + dst['name'] + ' has died to the ' + src['name'] + "'s " + weapon_name + '!')
    return ret


if __name__ == '__main__':
    print("HERE")
