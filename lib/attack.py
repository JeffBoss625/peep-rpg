import random

import lib.calc
from lib.constants import FACING, GAME_SETTINGS
from lib.stat import calc_pct

def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_ranged_attack(src):
    ranged_attacks = []
    for a in src.attacks:
        if a.range > 0:
            ranged_attacks.append(a)
    numattacks = len(ranged_attacks)
    if numattacks == 0:
        return None
    if numattacks == 1:
        return ranged_attacks[0]
    else:
        i = random.randint(1, numattacks-1)
        return ranged_attacks[i]

def choose_melee_attack(src):
    numattacks = len(src.attacks)
    for a in src.attacks:
        if a.range > 0:
            numattacks -= 1
    if numattacks == 0:
        return None
    elif numattacks == 1:
        return src.attacks[0]
    else:
        i = random.randint(1, numattacks-1)
        return src.attacks[i]

def calc_hit(ac, thaco):
    chance = thaco - ac
    return random.randint(1, 20) >= chance

# attack dst with src/src_attack.
# return True if the attack hits, False if missed
def attack_dst(src, dst, src_attack, dungeon):
    if src == dst:
        return False
    dungeon.log(f'attack({src}, {dst}, {src_attack})')
    hit = (calc_hit(dst.ac, src.thaco))
    if hit:
        dice_info = parse_dice(src_attack.damage)
        tot_hp_loss = 0
        for i in range(1, dice_info['num_dice'] + 1):
            hp_loss = random.randint(1, dice_info['num_sides'])
            tot_hp_loss += hp_loss
            if shield_in_hand(dst.inventory):
                if shield_in_hand(dst.inventory) == 0:
                    dmg_multiplier = lib.calc.calc_dmg_multiplier(dst, dst.inventory.hand1)
                elif shield_in_hand(dst.inventory) == 1:
                    dmg_multiplier = lib.calc.calc_dmg_multiplier(dst, dst.inventory.hand2)
                else:
                    dmg_multiplier = 1
            else:
                dmg_multiplier = lib.calc.calc_dmg_multiplier(dst, 'None')
            tot_hp_loss *= dmg_multiplier
        dungeon.message(f'{src.name} attacks {dst.name} with {src_attack.name}! (for {tot_hp_loss} damage)')
        dst.hp = dst.hp - tot_hp_loss
        if dst.hp <= 0:
            dungeon.monster_killed(src, src_attack, dst)
        else:
            dungeon.message(f'  {dst.name} has {round(dst.hp)} points remaining')
        if src_attack.blowback != 0:
            src.hp = int(src.hp - src_attack.blowback * tot_hp_loss)
            if src.hp <= 0:
                dungeon.message(f'  {src.name} is destroyed')
            else:
                # todo: convert arrow into item
                src.speed = 0   # todo: remove remaining moves in turn_seq
                src.attacks = ()
    else:
        dungeon.message(f'the {src.name} missed the {dst.name}')
        return False

# return chance of deflecting a blow
def calc_deflection(defl, skillrat, playerstats, roundto=3):
    ret = defl
    ret = calc_pct(ret, playerstats.str, 0.5)   # strength has 50% impact on deflection
    ret = calc_pct(ret, playerstats.dex)        # dexterity has 100% impact on deflection
    ret = calc_pct(ret, skillrat)               # skill ratio has 100% impact on deflection

    return round(ret, roundto)

def calc_exposure(parts, facing, attack):
    # todo: return a tuple of (attack, exposure, part) for the most vulnerable or accessible part for the attack
    return attack, 1.0, parts[0]

def choose_melee_attack2(src, dst, facing):
    exposures = []
    for attack in src.attacks:
        parts = dst.body.parts_exposed(facing, attack)
        exposures.append(calc_exposure(parts, facing, attack))

    exposures.sort(key=lambda tup: tup[1])
    return exposures[0]


def attack_dst2(src, dst, _attack, out, seed=0):
    # 1. attacker chooses attack and body part(s)
    attack, exposure, part = choose_melee_attack2(src, dst, FACING.FRONT)

    # 2. attacker rolls for hit (agility and skill vs target)


    # 3. hit? defender could not avoid the blow, but attempts to deflect (shield etc)

    # 4. calculate armor deflection, penetration of materials, damage

    # 5. calculate blow-back damage or life-drain/healing

    pass

def peep_regenhp(peepmaxhp, peepspeed, regen_fac):
    speedhealfac = 10 / peepspeed
    amount_heal = peepmaxhp * regen_fac * GAME_SETTINGS.REGEN_RATE
    ret = speedhealfac * amount_heal
    return ret

def shield_in_hand(inventory):
    if inventory.hand1 != 'shield':
        if inventory.hand2 != 'shield':
            return None
        return 1
    else:
        return 0

if __name__ == '__main__':
    print("HERE")
