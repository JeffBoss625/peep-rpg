import doctest
from dataclasses import dataclass, field
from typing import List, Any

# some materials will be strong and hard, but not rigid. Or rigid and strong, but not hard.

NORMAL_HUMAN_HP = 100

@dataclass
class Strike:
    velocity: float = 1.0
    area: float = 1.0
    mass: float = 1.0

@dataclass
class Layer:
    elasticity: float = 1.0
    thickness: float = 1.0
    area: float = 1.0
    breaking_pt: float = 1.0
    plastic_region: float = 1.0
    toughness: float = 1.0          # holds together and friction like felt
    hardness: float = 1.0
    durability: float = 1.0

@dataclass
class Properties:
    layer: List[Layer] = field(default_factory=list)

@dataclass
class Target:
    properties: Properties = None


person = Target(Properties([Layer(200, 2, 40, 100000, 90000, 0.3, .9), Layer(50, 2, 40, 500000, 500000, 0.6, 0.1)]))
hammer = Strike(velocity=40, area=5, mass= 50)

force_theshold = 1000

def apply_crush(strike, layer, f_per_cm):
    if f_per_cm > layer.plastic_region:
        layer.durability = layer.durability - 0.1 * (f_per_cm/layer.breaking_pt)
    strike.velocity = strike.velocity - layer.elasticity * (strike.velocity * (2/3))
    strike.velocity = max(0, strike.velocity)
    strike.area = strike.area + layer.elasticity * (layer.area/4)
    strike.area = max(layer.area/4, strike.area)
    return strike, layer

def calc_damage(force, strike):

    output = (force ** 1.3)/1000
    if strike.area <= .2:
        max_output = .33 * NORMAL_HUMAN_HP
        if output > max_output:
            output = max_output
    else:
        output *= strike.area
    return output


def striking_blow(strike, target):
    """
    # >>> striking_blow(Strike(area=.1, mass=0.015, velocity=100), Target(Properties([Layer(breaking_pt=10000, hardness=0.8, toughness = 0.2)])))
    #
    # >>> striking_blow(Strike(area=.1, mass=0.015, velocity=100), Target(Properties([Layer(breaking_pt=10000, hardness=0.9, toughness = 0.2)])))
    #
    # >>> striking_blow(Strike(area=16, mass=0.1, velocity=50), Target(Properties([Layer(breaking_pt=10000, hardness=0.8, toughness = 0.2)])))

    >>> striking_blow(Strike(velocity=40, area=5, mass= 50), Target(Properties([Layer(.75, 2, 40, 100000, 90000, 0.3, .9)])))
    """
    for layer in target.properties.layers:
        f_per_cm = ((strike.mass * (strike.velocity ** 2)) / 2) / strike.area
        if strike.velocity <= 0:
            return 0
        pierce = pierceable(strike, layer)
        if pierce == "pierce":
            print("pierce")
            strike, layer = apply_pierce(strike, layer, f_per_cm)
        elif pierce == "stop":
            print("no pierce")
            strike, layer = apply_crush(strike, layer, f_per_cm)
        else:
            strike.velocity = 0
    f = (strike.mass * (strike.velocity ** 2)) / 2
    f_per_cm = f/strike.area
    print(f"damage: {calc_damage(f_per_cm, strike)}")
    if f_per_cm > force_theshold:
        return calc_damage(f_per_cm, strike)
    else:
        return 0


def apply_pierce(strike, layer, f_per_cm):
    strike.velocity = (strike.velocity * (strike.mass * 100)) - (layer.toughness * strike.velocity) / (1 / layer.thickness)
    strike.velocity = max(0, strike.velocity)
    layer.durability -= .02
    return strike, layer

def pierceable(strike, layer):
    """
    # >>> pierceable(Strike(area=.1, mass=0.015, velocity=100), Layer(breaking_pt=10000, hardness=0.9))
    # "stop"
    # >>> pierceable(Strike(area=.1, mass=0.015, velocity=100), Layer(breaking_pt=10000, hardness=0.1))
    # "pierce"
    # >>> pierceable(Strike(area=16, mass=0.1, velocity=50), Layer(breaking_pt=10000, hardness=0.9))
    # "stop"
    # >>> pierceable(Strike(area=16, mass=0.1, velocity=50), Layer(breaking_pt=10000, hardness=0.1))
    # "pierce"
    """
    f_per_cm = ((strike.mass * (strike.velocity ** 2)) / 2) / strike.area ** 2
    print(f'f_per_cm: {f_per_cm}')
    print(f'piercable: {layer.breaking_pt * (layer.hardness ** 2)}')
    if f_per_cm > layer.breaking_pt * (layer.hardness ** 2):
        return "pierce"
    return "stop"
    # return "glance"    #for blows that were glanced off


if __name__ == '__main__':
    doctest.testmod()
    # striking_blow(hammer, person)