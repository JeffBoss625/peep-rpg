from dataclasses import dataclass

from lib.items.item import Item, FitInfo
from lib.model import register_yaml, Size

# todo: add material and calculate weight

# Full suite of plate 15-25 kg, jousting armor could be twice that
# “An entire suit of field armor (that is, armor for battle) usually weighs between 45 and 55 lbs. (20 to 25 kg),
# with the helmet weighing between 4 and 8 lbs. (2 to 4 kg)—less than the full equipment of a fireman with oxygen gear,
# or what most modern soldiers have carried into battle since the nineteenth century.
# https://www.sarahwoodbury.com/medieval-swords-and-armor-were-not-heavy/#:~:text=%E2%80%9CAn%20entire%20suit%20of%20field,battle%20since%20the%20nineteenth%20century.

AVERAGE_HELM_SIZE = Size(0.133, 0.10, 0.09) # average human head height is 2/15 of total height or 0.133 units
AVERAGE_HELM_THICK = 0.5 / 175
AVERAGE_HELM_WEIGHT = 3 / 65

# Armor that covers the body and is 'fitted' is normalized at the fit of an average male of 175 cm height and
# normal girth:
#   height=1.0, (tallness)
#   width=1.0,  (shoulder width and head size)
#   depth=1.0,  (fatness)
#
# These three measures make up the body-type of a humanoid. Implied with that body type are different proportions,
# so a very tall measure will infer a relatively smaller head because of the shoulder-to-height ratio.
# This is to make construction of all equipment for a body-type more convenenient.
# Armor fit for a tall thin sodier could be created:
#   armor.jacket(1.2, 1.0, 0.8)     - a long thin jacket (normal shoulder width)
#   armor.boots(1.2, 1.0, 0.8)      - boots fitting a long and narrow foot.
#   armor.helm(1.2, 1.0, 0.8)       - a helm fitting a tall thin person
#
# So a Titan of human proportions could be expressed:
#   2.0, 2.0, 2.0
@dataclass
class Helm(Item):
    name: str = 'helm'
    char: str = '^'
    fit_info: FitInfo = FitInfo('cover', 'fitted', 'head')

# depth is the thickness of material
def helm(h=1.0, w=1.0, d=1.0, thick=1.0):
    ret = Helm()
    ret.size = AVERAGE_HELM_SIZE.copy(h, w, d)
    ret.thick = thick * AVERAGE_HELM_THICK
    vol = ret.thick * ret.size.cover_area()
    avol = AVERAGE_HELM_THICK * AVERAGE_HELM_SIZE.cover_area()
    ret.weight = AVERAGE_HELM_WEIGHT * (vol/avol)

    return ret

@dataclass
class Boots(Item):
    name: str = 'boots'
    char: str = '['
    fit_info: FitInfo = FitInfo('cover', 'fitted', 'foot')

# height relates to foot length
# width relates to foot width
# depth relates to
def boots(h=1.0, w=1.0, d=1.0):
    # average human head height is 2/15 of total height or 0.133 units
    ret = Boots()
    ret.size = Size(h * 0.090, w * 0.060, d * 0.167)
    return ret

@dataclass
class Shield(Item):
    name: str = 'shield'
    char: str = ')'
    fit_info: FitInfo = FitInfo('held', 'held', 'hand')
    shape = 'round'


# averages in human units
AVERAGE_SHIELD_WEIGHT = 2.5 / 65                    # 2.5 kg / 65 kg.
AVERAGE_SHIELD_THICK = 0.75 / 65
AVERAGE_SHIELD_SIZE = Size(0.48, 0.40, 0.061)       # 84 cm x 70 cm x 4 cm

# shield width and height is expressed relative to average human male height (175 cm, about 5ft 9 inches).
#   Viking large round shield:      105cm diameter (.866 sq m), 0.6 cm thick, 4.5 kg
#   Round greek aspis:               90cm diameter (.636 sq m), 3 cm thick, 7.3 kg
#   Viking small round shield:       70cm diameter (.385 sq m), 1.2 cm thick, 3.0 kg (guess)
#
# Depth is the curvature of the shield
#   Roman Scutum (square plywood curving around)  100 cm x 40cm x 30cm (0.60 sq m), 0.6 cm thick, 6-8 kg
#
# Kite (70% of square)
#   Small 'heater' shield:   70cm x 55cm (70% of sq area = .269 sq m), 2 kg
#   large Kite shield:      115cm x 75cm (70% of sq area = .604 sq m), 6.5 kg
#
# Conversions:
# 116cm = 0.66 units
# 105cm = 0.60 units
#  91cm = 0.52 units
#  70cm = 0.40 units
#  53cm = 0.30 units
#
# when we implement materials:
#
#   3.500cm = 0.2 units     very thick
#   1.750cm = 0.1 units
#   1.225cm = 0.007 units
#   0.700cm = 0.004 units
#   0.525cm = 0.003 units   very thin (large area shields)
#
# Average Human Shield is 84cm x 70cm (0.48 x 0.40)
# A very tall shield would be 119 cm (0.68)
def shield(size=Size(1.0,1.0,1.0), thick=1.0, **params):
    ret = Shield(**params)
    ret.size = AVERAGE_SHIELD_SIZE.copy(size.h, size.w, size.d)
    ret.thick = thick * AVERAGE_SHIELD_THICK
    vol = ret.size.h * ret.size.w * ret.thick   # todo: factor in curvature of shield (d)
    avol = AVERAGE_SHIELD_SIZE.h * AVERAGE_SHIELD_SIZE.w * AVERAGE_SHIELD_THICK
    ret.weight = AVERAGE_SHIELD_WEIGHT * (vol/avol)
    return ret


register_yaml((Helm,Shield))

# if __name__ == '__main__':
# s = Shield(layers=(Layer('iron', 'plate', 2), Layer('oak', 'plate', 10)))
# print(yaml.dump(s, sort_keys=False))

