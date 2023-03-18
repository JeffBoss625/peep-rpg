import math
from dataclasses import dataclass, field
from typing import List, Any

from lib.prpg_main import is_in_sight


def how_loud(distance, loudness):
    """
    >>> how_loud(2, 5)
    1.25
    >>> how_loud(1.5, 5)
    2.2222222222222223
    >>> how_loud(1, 5)
    5.0
    >>> how_loud(0.5, 5)
    20.0
    >>> how_loud(0.4, 5)
    31.249999999999996
    >>> how_loud(0.3, 5)
    55.55555555555556
    >>> how_loud(0.2, 5)
    124.99999999999999
    >>> how_loud(0.1, 5)
    499.99999999999994
    """
    return loudness * (1 / distance ** 2)


def distance(p1, p2):
    dis_x = abs(p1[0] - p2[0])
    dis_y = abs(p1[1] - p2[1])
    if dis_x == 0 or dis_y == 0:
        ret = dis_x + dis_y
        return ret
    sq_dis_x = dis_x ** 2
    sq_dis_y = dis_y ** 2
    tobe = sq_dis_x + sq_dis_y
    ret = math.sqrt(tobe)
    return ret

def disturbance(src, dst, loudness):
    dist = distance(src.pos, dst.pos)
    return how_loud(dist, loudness)

def sound_made(peep, control):
    loudness = (peep.armor.sound + peep.weight) * peep.silent_ability
    for p in control.peeps:
        if is_in_sight(p, peep.pos, control.mazemodel.walls):
            time_heard = peep.age         #1 age is a normal speed (1) moving one square, add all sound during that time of moving from one square to another
            p.process_sound.append(disturbance(peep, p, loudness), time_heard)
            for s in p.process_sound:
                if 1 < s[1] - time_heard:   #todo: Make a function for updating event window
                    p.process_sound.remove(s)

@dataclass
class PeepSleeping:
    sleepiness: float = 0
    limit: int = 1
    age_checked: int = 0
    timer: List[Any] = field(default_factory=list)
    target: float = 0.2
    cycles: int = 0

def handle_sound(time, sleep):
    time_passed = time - sleep.age_checked
    sleep.age_checked = time

    if sleep.timer[0] is True and sleep.timer[1] <= 0:
        if sleep.target == sleep.limit:
            sleep.cycles += 1
            if sleep.cycles > 5: sleep.cycles = 5
            sleep.target = 0.2 * sleep.limit
            sleep.timer[0] = False
        else:
            sleep.target = sleep.limit
            sleep.timer[0] = False

    if sleep.sleepiness < sleep.target:
        sleep.sleepiness += 0.05 * time_passed * ((sleep.cycles * 0.1) + 1)
        if sleep.sleepiness >= sleep.target:
            sleep.sleepiness = sleep.target
            sleep.timer[0] = True
            if sleep.target == sleep.limit:
                sleep.timer[1] = 20 * (1 - (sleep.cycles * 0.1))
            else:
                sleep.timer[1] = 10 * (1 - (sleep.cycles * 0.1))
    elif sleep.sleepiness > sleep.target:
        sleep.sleepiness -= 0.05 * time_passed * ((sleep.cycles * 0.1) + 1)
        if sleep.sleepiness <= sleep.target:
            sleep.sleepiness = sleep.target
            sleep.timer[0] = True
            if sleep.target == sleep.limit:
                sleep.timer[1] = 10 * (1 - (sleep.cycles * 0.1))
            else:
                sleep.timer[1] = 20 * (1 - (sleep.cycles * 0.1))
    else:
        sleep.timer[1] -= time_passed

    return time, sleep.sleepiness




if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    sleep = PeepSleeping(0, 1, 0, [False, 0], 0.2, 0)
    i = 0
    while i <= 400:
        print(handle_sound(i, sleep))
        i += 0.25

