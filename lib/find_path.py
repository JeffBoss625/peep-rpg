from dataclasses import dataclass, field
from time import sleep
from typing import Tuple

from lib.dijikstra_algo import Node, add_edge, dijikstra
from lib.items import clothes


class FLog:
    def __init__(self, control):
        self.control = control
        self.game = control.game_model

    def is_wall(self, x, y):
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
        item = clothes.belt(pos=(x, y))
        item.char = 'X'
        self.game.maze_model.items.append(item)
        self.control.root_layout.window.paint()


@dataclass
class Hall:
    p1: Tuple[int, int] = field(default_factory=tuple) #String is for direction
    direct1: str = 'up'
    room1: Tuple[Tuple[int, int], ...] = field(default_factory=tuple)
    p2: Tuple[int, int] = field(default_factory=tuple)
    room2: Tuple[Tuple[int, int], ...] = field(default_factory=tuple)
    direct2: str = 'up'
    dist: int = 0

@dataclass
class Vector:
    pt: Tuple[int, int] = field(default_factory=tuple)
    direct: str = 'up'

@dataclass
class Room:
    exits: Tuple[Tuple[int, int], ...] = field(default_factory=tuple)


def find_rooms(control, input_key):
    #find start
    #find exits (in hall form)
    #make room from exits (list(exits))
    #follow exits to end
    #loop

    room_by_exits = {}
    halls_by_exits = {}
    all_halls = []
    con = True
    pos = find_start(control.game_model.player.pos, FLog(control))
    direct = 'up'
    while True:
        if not loop(room_by_exits, halls_by_exits, all_halls, pos, FLog(control), direct):
            node_graph(halls_by_exits, room_by_exits)
            break
        for h in all_halls:
            if h.p2 not in room_by_exits:
                pos = h.p2
                direct = h.direct2
                break




# def find_rooms(control, input_key):
#     room_by_exits = {}
#     halls_by_exits = {}
#     loop = True
#     halls = _find_rooms(control.game_model.player.pos, FLog(control), halls_by_exits, True, None)
#     room = Room(exits=halls[0].room1)
#     # put all hall rooms into dictionary
#     for p in halls[0].room1:
#         room_by_exits[tuple(p)] = room
#     for h in halls:
#         follow_hall(h, FLog(control))
#     for h in halls:
#         if h.p1 not in halls_by_exits:
#             halls_by_exits[h.p1] = h
#         if h.p2 not in halls_by_exits:
#             halls_by_exits[h.p2] = h
#             loop = True
#             while loop is True:
#                 halls = _find_rooms(h.p2, FLog(control), halls_by_exits, False, h.direct2)
#                 if halls is None:
#                     break
#                 room = Room(exits=halls[0].room1)
#                 for p in halls[0].room1:
#                     room_by_exits[tuple(p)] = room
#                 for h in halls:
#                     if h.p1 not in halls_by_exits:
#                         follow_hall(h, FLog(control))
#                     else:
#                         halls.remove(h)
#                         if len(halls) == 0:
#                             loop = False
#                             break
#                 if loop is False:
#                     break
#                 for h in halls:
#                     if h.p1 not in halls_by_exits:
#                         halls_by_exits[h.p1] = h
#                     if h.p2 not in halls_by_exits:
#                         halls_by_exits[h.p2] = h
#                         break


def make_room(vectors):
    ret = []
    for v in vectors:
        ret.append(v.pt)
    return ret


def make_halls(vectors):
    ret = []
    for v in vectors:
        ret.append(Hall(p1=v.pt, direct1=v.direct))
    return ret


def loop(room_by_exits, halls_by_exits, all_halls, pos, flog, direct):
    r = []
    vectors = find_exits(pos, flog, direct)
    room = make_room(vectors)
    for p in room:
        room_by_exits[p] = room
    halls = make_halls(vectors)
    for h in halls:
        if h.p1 in halls_by_exits:
            r.append(h)
        else:
            follow_hall_2(h.p1, h.direct1, h, flog)
            halls_by_exits[h.p1] = h
            halls_by_exits[h.p2] = h
            all_halls.append(h)
    for h in r:
        halls.remove(h)
    if len(halls) == 0:
        for h in all_halls:
            if h.p2 not in room_by_exits:
                con = True
                return con
        con = False
    else: con = True
    return con

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


