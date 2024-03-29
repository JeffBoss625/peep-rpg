import random
from dataclasses import dataclass
import lib.calc
from lib.constants import FACING
from lib.items.item import Layer, Properties
from lib.items.physics import striking_blow, Strike, Target
from lib.pclass import STATECLASSES_BY_NAME
from lib.stats import calc_pct


@dataclass
class AttackInfo:
    name: str = ''
    damage: str = '1d1'
    speed: float = 1.0
    range: int = 0
    reach: int = 1.5
    # blowback is multiplied by damage done and applied to attacker. positive causes damage negative
    # *heals* hit points (life drain)
    blowback: float = 0

def parse_dice(dstring):
    parts = dstring.split("d")
    return {
        'num_dice': int(parts[0]),
        'num_sides': int(parts[1])
    }

def choose_attack(src, att_type): #mtrue means melee True or False, False is ranged
    if att_type == 'melee':
        attacks = list(a for a in src.attacks if a.range == 0)
    elif att_type == 'ranged':
        attacks = list(a for a in src.attacks if a.range > 0)
    else:
        raise ValueError(f'unknown attack type: {att_type}')
    a_dmg = 0
    attack = None
    for a in attacks:
        parts = a.damage.split('d')
        d = avg_dmg(int(parts[0]), int(parts[1]))
        if d == a_dmg:
            r = random.randint(1, 100)
            if r > 50:
                a_dmg = d
                attack = a
            else:
                pass
        if d > a_dmg:
            a_dmg = d
            attack = a
    return attack

def calc_hit(ac, thaco):
    chance = thaco - ac
    return random.randint(1, 20) >= chance

def avg_dmg(n, q):
    return n * ((q+1)/2)

# attack dst with src/src_attack.
# return True if the attack hits, False if missed
def attack_dst(src, dst, src_attack, game):
    if src == dst:
        return False
    hit = (calc_hit(dst.ac, src.thaco))
    src._tics = src._tics - 1/src.speed * 1/src_attack.speed
    if hit:
        tot_hp_loss = dice(src_attack, dst)
        # if len(src.body.parts["torso"]) > 0:
        # tot_hp_loss = striking_blow(Strike(area=.1, mass=0.015, velocity=100), Target(Properties([Layer(breaking_pt=10000, hardness=0.8, toughness = 0.2)])))
        # tot_hp_loss *= dmg_multiplier[0]
        # game.message(f'The {dst.name} was hit in the {dmg_multiplier[1]}')
        game.message(f'{src.name} attacks {dst.name} with {src_attack.name}! ({tot_hp_loss} damage)')
        if src.states:
            for s in src.states:
                if s.dmgboost and s.dmgboost != 1.0:
                    tot_hp_loss *= s.dmgboost
                    if src == game.player:
                        game.message(f'You have attacked with {s.dmgboost}x multiplied damage because of your {s.name} ability')
        dst.hp = dst.hp - tot_hp_loss
        if src.aabilities:
            for a in src.aabilities:
                if a.halt_hit is True:
                    state = STATECLASSES_BY_NAME[a.state]
                    states = []
                    for s in src.states:
                        if s.name != state.name:
                            states.append(s)
                        else:
                            game.message(f"You're {a.name} has been deactivated because you hit an enemy")
                            src.states = states
                            src.speed = src.speed - s.speedboost
                    src.states = states
        if dst.hp <= 0:
            if src.shooter:
                game.monster_killed(src.shooter, src_attack, dst)
            else:
                game.monster_killed(src, src_attack, dst)
        else:
            game.message(f'{dst.name} has {round(dst.hp)} points.')
        if src_attack.blowback != 0:
            src.hp = int(src.hp - src_attack.blowback * tot_hp_loss)
            if src.hp <= 0:
                game.message(f'  {src.name} is destroyed')
            if src.hp >= src.maxhp: src.hp = src.maxhp
    else:
        game.message(f'{src.name} missed {dst.name}.')
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

def shield_in_hand(peep):
    in_hand = peep.body.protection('hand')
    for h in in_hand:
        if h == 'Shield':
            return h
    else: return 'None'

def dice(src_attack, dst):
    dice_info = parse_dice(src_attack.damage)
    tot_hp_loss = 0
    for i in range(1, dice_info['num_dice'] + 1):
        hp_loss = random.randint(1, dice_info['num_sides'])
        tot_hp_loss += hp_loss
    if shield_in_hand(dst) != 'None':
        dmg_multiplier = lib.calc.calc_dmg_multiplier(dst, shield_in_hand)
    else:
        dmg_multiplier = lib.calc.calc_dmg_multiplier(dst, 'None')
    return tot_hp_loss

def fire_projectile(monster, player, line_points, mm, ranged_attack):
    path = list(line_points(monster.pos, player.pos))
    mm.create_projectile(monster, ranged_attack.name, path, (ranged_attack.projectile_attack(),))
    monster._tics = monster._tics - 1 / monster.speed * 1 / ranged_attack.speed
    return True


if __name__ == '__main__':
    print("HERE")
