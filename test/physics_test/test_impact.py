import doctest
from dataclasses import dataclass, field
from typing import List, Any

# some materials will be strong and hard, but not rigid. Or rigid and strong, but not hard.

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
    durability: float = 100
    pierce_area: float = 1.0       # area of the object as it pierces through ie. arrow gets thicker as it goes further in.

@dataclass
class Piece:
    layer: List[Layer] = field(default_factory=list)

@dataclass
class Target:
    armor: List[Piece] = field(default_factory=list)


person = Target([Piece([Layer(200, 2, 40, 100000, 90000, 0.3, .9), Layer(50, 2, 40, 500000, 500000, 0.6, 0.1)])])
hammer = Strike(velocity=40, area=5, mass= 50)

force_theshold = 1000

def apply_crush(strike, layer, f_per_cm):
    if f_per_cm > layer.plastic_region:
        layer.durability = layer.durability - 10 * (f_per_cm/layer.breaking_pt)
    strike.velocity = strike.velocity - layer.elasticity/250 * (strike.velocity * (2/3))
    strike.area = strike.area + (layer.elasticity/250) * (layer.area/4)
    return strike, layer

def calc_damage(force):
    output = (force ** 1.3)/3500
    return output


def striking_blow(strike, target):
    if len(target.armor) > 0:
        for layer in target.armor[0].layer:
            f_per_cm = ((strike.mass * (strike.velocity ** 2)) / 2) / layer.area
            if pierceable(strike, layer):
                strike, layer = apply_pierce(strike, layer, f_per_cm)
            else:
                strike, layer = apply_crush(strike, layer, f_per_cm)
    f = (strike.mass * (strike.velocity ** 2)) / 2
    f_per_cm = f/strike.area
    if f_per_cm > force_theshold:
        return calc_damage(f_per_cm)
    else:
        return 0


def apply_pierce(strike, layer, f_per_cm):
    strike.velocity = strike.velocity - layer.pierce_res * layer.thickness ** 2
    layer.durability -= 3
    return strike, layer

def pierceable(strike, layer):
    """
    >>> pierceable(Strike(area=.1, mass=0.015, velocity=150), Layer(breaking_pt=10000, hardness=0.9))
    True
    >>> pierceable(Strike(area=.1, mass=0.015, velocity=150), Layer(breaking_pt=10000, hardness=0.1))
    True
    >>> pierceable(Strike(area=16, mass=4.52, velocity=50), Layer(breaking_pt=10000, hardness=0.9))
    False
    >>> pierceable(Strike(area=16, mass=4.52, velocity=50), Layer(breaking_pt=10000, hardness=0.1))
    False
    """
    f_per_cm = ((strike.mass * (strike.velocity ** 2)) / 2) / strike.area ** 2
    print(f'f_per_cm: {f_per_cm}')
    print(f'piercable: {layer.breaking_pt * (layer.hardness ** 2)}')
    if f_per_cm > layer.breaking_pt * (layer.hardness ** 2):
        return True
    return False


if __name__ == '__main__':
    doctest.testmod()
    # striking_blow(hammer, person)