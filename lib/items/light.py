from dataclasses import field
from math import sqrt
import doctest
from typing import Tuple

# todo: give peeps and items brightness


class Lightsource:
    def __init__(self, name, brightness, pos):
        self.name = name
        self.brightness = brightness
        self.pos = pos
        self.data = []
    name: str = ''
    brightness: float = 5
    pos: Tuple[int,int] = field(default_factory=tuple)
    def __str__(self):
        return f"light(name: {self.name}, brightness: {self.brightness}, position: {self.pos})"





light_1 = Lightsource(name='jim', brightness=10, pos=[5,4])
light_2 = Lightsource(name='joe', brightness=15, pos=[10,2])
light_3 = Lightsource(name='john', brightness=2, pos=[4,0])
lightsources = [light_1, light_2, light_3]


def light_at(lightsources, pos):
    """
    >>> light_at(lightsources, [0,0])
    [0.24390243902439024, 0.14423076923076925, 0.125]

    """
    pos_x = pos[0]
    pos_y = pos[1]
    brightness = []
    for light in lightsources:
        distance_x = abs(light.pos[0] - pos_x)
        distance_y = abs(light.pos[1] - pos_y)
        tot_distance = sqrt(distance_x ** 2 + distance_y ** 2)
        brightness.append(light.brightness / (tot_distance ** 2))

    return brightness



