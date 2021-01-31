import math




def level_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base*math.pow(factor, i)
        ret += addon
    return ret
