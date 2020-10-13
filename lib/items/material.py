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
    unit_thickness_mm: float = 0

def mtype_by_name():
    data = (
        ('metal', 0.2),
        ('wood', 3),
        ('leather', 0.5),
        ('wicker', 0.5),
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
        # material   type       color          unit_mm, g/cm3  (pier, slas, crus, heat, cold, elec)
        ('mithril',  'metal',   COLOR.BLUE,    1.00,  1.950, (0.40, 0.35, 0.40, 0.80, 0.80, 0.75)),
        ('titanium', 'metal',   COLOR.BLUE,    1.00,  4.480, (0.45, 0.40, 0.45, 0.75, 0.75, 0.65)),
        ('steel',    'metal',   COLOR.BLUE,    1.00,  7.900, (0.55, 0.45, 0.55, 0.80, 0.80, 0.65)),  # modern high-grade steel
        ('bronze',   'metal',   COLOR.YELLOW,  1.00,  8.800, (0.60, 0.50, 0.60, 0.85, 0.80, 0.90)),  # weapon-grade bronze (work-hardened high-tin content)
        ('iron',     'metal',   COLOR.BLUE,    1.00,  7.680, (0.65, 0.55, 0.65, 0.90, 0.85, 0.80)),  # worked iron
        ('leather',  'leather', COLOR.RED,     1.00,  0.980, (0.80, 0.65, 0.93, 0.30, 0.30, 0.25)),  # soft leather
        ('cotton',   'cloth',   COLOR.WHITE,   0.20,  0.180, (0.96, 0.93, 0.97, 0.55, 0.55, 0.55)),
        ('flax',     'cloth',   COLOR.WHITE,   0.20,  0.150, (0.94, 0.91, 0.98, 0.70, 0.70, 0.55)),  # light strong fabric
        ('wool',     'cloth',   COLOR.WHITE,   2.00,  0.150, (0.96, 0.94, 0.95, 0.30, 0.30, 0.40)),  # warm loose fabric
        ('felt',     'cloth',   COLOR.WHITE,   2.00,  0.220, (0.87, 0.89, 0.75, 0.35, 0.35, 0.40)),  # warm, thick, buffering fabric
        ('wicker',   'wicker',  COLOR.WHITE,   1.50,  0.210, (0.90, 0.80, 0.80, 0.60, 0.60, 0.50)),
        ('oak',      'wood',    COLOR.RED,     4.00,  0.900, (0.65, 0.55, 0.65, 0.40, 0.40, 0.40)),  # heavy oak
        ('pine',     'wood',    COLOR.RED,     4.00,  0.550, (0.80, 0.60, 0.80, 0.45, 0.45, 0.45)),
    )
    ret = {}
    for name, mtype, fgcolor, grams_cm3, prot in data:
        ret[name] = Material(name, mtype, fgcolor, grams_cm3, Protection(*prot))
    return ret

def durability():
    data = (
        # material   (pier, slas, crus, heat, cold, elec)
        (
            'mithril',
            (0.03, 0.35, 0.40, 0.80, 0.80, 0.75),
            (0.40, 0.35, 0.40, 0.80, 0.80, 0.75),
        ),
        ('titanium', (0.45, 0.40, 0.45, 0.75, 0.75, 0.65)),
        ('steel',    (0.55, 0.45, 0.55, 0.80, 0.80, 0.65)),  # modern high-grade steel
        ('bronze',   (0.60, 0.50, 0.60, 0.85, 0.80, 0.90)),  # weapon-grade bronze (work-hardened high-tin content)
        ('iron',     (0.65, 0.55, 0.65, 0.90, 0.85, 0.80)),  # worked iron
        ('leather',  (0.80, 0.65, 0.93, 0.30, 0.30, 0.25)),  # soft leather
        ('cotton',   (0.96, 0.93, 0.97, 0.55, 0.55, 0.55)),
        ('flax',     (0.94, 0.91, 0.98, 0.70, 0.70, 0.55)),  # light strong fabric
        ('wool',     (0.96, 0.94, 0.95, 0.30, 0.30, 0.40)),  # warm loose fabric
        ('felt',     (0.87, 0.89, 0.75, 0.35, 0.35, 0.40)),  # warm, thick, buffering fabric
        ('wicker',   (0.90, 0.80, 0.80, 0.60, 0.60, 0.50)),
        ('oak',      (0.65, 0.55, 0.65, 0.40, 0.40, 0.40)),  # heavy oak
        ('pine',     (0.80, 0.60, 0.80, 0.45, 0.45, 0.45)),
    )
    ret = {}
    for name, mtype, fgcolor, grams_cm3, prot in data:
        ret[name] = Material(name, mtype, fgcolor, grams_cm3, Protection(*prot))
    return ret

MAT_BY_NAME = mat_by_name()


@dataclass
class Construction:
    name: str = ''
    mat: Tuple = field(default_factory=tuple)
    weight_fac: float = 0
    prot_fac: Tuple = field(default_factory=tuple)


