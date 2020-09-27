import random
import lib.move as mlib
import lib.projectile as ammolib


def create_projectile(direction, model):
    dx, dy = mlib.direction_to_dxdy(direction)
    ammo = ammolib.create_projectile(
        'arrow',
        pos=(model.maze.player.pos[0] + dx, model.maze.player.pos[1] + dy),
        hp=1,
        direct=direction
    )
    model.maze.peeps.append(ammo)

def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_melee_attack(src):
    keys = iter(src.attacks.keys())
    return next(keys)

def calc_hit(ac, thaco, seed = 0):
    if seed > 0:
        random.seed(seed)
    chance = thaco - ac
    die_roll = random.randint(1, 20)
    if die_roll >= chance:
        return True
    else:
        return False

def attack(src, dst, attack_name, out, seed=0):
    out.log('attack({}, {}, {})'.format(src, dst, attack_name))
    if seed > 0:
        random.seed(seed)
    out.message(src.name, "attacks with", attack_name + "!")
    hit = (calc_hit(dst.ac, src.thaco))
    if hit:
        src_attack = src.attacks[attack_name]
        if not src_attack: raise ReferenceError(src.name + ' has no attack called' + attack_name)
        dice_info = parse_dice(src_attack.damage)
        tot_hp_loss = 0
        for i in range(1, dice_info['num_dice'] + 1):
            hp_loss = random.randint(1, dice_info['num_sides'])
            tot_hp_loss += hp_loss
        dst.hp = dst.hp - tot_hp_loss
        if dst.hp <= 0:
            out.message("the {} has died to the {}'s {}!".format(dst.name, src.name, attack_name ))
        if src_attack.blowback != 0:
            bb = src_attack.blowback * tot_hp_loss / 100
            src.hp = src.hp - bb
    else:
        out.message('the {} missed the {}'.format(src.name, dst.name))


if __name__ == '__main__':
    print("HERE")
