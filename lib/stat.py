# Stats naturally range from 0.33 to 3.00 (1/3 to 3 times competent level) for human population with the very limits
# being at 3.0 and incompetency below 0.3, 5 being legendary/heroic unheard of. We call this the 5-range scale
# because that is where values will range for humanoids (though gods and beasts values can go to the 50's and
# perhaps higher - at those levels, the intelligence/dexterity/strength becomes hard to even comprehend.
# Strength is measured relative to body weight where 1.0 is ability to lift 1.5 times body-weight. Smaller classes
# like dwarves who are compact but lighter than humans will have higher strength values (1.8 average).
# A beast with mass of 15.0 and strength of 1.0
# will have a true strength to lift 15 humans. (multiply strength by body mass to create effective strength).
#
# Player stats are work on a floating scale where 99.9% of human values range between 0.33 and 3.0 and where 1.0 is
# the most common/normal value representing competent/normal human (male). Values below 1 represent percentage
# off normal so 0.5 would be half of normal strength/intelligence etc. 0.33 would be on third, 1.5 50% above
# average, 3.0 is three times average etc.
#
# Values at 3.0 are at peak human levels of olympic champion strength, super-rare genius etc,
# a result of one in one hundred thousand innate talent combined with intesensive training.
# For intelligence, 3.0 represents super-rare genius, for dexterity it is freakeshly fast and agile, for
# constitution it is Rasputin-like resistance to poisons and wounds.
#
#                                                                           human limit
#  lowest-possible                                                       olympic champion
#    |        very-low     competent      high       very-high             super-genius         demi-god        god
#    |            |            |           |             |                       |                   |           |
#   0.1          0.5   0.75   1.0         1.5           2.0        2.5          3.0       ...   10.0  ...   20.0   ...
#                        |                                          |                    |        |
#                       low                                    extremely-high            |    Beowolf
#                                                                                   super-human
#                                                                                  heroic/legendary
#                                                                                   Gilgamesh
#
#   rarity:
#    |    0.1%    3%    15%    30%        15%            3%       0.1%        0.00001%      xxx legend-only xxx...
#    |
#   0.000001% - minimum functional value is 0.1, below which is not possible or is
#               unworkable
#                   strength - cannot move
#                   dexterity - cannot control movement
#                   intelligence - can't think
#                   constitution - can't stop a fit of uncontrollable coughing at a damp breeze
#                   wisdom - greet and attempt to befriend a raging umber hulk
#                   charisma - repulsive in many ways. can't possibly be any less charasmatic
#                   ...
#
# Where 1.0 is normal-competent, human stats are generally range 0.1..3.0* ranging from extremely deficient
# to heroic (strength to lift 4.5 times body weight, dexterity 3 times faster than most fit humans). Above 3.0 is
# super-human, 5 to 10 times human is demigod and 20-50 is
# godlike where a 300 lb being would lift 9,000-22,500 lbs. - the weight of one or two african bull elephants or react
# 20 times faster than a normal human.

from random import random, randint
from dataclasses import dataclass, astuple

@dataclass
class HarmStats:
    pierce: float = 0
    slash: float = 0
    crush: float = 0
    heat: float = 0
    cold: float = 0
    acid: float = 0
    elec: float = 0

    def __repr__(self):
        return f'prc:{self.pierce:0.3f} sla:{self.slash:0.3f} cru:{self.crush:3.3f} ' \
               f'hea:{self.heat:0.3f} col:{self.cold:0.3f} aci:{self.acid:0.3f} ele:{self.elec:0.3f}'


@dataclass
class PlayerStats:
    # average strength lifting varies by training from lifting 80% of one's weight to almost 350% (a 4X difference)
    # strength varies by nature and by training and profession
    # 1.0 is strength of an average man who is active and lightly trained and can lift 1.5 x his weight.
    # 0.5 is the strength of a human without conditioning or training (deadlift 75% of bodyweight)
    # 0.3 is quite weak, lifting less than half of body weight
    # 0.1 is sickly, lifting only 15% of bodyweight
    # 2.0 is extremely strong, deadlifting 3x bodyweight
    # 3.0 begins heroic strength
    # 5.0 is truly heroic, legendary strength - a 200lb man dead lifting 1500lbs! (world record for deadlift is 425 lb man lifting 1,100 lbs)
    str: float = 1.0

    # intelligence combines multiple traits of intelligence, including intuition, knowledge, quick-wittedness,
    # perception, cunning... it represents all these things in different measures for different characters.
    # 1.0 is intelligence of a somewhat thoughtful human who has had some studies/schooling, but nothing intensive.
    # 0.5 is intelligence of an unschooled human who doesn't have tendency to think much.
    # 0.3 is unusually slow and/or unobservant who has a hard time figuring out most puzzles/tricks/challenges.
    # 0.1 is truly limited in understanding and cannot learn all but the simple things. For example, may simply
    #     bang rocks together or go around bashing things with a heavy club.
    # 2.0 is a very clever and highly studied person
    # 3.0 is true genius intelligence and very rare
    # 5.0 is unheard of demi-god like intelligence and perceptiveness. this level of intelligence sees through
    #     almost any challenge, scheme or puzzle like child's play.
    int: float = 1.0

    wis: float = 1.0

    # agility, reflexes, speed and awareness
    # 1.0 is dexterity of an average human with lightly honed reflexes.
    # 0.5 is dexterity of a clumsy individual who is slow to pick up techniques and skills and does not react quickly
    #     to attacks
    # 0.3 is a noticeably slow and clumsy human. such a person would have little chance of evading an average attack
    #     and would be easy to anticipate when defending against
    # 0.1 is terribly slow and clumsy and would have to be incredibly lucky to land a physical blow against a normal
    #     person
    # 2.0 is a very highly trained and/or gifted individual who anticipates and evades and strikes with excellent skill
    # 3.0 is return-of-the dragon Bruce Lee. Incredibly hard to hit or block.
    # 5.0 is heroic/legendary approaching spidey-sense and reflexes.
    dex: float = 1.0
    con: float = 1.0
    cha: float = 1.0

# adjust the percentage relative to percentage off 1.0 norm using the stat scale (0.1 to 5.0 ... 20.0 (gods)... range)
def calc_pct(pct, stat, statadj=1.0):
    if stat == 1.0 or pct == 1.0:
        return pct

    if statadj != 1.0:
        stat = adjust_stat(stat, statadj)

    r1 = pct * stat
    r2 = 1 - (1 - pct)/stat
    if 0.0001 < r2 < r1:
        ret = r2
    else:
        ret = r1

    return ret

# adjust a stat that is centered/oriented at 1.0 as the norm by the given percentage (above or below norm).
def adjust_stat(stat, adj, norm=1.0):
    if stat == norm:
        return stat
    if stat < norm and adj > 1.0:
        return stat / adj                   # amplify weakness
    else:
        return norm + (stat - norm) * adj   # reduce weakness

def roll_dice(dstring):
    parts = dstring.split("d")
    ndice = int(parts[0])
    nsides = int(parts[1])
    ret = 0
    for i in range(1, ndice + 1):
        ret += randint(1, nsides)
    return ret
