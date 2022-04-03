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
    p1: Tuple[int, int] = field(default_factory=tuple)
    p2: Tuple[int, int] = field(default_factory=tuple)
    dist: int = 0


def find_rooms(control, input_key):
    _find_rooms(control.game_model.player.pos, (), FLog(control))


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
                exit.append(list(pos))
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
