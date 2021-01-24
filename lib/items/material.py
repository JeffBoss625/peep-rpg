import math
from dataclasses import dataclass, field, astuple
from typing import Tuple

from lib.stat import HarmStats, PlayerStats


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
    fgcolor: str = 'blue'
    grams_cm3: float = 0        # grams per cm^3
    durability: int = 0
    defl: HarmStats = None  # deflect
    pen: HarmStats = None   # penetrate
    mdam: HarmStats = None  # material damage

def mat_by_name():
    data = (
        # material   type       color    unit_mm, g/cm3  durability
        ('mithril',  'metal',   'blue',    1.00,  1.950, 1000000),
        ('titanium', 'metal',   'blue',    1.00,  4.480,  100000),
        ('steel',    'metal',   'blue',    1.00,  7.900,   50000),  # modern high-grade steel
        ('bronze',   'metal',   'yellow',  1.00,  8.800,   30000),  # weapon-grade bronze (work-hardened high-tin content)
        ('iron',     'metal',   'blue',    1.00,  7.680,   20000),  # worked iron
        ('hard-leather', 'leather', 'red', 1.00,  1.100,   11000),
        ('oak',      'wood',    'red',     4.00,  0.900,   10000),  # heavy oak
        ('pine',     'wood',    'red',     4.00,  0.550,    5000),
        ('leather',  'leather', 'red',     1.00,  0.980,    5000),  # soft leather
        ('wicker',   'wicker',  'white',   1.50,  0.210,    1100),
        ('felt',     'cloth',   'white',   2.00,  0.220,    4000),  # warm, thick, buffering fabric
        ('flax',     'cloth',   'white',   0.20,  0.150,    1500),  # light strong fabric
        ('cotton',   'cloth',   'white',   0.20,  0.180,    1000),
        ('wool',     'cloth',   'white',   2.00,  0.150,    1500),  # warm loose fabric
        # ('gold',     'metal',   'yellow',  1.00, 19.280,   15000),
    )
    ret = {}
    for name, mtype, fgcolor, grams_cm3, unit_mm, dur in data:
        defl = DEFL_BY_NAME[name]
        pen = PEN_BY_NAME[name]
        mdam = MDAM_BY_NAME[name]
        ret[name] = Material(name, mtype, fgcolor, grams_cm3, dur, defl, pen, mdam)
    return ret

# chance of a blow to pierce/slash/burn/freeze through the armor
def penetration():
    data = {
        # name          (pier, slas, crus, heat, cold, acid, elec)
        'mithril':      (0.40, 0.35, 0.40, 0.80, 0.80, 0.25, 0.75),
        'titanium':     (0.45, 0.40, 0.45, 0.75, 0.75, 0.30, 0.65),
        'steel':        (0.55, 0.45, 0.55, 0.80, 0.80, 0.33, 0.65),
        'bronze':       (0.60, 0.50, 0.60, 0.85, 0.80, 0.37, 0.93),
        'iron':         (0.65, 0.55, 0.65, 0.90, 0.85, 0.40, 0.80),
        'hard-leather': (0.80, 0.75, 0.80, 0.85, 0.85, 0.45, 0.90),
        'leather':      (0.90, 0.85, 0.90, 0.90, 0.85, 0.55, 0.98),
        'wicker':       (0.90, 0.80, 0.80, 0.60, 0.60, 0.60, 0.50),
        'cotton':       (0.65, 0.55, 0.65, 0.40, 0.40, 0.75, 0.40),
        'flax':         (0.80, 0.60, 0.80, 0.45, 0.45, 0.75, 0.45),
        'wool':         (0.80, 0.65, 0.92, 0.30, 0.30, 0.65, 0.25),
        'felt':         (0.87, 0.89, 0.70, 0.35, 0.35, 0.60, 0.40),
        'oak':          (0.94, 0.91, 0.96, 0.80, 0.80, 0.40, 0.55),
        'pine':         (0.98, 0.95, 0.96, 0.75, 0.75, 0.50, 0.55),
    }
    return {name: HarmStats(pen) for name, pen in data.items()}

