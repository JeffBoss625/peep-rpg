import random
from lib.stat import calc_pct


def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_melee_attack(src):
    numattacks = len(src.attacks)
    if numattacks == 0:
        return None
    elif numattacks == 1:
        return src.attacks[0]
    else:
        i = random.randint(1, numattacks-1)
        return src.attacks[i]

def calc_hit(ac, thaco, seed=0):
    if seed > 0:
        random.seed(seed)
    chance = thaco - ac
    return random.randint(1, 20) >= chance

def attack_dst(src, dst, src_attack, out, seed=0):
    out.log(f'attack({src}, {dst}, {src_attack})')
    if seed > 0:
        random.seed(seed)
    hit = (calc_hit(dst.ac, src.thaco))
    if hit:
        dice_info = parse_dice(src_attack.damage)
        tot_hp_loss = 0
        for i in range(1, dice_info['num_dice'] + 1):
            hp_loss = random.randint(1, dice_info['num_sides'])
            tot_hp_loss += hp_loss
        out.message(f'{src.name} attacks {dst.name} with {src_attack.name}! (for {tot_hp_loss} damage)')
        dst.hp = dst.hp - tot_hp_loss
        if dst.hp <= 0:
            out.message(f"the {dst.name} has died to the {src.name}'s {src_attack.name}!")
        else:
            out.message(f'  {dst.name} has {dst.hp} points remaining')
        if src_attack.blowback != 0:
            src.hp = int(src.hp - src_attack.blowback * tot_hp_loss)
            if src.hp <= 0:
                out.message(f'  {src.name} is destroyed')
            else:
                # todo: convert arrow into item
                src.speed = 0   # todo: remove remaining moves in turn_seq
                src.attacks = ()
    else:
        out.message(f'the {src.name} missed the {dst.name}')
        if src.type is 'projectile':
            src.pos = (src.pos[0] + src.direct[0], src.pos[1] + src.direct[1])

# return chance of deflecting a blow
def calc_deflection(defl, skillrat, playerstats, roundto=3):
    ret = defl
    ret = calc_pct(ret, playerstats.str, 0.5)   # strength has 50% impact on deflection
    ret = calc_pct(ret, playerstats.dex)        # dexterity has 100% impact on deflection
    ret = calc_pct(ret, skillrat)               # skill ratio has 100% impact on deflection

    return round(ret, roundto)

def calc_hit2(src, dst, attack, out, seed=0):

    pass


if __name__ == '__main__':
    print("HERE")
