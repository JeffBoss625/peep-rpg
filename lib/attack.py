import random


def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_melee_weapon(src):
    weapons = src['weapons']
    keys = iter(weapons.keys())
    return next(keys)

def attack(src, dst, weapon_name, seed=0):
    src_info = src['peep']      # src original info (name, weapons, original hit points...)
    dst_info = dst['peep']      # dst original info (name, weapons, original hit points...)
    dst_state = dst             # dst current rapidly-changing state (current hit points, position...)
    ret = []
    if seed > 0:
        random.seed(seed)
    ret.append("The " + src_info['name'] + " attacks with " + weapon_name + "!")

    src_weapon = src_info['weapons'][weapon_name]
    if not src_weapon: raise ReferenceError(src_info['name'] + ' has no weapon called' + weapon_name)
    dice_info = parse_dice(src_weapon['damage'])
    tot_hp_loss = 0
    for i in range(1, dice_info['num_dice'] + 1):
        hp_loss = random.randint(1, dice_info['num_sides'])
        # print("i:" + str(i) + " hp_loss:" + str(hp_loss))
        tot_hp_loss += hp_loss
    dst_state['hp'] = dst_state['hp'] - tot_hp_loss
    if dst_state['hp'] <= 0:
        ret.append('the ' + dst_info['name'] + ' has died to the ' + src_info['name'] + "'s " + weapon_name + '!')
    return ret


if __name__ == '__main__':
    print("HERE")
