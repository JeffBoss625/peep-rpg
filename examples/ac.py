import random


def calc_hit(ac, thaco, seed = 0):
    if seed > 0:
        random.seed(seed)
    chance = thaco - ac
    die_roll = random.randint(1, 20)
    print('chance: ', chance, 'die_roll: ', die_roll)
    if die_roll >= chance:
        return True
    else:
        return False

for i in range (50):
    print(calc_hit(6, 18, i + 1))