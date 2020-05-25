import random


def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_melee_attack(src):
    keys = iter(src.attacks.keys())
    return next(keys)

def attack(src, dst, attack_name, seed=0):
    ret = []
    if seed > 0:
        random.seed(seed)
    ret.append("The " + src.name + " attacks with " + attack_name + "!")

    src_attack = src.attacks[attack_name]
    if not src_attack: raise ReferenceError(src.name + ' has no attack called' + attack_name)
    dice_info = parse_dice(src_attack.damage)
    tot_hp_loss = 0
    for i in range(1, dice_info['num_dice'] + 1):
        hp_loss = random.randint(1, dice_info['num_sides'])
        # print("i:" + str(i) + " hp_loss:" + str(hp_loss))
        tot_hp_loss += hp_loss
    dst.hp = dst.hp - tot_hp_loss
    ret.append('the ' + dst.name + ' has ' + str(dst.hp) + 'hp left!')
    if dst.hp <= 0:
        ret.append('the ' + dst.name + ' has died to the ' + src.name + "'s " + attack_name + '!')
    return ret


if __name__ == '__main__':
    print("HERE")
