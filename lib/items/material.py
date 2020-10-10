from dataclasses import dataclass, field, astuple
from typing import Tuple

from lib.constants import COLOR


@dataclass
class Protection:
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


class MAT:
    MITHRIL =   'mithril'
    TITANIUM =  'titanium'
    STEEL =     'steel'     # modern high-grade steel
    BRONZE =    'bronze'    # weapon-grade brass (work-hardened high-tin content)
    IRON =      'iron'
    LEATHER =   'leather'
    OAK =       'oak'
    PINE =      'pine'


@dataclass
class Material:
    name: str = ''
    fgcolor: str = COLOR.BLUE
    grams_cm3: float = 0        # grams per cm^3
    prot: Protection = field(default=MAT.MITHRIL)

def mat_by_name():
    data = (
        ('mithril',  COLOR.BLUE,   1.950, (0.80, 0.90, 0.70, 0.15, 0.15, 0.45, 0.45)),
        ('titanium', COLOR.BLUE,   4.480, (0.70, 0.85, 0.60, 0.70, 0.70, 0.35, 0.25)),
        ('steel',    COLOR.BLUE,   7.900, (0.60, 0.80, 0.55, 0.70, 0.70, 0.25, 0.15)),  # modern high-grade steel
        ('bronze',   COLOR.YELLOW, 8.800, (0.50, 0.70, 0.50, 0.50, 0.50, 0.20, 0.20)),  # weapon-grade brass (work-hardened high-tin content)
        ('iron',     COLOR.BLUE,   7.680, (0.45, 0.65, 0.45, 0.50, 0.50, 0.20, 0.80)),
        # ('leather',  COLOR.WHITE,  0.980, (0.10, 0.20, 0.50, 0.40, 0.40, 0.25, 0.40)),  # oiled leather
        # ('oak',      COLOR.RED,    0.900, (0.25, 0.35, 0.35, 0.50, 0.50, 0.40, 0.50)),
        # ('pine',     COLOR.RED,    0.550, (0.15, 0.20, 0.20, 0.50, 0.50, 0.35, 0.50)),
    )
    ret = {}
    for name, fgcolor, grams_cm3, prot in data:
        ret[name] = Material(name, fgcolor, grams_cm3, Protection(*prot))
    return ret


MAT_BY_NAME = mat_by_name()


@dataclass
class Construction:
    mat: str = ''
    weight_fac: float = 0
    prot_fac: Tuple = field(default_factory=tuple)

def construct_by_name():
    data = (
        # name    weight_fac (pierce, slash, crush, heat, cold, elec)
        ('chainmail', 0.50, (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),
        ('lamellar',  0.75, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
        ('scalemail', 0.80, (0.70, 0.85, 0.70, 1.00, 1.00, 0.85, 1.00)),
        ('platemail', 1.00, (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00)),
    )
    ret = {}
    for name, weight_fac, prot in data:
        ret[name] = Construction(name, weight_fac, prot)
    return ret


CON_BY_NAME = construct_by_name()


@dataclass
class Layer:
    material: str = ''
    construction: str = ''
    thick_mm: int = 0

    def __post_init__(self):
        mat = MAT_BY_NAME[self.material]
        con = CON_BY_NAME[self.construction]
        self.grams_cm2 = mat.grams_cm3 * (self.thick_mm / 10) * con.weight_fac
        thick = pow(self.thick_mm, pow(1.04, self.thick_mm))
        mprot = astuple(mat.prot)
        prot = (1 - ((1 - p * fac)/thick) for p, fac in zip(mprot, con.prot_fac))
        self.prot = Protection(*tuple(prot))

    def __str__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction}'

    def __repr__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction} {self.grams_cm2:0.3f} g/cm2 {self.prot}'


if __name__ == '__main__':
    for cname in CON_BY_NAME:
        for mname in MAT_BY_NAME:
            for mm in range(1, 12):
                layer = Layer(mname, cname, mm)
                print(repr(layer))