# base chance of deflecting some or part of a blow without any damage (higher deflects more)
def deflection():
    data = {
        # name              (pier, slas, crus, heat, cold, acid, elec)
        'mithril':          (0.45, 0.50, 0.45, 0.20, 0.20, 0.20, 0.30),
        'titanium':         (0.40, 0.45, 0.40, 0.20, 0.20, 0.20, 0.35),
        'steel':            (0.36, 0.40, 0.36, 0.18, 0.18, 0.18, 0.25),
        'bronze':           (0.33, 0.38, 0.33, 0.17, 0.17, 0.17, 0.20),
        'iron':             (0.30, 0.35, 0.30, 0.16, 0.16, 0.16, 0.18),
        'hard-leather':     (0.24, 0.28, 0.20, 0.18, 0.18, 0.18, 0.30),
        'oak':              (0.25, 0.31, 0.25, 0.12, 0.20, 0.20, 0.30),
        'pine':             (0.20, 0.24, 0.20, 0.10, 0.18, 0.18, 0.27),
        'leather':          (0.04, 0.06, 0.05, 0.15, 0.15, 0.15, 0.30),
        'wicker':           (0.05, 0.08, 0.05, 0.04, 0.11, 0.11, 0.15),
        'cotton':           (0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.15),
        'flax':             (0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.15),
        'wool':             (0.02, 0.03, 0.02, 0.40, 0.40, 0.40, 0.40),
        'felt':             (0.03, 0.04, 0.03, 0.40, 0.40, 0.40, 0.40),
    }
    return dict({name: data[name] for name in data})

# damage sustained by material when a blow pierces/slashes/burns through (higher is more damage)
def pen_damage():
    data = {
        # name              (pier, slas, crus, heat, cold, acid, elec)
        'mithril':          (0.30, 0.25, 0.35, 0.05, 0.08, 0.30, 0.05),
        'titanium':         (0.30, 0.25, 0.35, 0.10, 0.10, 0.30, 0.05),
        'steel':            (0.30, 0.25, 0.35, 0.10, 0.10, 0.30, 0.05),
        'bronze':           (0.30, 0.25, 0.35, 0.15, 0.10, 0.30, 0.05),
        'iron':             (0.30, 0.25, 0.35, 0.20, 0.10, 0.30, 0.05),
        'hard-leather':     (0.30, 0.28, 0.15, 0.70, 0.20, 0.30, 0.05),
        'oak':              (0.20, 0.10, 0.85, 0.90, 0.30, 0.20, 0.40),
        'pine':             (0.25, 0.15, 0.85, 0.95, 0.30, 0.25, 0.45),
        'leather':          (0.25, 0.30, 0.02, 0.80, 0.20, 0.25, 0.05),
        'wicker':           (0.15, 0.80, 0.80, 1.00, 0.30, 0.15, 0.50),
        'cotton':           (0.20, 0.75, 0.02, 0.85, 0.10, 0.20, 0.05),
        'flax':             (0.20, 0.75, 0.02, 0.85, 0.10, 0.20, 0.05),
        'wool':             (0.10, 0.75, 0.02, 0.85, 0.10, 0.10, 0.05),
        'felt':             (0.15, 0.75, 0.02, 0.75, 0.10, 0.15, 0.15),
    }
    return {name: HarmStats(dam) for name, dam in data.items()}

# damage sustained by material for portion of thrust/slash/flame... that is absorbed (non-penetrating damage)
# todo: calculate relative to metal base, cloth base, wood base, ...
def abs_damage():
    data = {
        # name              (pier, slas, crus, heat, cold, acid, elec)
        'mithril':          (0.02, 0.01, 0.01, 0.01, 0.01, 0.02, 0.01),
        'titanium':         (0.03, 0.02, 0.03, 0.02, 0.02, 0.03, 0.02),
        'steel':            (0.04, 0.05, 0.04, 0.03, 0.03, 0.04, 0.03),
        'bronze':           (0.06, 0.07, 0.06, 0.04, 0.04, 0.06, 0.04),
        'iron':             (0.07, 0.08, 0.07, 0.05, 0.05, 0.07, 0.05),
        'hard-leather':     (0.11, 0.11, 0.11, 0.40, 0.30, 0.11, 0.10),
        'leather':          (0.13, 0.15, 0.02, 0.80, 0.20, 0.13, 0.05),
        'cotton':           (0.80, 0.90, 0.01, 0.90, 0.90, 0.80, 0.90),
        'flax':             (0.80, 0.75, 0.01, 0.90, 0.90, 0.80, 0.90),
        'wool':             (0.75, 0.75, 0.01, 0.85, 0.84, 0.75, 0.85),
        'felt':             (0.50, 0.75, 0.01, 0.75, 0.10, 0.50, 0.15),
        'wicker':           (0.20, 0.25, 0.95, 0.95, 0.30, 0.20, 0.50),
        'oak':              (0.10, 0.10, 0.70, 0.50, 0.20, 0.10, 0.20),
        'pine':             (0.20, 0.15, 0.85, 0.60, 0.20, 0.20, 0.20),
    }
    return {name: HarmStats(dam) for name, dam in data}


