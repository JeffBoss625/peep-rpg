force_theshold = 1000

def crushing_blow(crush, target):
    for layer in target.armor.piece:
        crush, layer = apply_crush(crush, layer)
    f = (crush.mass * crush.velocity^2) / 2
    f_per_cm = f/crush.area
    if f_per_cm > force_theshold:
        return calc_damage(f_per_cm)
    else:
        return 0

def apply_crush(crush, layer):
    crush.velocity = crush.velocity - layer.elasticity
    crush.area = crush.area + 5
    return crush

def calc_damage(force):
    damage = (force^1.3)/3500



def piercing_blow(pierce, target):
    for layer in target.armor.piece:
        if pierceable(pierce, layer):
            pierce, layer = apply_pierce(pierce, layer)
        else:
            return crushing_blow(pierce, target)
    f = (pierce.mass * pierce.velocity^2) / 2
    f_per_cm = f/pierce.area
    if f_per_cm > force_theshold:
        return calc_damage(f_per_cm)
    else:
        return 0


def apply_pierce(pierce, layer):
    pierce.velocity = pierce.velocity - layer.thickness
    return pierce

def pierceable(pierce, layer):
    return True