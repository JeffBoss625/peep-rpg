import math
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
class MatType:
    name: str = ''
    unit_thickness: int = 0

def mtype_by_name():
    data = (
        ('metal', 1),
        ('wood', 20),
        ('leather', 5),
    )
    ret = {}
    for name, base_thickness in data:
        ret[name] = MatType(name, base_thickness)
    return ret


MTYPE_BY_NAME = mtype_by_name()


@dataclass
class Material:
    name: str = ''
    type: str = ''
    fgcolor: str = COLOR.BLUE
    grams_cm3: float = 0        # grams per cm^3
    prot: Protection = field(default=MAT.MITHRIL)

def mat_by_name():
    data = (
        ('mithril',  'metal', COLOR.BLUE,   1.950, (0.80, 0.90, 0.70, 0.15, 0.15, 0.45, 0.45)),
        ('titanium', 'metal', COLOR.BLUE,   4.480, (0.70, 0.85, 0.60, 0.70, 0.70, 0.35, 0.25)),
        ('steel',    'metal', COLOR.BLUE,   7.900, (0.60, 0.80, 0.55, 0.70, 0.70, 0.25, 0.15)),  # modern high-grade steel
        ('bronze',   'metal', COLOR.YELLOW, 8.800, (0.50, 0.70, 0.50, 0.50, 0.50, 0.20, 0.20)),  # weapon-grade brass (work-hardened high-tin content)
        ('iron',     'metal', COLOR.BLUE,   7.680, (0.45, 0.65, 0.45, 0.50, 0.50, 0.20, 0.80)),
        ('leather',  'leather', COLOR.WHITE,  0.980, (0.10, 0.20, 0.50, 0.40, 0.40, 0.25, 0.40)),  # oiled leather
        ('oak',      'wood', COLOR.RED,    0.900, (0.25, 0.35, 0.35, 0.50, 0.50, 0.40, 0.50)),
        ('pine',     'wood', COLOR.RED,    0.550, (0.15, 0.20, 0.20, 0.50, 0.50, 0.35, 0.50)),
    )
    ret = {}
    for name, mtype, fgcolor, grams_cm3, prot in data:
        ret[name] = Material(name, mtype, fgcolor, grams_cm3, Protection(*prot))
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
        ('plate', 1.00, (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00)),    # placeholder for normal layer over shields...
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
        mtype = MTYPE_BY_NAME[mat.type]
        con = CON_BY_NAME[self.construction]
        self.grams_cm2 = mat.grams_cm3 * (self.thick_mm / 10) * con.weight_fac
        thick_unit = self.thick_mm/mtype.unit_thickness
        thick = pow(thick_unit, pow(1.04, thick_unit))
        mprot = astuple(mat.prot)
        prot = (1 - ((1 - p * fac)/thick) for p, fac in zip(mprot, con.prot_fac))
        self.prot = Protection(*tuple(prot))

    def __str__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction}'

    def __repr__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction} {self.grams_cm2:0.3f} g/cm2 {self.prot}'

# calculate protection factor
# base: inverse of protection (1 - protection percent)
# nlayers: number of layers of the material
# slow_compound: compounding factor of slowing a projectile
# slow_log_base: compounding logarithm rate. e.g. 1.5 will compound slowing for every 50% increase in thickness. 2
#    will compound for every doubling of thickness
def layer_protection(base, nlayers, slow_compound, slow_log_base):
    if nlayers == 1:
        return round(base * 100, 3)
    xtra = (slow_compound ** (math.log(nlayers, slow_log_base))) ** (nlayers*4)
    for i in range(2, int(nlayers+1)):
        base -= base / i

    if int(nlayers) != nlayers:
        frac = nlayers - int(nlayers)
        base -= (frac * (base/nlayers))
    return round(base * xtra * 100, 3)


if __name__ == '__main__':
    # for cname in CON_BY_NAME:
    #     for mname in MAT_BY_NAME:
    #         for mm in range(1, 12):
    #             layer = Layer(mname, cname, mm)
    #             print(repr(layer))

    for i in range(1, 11):
        print(f'i:{i} result:{layer_protection(0.22, i, 0.98, 1.5)}')

    for i in (1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2, 2.1, 2.1):
        print(f'i:{i} result:{layer_protection(0.22, i, 0.98, 1.5)}')

    # print('result:', layer_protection2(0.48, 10))