def constructs():
    data = {
        # mass factor is the amount of material used for a given unit of the material.
        # Protection factors of the multiple materials may add up to surpass the materials
        # individual protection - meaning that they are better in synergy.
        # name
        #  (materials, ...), massf, (pierce, slash, crush, heat, cold, elec)
        'quilt': (
            (
                ('cloth',), 0.40,
                (0.40, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00),
                (0.95, 0.10, 0.15, 1.00, 1.00, 2.00, 1.00),     # durability factor
            ),
            (('cloth',), 0.20, (0.25, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),
            (('cloth',), 0.40, (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),
        ),
        'bound-wood': (
            # wood planks wrapped in cloth or leather with strong resin
            (('wood')),
            (('cloth', 'leather'), 0.40, (0.40, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),

        ),
        'hard-leather': (
            #  (materials, ...), massf,
            (
                ('leather',) ,1.20,
                # pier, slas, crus, heat, cold, elec
                (1.50, 1.90, 3.00, 1.20, 1.20, 1.10),
                (2.00, 2.50, 0.10, 1.20, 0.50, 1.00),       # damage factor
            ),
        ),
        'rim': (
            # some construction, such as shields can add a rim of enforcement to protect against slashing
        ),
        'chain': (
            (('metal',), 0.50, (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),
        ),
        'lamellar': (
            (('metal', 'ceramic', 'shell'), 0.65, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
            (('leather', 'cloth'), 0.35, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
        ),
        'brigandine': (
            (('metal', 'hard-leather'), 0.85, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
            (('leather', 'cloth'), (0.35, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
        ),
        'splint': (
             (('metal', 'wood'), 0.60, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
             (('leather', 'cloth'), 0.45, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
         ),
        'scale': (
            (('metal', 'shell', 'scale'), 0.80, (0.70, 0.85, 0.70, 1.00, 1.00, 0.85, 1.00)),
            (('leather', 'cloth'),       0.30, (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00)),
        ),
        'mirror': (
            (('metal', 'shell', 'hard-leather', 'wood'), 0.65, (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00)),
        ),
        'plate': (
           (('metal', 'shell', 'hard-leather'), 1.00, (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00)),
        ),
    }
    ret = {}
    for name, constructs in data:
        for materials, weight_fac, prot in constructs:
            ret[name] = Construction(name, weight_fac, prot)
    return ret

def construct_by_name():
    prot = (
        # name         weight_fac (pierce, slash, crush, heat, cold, elec)
        ('chain',      0.50,      (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00) ),
        ('lamellar',   0.75,      (0.55, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00) ),
        ('brigandine', 0.75,      (0.65, 0.80, 0.70, 1.00, 1.00, 0.80, 1.00) ),
        ('scale',      0.80,      (0.70, 0.85, 0.70, 1.00, 1.00, 0.85, 1.00) ),
        ('splint',     0.80,      (0.70, 0.85, 0.70, 1.00, 1.00, 0.85, 1.00) ),
        ('plate',      1.00,      (1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00) ),    # solid metal plate
        ('quilt',      1.00,      (0.50, 0.75, 0.15, 1.00, 1.00, 2.00, 1.00) ),
    )

    comp = {
        'chain': (
            ('metal', 1.0),
        ),
        'lamellar': (
            ('metal', 0.30),
            ('leather', 0.70),
        )
    }




CONSTRUCTS = constructs()
@dataclass
class Layer:
    material: str = ''
    construction: str = ''
    thick_mm: int = 0

    def __post_init__(self):
        mat = MAT_BY_NAME[self.material]
        mtype = MTYPE_BY_NAME[mat.type]
        con = METAL_CONSTRUCTS[self.construction]
        self.grams_cm2 = mat.grams_cm3 * (self.thick_mm / 10) * con.weight_fac
        thick_unit = self.thick_mm/mtype.unit_thickness_mm
        thick = pow(thick_unit, pow(1.04, thick_unit))
        mprot = astuple(mat.prot)
        prot = (1 - ((1 - p * fac)/thick) for p, fac in zip(mprot, con.prot_fac))
        self.prot = Protection(*tuple(prot))

    def __str__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction}'

    def __repr__(self):
        return f'{self.thick_mm}mm {self.material} {self.construction} {self.grams_cm2:0.3f} g/cm2 {self.prot}'

# calculate protection factor
#   uexposure: vulnerability from one layer. inverse of protection (1 - protection percent)
#   nlayers: number of layers of the material
def calc_prot_layers(uexposure, nlayers):
    if nlayers == 1:
        return round(uexposure, 3)

    for i in range(2, int(nlayers+1)):
        uexposure -= uexposure / i

    if int(nlayers) != nlayers:
        frac = nlayers - int(nlayers)
        uexposure -= (frac * (uexposure / nlayers))
    return round(uexposure, 3)

# return the extra stopping factor that results from combining layers
#   nlayers: number of layers (unit size per material type)
#   slow_compound: compounding factor of slowing a projectile
#   slow_log_base: compounding logarithm rate. e.g. 1.5 will compound slowing for every 50% increase in thickness. 2
#       will compound for every doubling of thickness
#   exp: accelerates compounding to add more rapid asymptotic stopping of damage
def stop_factor(nlayers, compound=0.98, log_base=1.5, exponent=2):
    return (compound ** (math.log(nlayers, log_base))) ** (nlayers * exponent)

# calculate the exposure of
def merge_different_layers(e1, e2):
    if e1 > e2:
        hi, lo = e1, e2
    else:
        hi, lo = e2, e1

    return round(hi - lo/2, 3)

class TestFn:
    def __init__(self, v):
        self.x = v

    def handler(self, a, b):
        return (a + b) * self.x


if __name__ == '__main__':
    for mname in MAT_BY_NAME:

        for cname in METAL_CONSTRUCTS:
            for mm in range(1, 12):
                layer = Layer(mname, cname, mm)
                print(repr(layer))

