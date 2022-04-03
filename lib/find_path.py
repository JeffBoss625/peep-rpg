from dataclasses import dataclass, field
from time import sleep
from typing import Tuple

from lib.items import clothes


class FLog:
    def __init__(self, control):
        self.control = control
        self.game = control.game_model

    def is_wall(self, x, y):
        sleep(0.03)
        c = self.game.maze_model.walls.char_at(x, y)
        is_w = c == '%' or c == '#'
        item = clothes.belt(pos=(x, y))
        if is_w:
            item.char = '&'
        else:
            item.char = '_'

        self.game.maze_model.items.append(item)
        self.control.root_layout.window.paint()
        return is_w

    def mark_exit(self, x, y):
        sleep(0.2)
        item = clothes.belt(pos=(x, y))
        item.char = 'X'
        self.game.maze_model.items.append(item)
        self.control.root_layout.window.paint()


@dataclass
class Hall:
    p1: Tuple[int, int] = field(default_factory=tuple) #String is for direction
    direct1: str = 'up'
    p2: Tuple[int, int] = field(default_factory=tuple)
    direct2: str = 'up'
    dist: int = 0


def find_rooms(control, input_key):
    halls = _find_rooms(control.game_model.player.pos, (), FLog(control))
    for h in halls:
        follow_hall(h, FLog(control))


def nextdir(dir, turn):
    if turn == 'cw':
        if dir == 'up':
            return 'right'
        if dir == 'right':
            return 'down'
        if dir == 'down':
            return 'left'
        if dir == 'left':
            return 'up'
    else:
        if dir == 'up':
            return 'left'
        if dir == 'left':
            return 'down'
        if dir == 'down':
            return 'right'
        if dir == 'right':
            return 'up'


def _find_rooms(src, tgt, flog):
    facing = None
    exit = []
    pos = list(src)
    been = []
    while flog.is_wall(pos[0] - 1, pos[1]) is False:
        pos[0] = pos[0] - 1
    if flog.is_wall(pos[0], pos[1] - 1) is False:
        facing = 'up'
    else:
        facing = 'right'
    while pos not in been:
        while flog.is_wall(
                point_of(pos, facing, 'forward')[0],
                point_of(pos, facing, 'forward')[1]) is False and \
                flog.is_wall(point_of(pos, facing, 'left')[0],
                             point_of(pos, facing, 'left')[1]):
            if flog.is_wall(
                point_of(pos, facing, 'right')[0],
                point_of(pos, facing, 'right')[1]
            ) is True and flog.is_wall(
                point_of(pos, facing, 'back')[0],
                point_of(pos, facing, 'back')[1]
            ) is False:
                flog.mark_exit(pos[0], pos[1])
                exit.append(Hall(p1=(pos[0], pos[1]), direct1=facing))
                pos[0] = point_of(pos, facing, 'back')[0]
                pos[1] = point_of(pos, facing, 'back')[1]
                facing = nextdir(facing, 'cw')
                facing = nextdir(facing, 'cw')
                break
            been.append(list(pos))
            pos[0] = point_of(pos, facing, 'forward')[0]
            pos[1] = point_of(pos, facing, 'forward')[1]

        if flog.is_wall(
                point_of(pos, facing, 'left')[0],
                point_of(pos, facing, 'left')[1]):
            facing = nextdir(facing, 'cw')
            # pos[0] = point_of(pos, facing, 'right')[0]
            # pos[1] = point_of(pos, facing, 'right')[1]
        else:
            facing = nextdir(facing, 'ccw')
            pos[0] = point_of(pos, facing, 'forward')[0]
            pos[1] = point_of(pos, facing, 'forward')[1]
    return exit


def follow_hall(hall, flog):
    facing = hall.direct1
    pos = []
    been = []
    pos.append(hall.p1[0])
    pos.append(hall.p1[1])
    distance = 0
    while wall_around(pos, flog) == 2:
        if flog.is_wall(point_of(pos, facing, 'forward')[0], point_of(pos, facing, 'forward')[1]) is False:
            been.append(list(pos))
            pos[0] = point_of(pos, facing, 'forward')[0]
            pos[1] = point_of(pos, facing, 'forward')[1]
            distance += 1
        else:
            if flog.is_wall(point_of(pos, facing, 'right')[0], point_of(pos, facing, 'right')[1]) is False:
                been.append(list(pos))
                pos[0] = point_of(pos, facing, 'right')[0]
                pos[1] = point_of(pos, facing, 'right')[1]
                facing = nextdir(facing, 'cw')
                distance += 1
            else:
                been.append(list(pos))
                pos[0] = point_of(pos, facing, 'left')[0]
                pos[1] = point_of(pos, facing, 'left')[1]
                facing = nextdir(facing, 'ccw')
                distance += 1
    final_pt = been[-1]
    flog.mark_exit(final_pt[0], final_pt[1])
    hall.p2 = final_pt
    facing = nextdir(facing, 'cw')
    facing = nextdir(facing, 'cw')
    hall.direct2 = facing
    hall.dist = distance


def wall_around(pos, flog):
    ret = 0
    if flog.is_wall(point_of(pos, 'up', 'forward')[0], point_of(pos, 'up', 'forward')[1]):
        ret += 1
    if flog.is_wall(point_of(pos, 'up', 'right')[0], point_of(pos, 'up', 'right')[1]):
        ret += 1
    if flog.is_wall(point_of(pos, 'up', 'left')[0], point_of(pos, 'up', 'left')[1]):
        ret += 1
    if flog.is_wall(point_of(pos, 'up', 'back')[0], point_of(pos, 'up', 'back')[1]):
        ret += 1
    return ret


def point_of(pos, facing, point):
    if facing == 'up':
        if point == 'forward': ret = [0 + pos[0], -1 + pos[1]]
        if point == 'back':    ret = [0 + pos[0], 1 + pos[1]]
        if point == 'right':   ret = [1 + pos[0], 0 + pos[1]]
        if point == 'left':    ret = [-1 + pos[0], 0 + pos[1]]
    if facing == 'right':
        if point == 'forward': ret = [1 + pos[0], 0 + pos[1]]
        if point == 'back':    ret = [-1 + pos[0], 0 + pos[1]]
        if point == 'right':   ret = [0 + pos[0], 1 + pos[1]]
        if point == 'left':    ret = [0 + pos[0], -1 + pos[1]]
    if facing == 'left':
        if point == 'forward': ret = [-1 + pos[0], 0 + pos[1]]
        if point == 'back':    ret = [1 + pos[0], 0 + pos[1]]
        if point == 'right':   ret = [0 + pos[0], -1 + pos[1]]
        if point == 'left':    ret = [0 + pos[0], 1 + pos[1]]
    if facing == 'down':
        if point == 'forward': ret = [0 + pos[0], 1 + pos[1]]
        if point == 'back':    ret = [0 + pos[0], -1 + pos[1]]
        if point == 'right':   ret = [-1 + pos[0], 0 + pos[1]]
        if point == 'left':    ret = [1 + pos[0], 0 + pos[1]]
    return ret