def find_start(src, flog):
    pos = list(src)
    while flog.is_wall(pos[0] - 1, pos[1]) is False:
        pos[0] = pos[0] - 1
    return tuple(pos)


def find_exits(src, flog, dir):
    pos = tuple(src)
    been = []
    exits = []
    facing = dir
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
                if pos in been:
                    break
                flog.mark_exit(pos[0], pos[1])
                x = (Vector(pt=tuple(pos), direct=facing))
                exits.append(x)
                been.append(list(pos))
                pos = point_of(pos, facing, 'back')
                facing = nextdir(facing, 'cw')
                facing = nextdir(facing, 'cw')
                break
            been.append(list(pos))
            pos = point_of(pos, facing, 'forward')

        if flog.is_wall(
                point_of(pos, facing, 'left')[0],
                point_of(pos, facing, 'left')[1]):
            facing = nextdir(facing, 'cw')
        else:
            facing = nextdir(facing, 'ccw')
            been.append(list(pos))
            pos[0] = point_of(pos, facing, 'forward')[0]
            pos[1] = point_of(pos, facing, 'forward')[1]
    return exits


def follow_hall_2(src, facing, hall, flog):
    pos = list(src)
    been = []
    distance = 0
    while wall_around(pos, flog) == 2:
        if flog.is_wall(point_of(pos, facing, 'forward')[0], point_of(pos, facing, 'forward')[1]) is False:
            been.append(tuple(pos))
            pos[0] = point_of(pos, facing, 'forward')[0]
            pos[1] = point_of(pos, facing, 'forward')[1]
            distance += 1
        else:
            if flog.is_wall(point_of(pos, facing, 'right')[0], point_of(pos, facing, 'right')[1]) is False:
                been.append(tuple(pos))
                pos[0] = point_of(pos, facing, 'right')[0]
                pos[1] = point_of(pos, facing, 'right')[1]
                facing = nextdir(facing, 'cw')
                distance += 1
            else:
                been.append(tuple(pos))
                pos[0] = point_of(pos, facing, 'left')[0]
                pos[1] = point_of(pos, facing, 'left')[1]
                facing = nextdir(facing, 'ccw')
                distance += 1
    final_pt = been[-1]
    flog.mark_exit(final_pt[0], final_pt[1])
    facing = nextdir(facing, 'cw')
    facing = nextdir(facing, 'cw')
    hall.p2 = final_pt
    hall.dist = distance - 1
    hall.direct2 = facing


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


def get_key(val, dict):
    for key, v in dict.items():
        for value in v:
            if val == value:
                return key

    return "key doesn't exist"





def node_graph(halls_by_pt, rooms_by_exits):
    rooms = []
    halls = []
    rooms_by_id = {}

    for h in halls_by_pt:
        if halls_by_pt[h] not in halls:
            halls.append(halls_by_pt[h])

    for r in rooms_by_exits:
        if rooms_by_exits[r] not in rooms:
            rooms.append(rooms_by_exits[r])

    nodes = {}
    for id in range(1, len(rooms) + 1):
        rooms_by_id[id] = rooms[id-1]
        nodes[id] = Node(id, {}, [])

    edges = {}
    for id in rooms_by_id:
        for e in rooms_by_id[id]:
            if halls_by_pt[e].p1 == e:
                for r in rooms_by_exits[halls_by_pt[e].p2]:
                    id2 = get_key(r, rooms_by_id)
                    add_edge(edges, id, id2, halls_by_pt[e].dist)
                    nodes[id].edges.append(edges[(id, id2)])
            else:
                for r in rooms_by_exits[halls_by_pt[e].p1]:
                    id2 = get_key(r, rooms_by_id)
                    add_edge(edges, id, id2, halls_by_pt[e].dist)
                    nodes[id].edges.append(edges[(id, id2)])
    dijikstra(nodes)

# find paths algo

# start with 2 empty dictionaries and a start_point
#   all_rooms by exit points (dict of all rooms by every exit point of the room)
#   all_hallways by exit points (dict of all hallways by the 2 exit points of the hallway)

# create first room
#   room.exits = find exit points for room
#   convert exit points to halls (looking up in dictionary)
#   do NOT follow hallways yet to find point2

# finish hallways
#   go through room hallways and find all end-points of hallways - point2 if missing