DEFL_BY_NAME = deflection()
PEN_BY_NAME = penetration()
MDAM_BY_NAME = pen_damage()
MAT_BY_NAME = mat_by_name()

def constructs():
    data = {
        # mass factor is the amount of material used for a given unit of the material.
        # Protection factors of the multiple materials may add up to surpass the materials
        # individual protection - meaning that they are better in synergy.
        # name
        'quilted': {
            # (materials, ...),                  massf   thick_min, thick_max
            'mat': (
                (('cotton', 'flax',),            1.0,    1.0,    2.0),
                (('cloth',),                     1.0,    1.0,    2.0),        # any cloth (felt, wool...)
                (('cotton', 'flax'),             1.0,    1.0,    2.0),
            ),
        },
        # wood planks wrapped in cloth or leather with strong resin
        'leather-bound-wood': {
            'mat': (
                (('leather',),  1.0, 1.0, 2.5,),
                (('wood',),                      1.0, 1.0, 3.0,),
            ),
            # name      (pier, slas, crus, heat, cold, elec)
            'pen':      (0.7, 0,8, 0.8, 0.9, 0.9, 0.9),
            'defl':     (),
            'dam':      (0.8, 0.8, 0.7, 0.9, 0.9, 1.0),
        },
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
#   exponent: accelerates compounding to add more rapid asymptotic stopping of damage
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

@dataclass
class AttackStats:
    # speed normalized to 10 meters per second (about 22 mph).
    speed: float = 1.0
    # a collective measure of the attack's accuracy, how well the attacker anticipates/overcomes defensive moves etc.
    skill: float = 1.0
    # Intensity:
    # an elite javilin thrower launches a 800 gram javilin at 100 km/h (62 mph)
    # a professional baseball player can swing a 1 kg bat at rougly 113 km/h (70 mph). Exit velocity of the ball can reach 100 mph.
    # a scimitar weighs about 1.8 kg
    # a longsword weighs 1-1.5 kg on average
    # for pierce, slash and crush, a value of 1.0 represents 10 kilogram meters per second. (equivalent of 2.2 lbs striking at 22 mph)
    #    1.0 represents 1 kg striking at 22 mph
    #    2.0 represetns 1 kg striking at 44 mph
    #    3.0 represents 1 kg striking at 66 mph
    #    5.0 represents 1 kg striking at over 100 mph - an heroic strike
    # for heat, cold, elec... it is the intensity (jouls, amps), etc.
    intensity: HarmStats = field(default_factory=HarmStats)

@dataclass
class Armor:
    name: str = ''
    dur: int = 0
    mass: float = 0
    mat: Tuple = field(default_factory=tuple)
    defl: HarmStats = field(default_factory=HarmStats)
    # pene: HarmStats = field(default_factory=HarmStats)
    # absdam: HarmStats = field(default_factory=HarmStats)
    # pendam: HarmStats = field(default_factory=HarmStats)

@dataclass
class DefendStats:
    skill: float = 1.0                  # combination of experience, combat training, reflex training, observation, spidy-sense...
    playerstats: PlayerStats = field(default_factory=PlayerStats)
    # item_familiarity: float = 1.0     # improved handling from familiarity defending with a shield, sword, bracers....
    # item_bonus: float = 1.0

# Where 1.0 is normal-competent, human stats are generally range 0.1..3.0* ranging from extremely deficient
# to heroic (strength to lift 4.5 times body weight, dexterity 3 times faster than most fit humans). Above 3.0 is
# super-human, 5 to 10 times human is demigod and 20-50 is
# godlike where a 300 lb being would lift 9,000-22,500 lbs. - the weight of one or two african bull elephants or react
# 20 times faster than a normal human.


if __name__ == '__main__':
    pass
    # for mname in MAT_BY_NAME:
    #     print(mname)
        #
        # for cname in METAL_CONSTRUCTS:
        #     for mm in range(1, 12):
        #         layer = Layer(mname, cname, mm)
        #         print(repr(layer))

