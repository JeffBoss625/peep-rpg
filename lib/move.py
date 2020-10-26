from lib.attack import attack_dst, choose_melee_attack
from lib.peep_types import create_peep


# update time for peeps
# return an array of same length as peeps with the number of moves for each peep, rounded down.
# store unused remainder tics into peep.tics.
#
# peeps: array of movable items with "speed" and "tics" properties
# fac: factor to apply to speed to represent only a fraction of a turn (for peeps that enter part-way through a turn)
def elapse_time(peeps, fac):
    move_counts = []                    # same array indexes as peeps
    for p in peeps:
        tics = (p.speed * fac) + p.tics
        move_counts.append(int(tics / 10))  # round-down division operator (python 3+)
        p.tics = round(tics % 10, 5)        # store remaining ticks (MOD operator)

    return move_counts

def peeps_by_clicks(move_counts):
    peepidx_by_mc = {}
    for peep_index, mc in enumerate(move_counts):
        if mc != 0:
            if mc not in peepidx_by_mc:
                peepidx_by_mc[mc] = []
            peepidx_by_mc[mc].append(peep_index)

    # peepidx_by_mc is something like {1:[0,2,3], 3:[4], 7:[1]}  (indexes of peeps moving once, three times and seven times)
    # peepidx_by_mc.keys would be [1,3,7]
    # peepidx_by_mc.keys[1] would be [0,2,3]                     (indexes of peeps moving only once)

    # calculate total clicks (= 1 * 2 * 3, in the example)
    tot_clicks = 1
    for move_count in peepidx_by_mc.keys():
        tot_clicks = tot_clicks * move_count

    # create a new structured keyed by CLICKS per move, not moves (clicks = tot_clicks/moves)
    # = {6:[0,2,3], 3:[4], 2:[1]} for this example
    peepsbyclicks = {}
    for move_count in peepidx_by_mc.keys():
        peepsbyclicks[int(tot_clicks / move_count)] = peepidx_by_mc[move_count]

    return [peepsbyclicks, tot_clicks]


# create an array the length of all clicks and put at each
# click/index where there is a move an array of monster (indexes) that get a move at
# that click.
#
# For example, in the returned array below, m1 has a move at clicks 1, 5, and 9.
# m2 has a move at clicks 3 and 7
# m3 has a move only at click 5 (simultaneously with m1's second move)
# [
#   1       [m1]
#   2       []
#   3       [m2]
#   4       []
#   5       [m1,m3]
#   6       []
#   7       [m2]
#   8       []
#   9       [m1]
# ]
def _calc_turn_sequence(peepsbyclicks, tot_clicks):
    # walk through tot_clicks and sequence monster moves for every click
    ret = [[] for _ in range(tot_clicks)]
    for click_count in range(1, tot_clicks + 1):
        for clicks in peepsbyclicks.keys():
            if click_count % clicks == 0:
                peeps = peepsbyclicks[clicks]
                for p in peeps:
                    ret[click_count - 1].append(p)
    return ret


def calc_turn_sequence(move_counts):
    p_by_clicks, tot_clicks = peeps_by_clicks(move_counts)
    return _calc_turn_sequence(p_by_clicks, tot_clicks)

# x and y modifiers for each directions on keypad
# Direction constants match keypad layout 1-9
#       7 8 9
#       4 5 6
#       1 2 3
class Direction: DOWN_LEFT, DOWN, DOWN_RIGHT, LEFT, CENTER, RIGHT, UP_LEFT, UP, UP_RIGHT = range(1,10)


X_MODIFIERS = {
    Direction.UP_LEFT: -1,
    Direction.LEFT: -1,
    Direction.DOWN_LEFT: -1,
    Direction.UP: 0,
    Direction.CENTER: 0,
    Direction.DOWN: 0,
    Direction.UP_RIGHT: 1,
    Direction.RIGHT: 1,
    Direction.DOWN_RIGHT: 1,
}

Y_MODIFIERS = {
    Direction.UP_LEFT: -1,
    Direction.UP: -1,
    Direction.UP_RIGHT: -1,
    Direction.LEFT: 0,
    Direction.CENTER: 0,
    Direction.RIGHT: 0,
    Direction.DOWN_LEFT: 1,
    Direction.DOWN: 1,
    Direction.DOWN_RIGHT: 1,
}


def direction_to_dxdy(direction):
    return X_MODIFIERS[direction], Y_MODIFIERS[direction]


def direction_from_vector(dx, dy):
    ret = Direction.CENTER

    if dx < 0 and dy < 0:
        ret = Direction.UP_LEFT
    if dx == 0 and dy < 0:
        ret = Direction.UP
    if dx > 0 and dy < 0:
        ret = Direction.UP_RIGHT
    if dx > 0 and dy == 0:
        ret = Direction.RIGHT
    if dx > 0 and dy > 0:
        ret = Direction.DOWN_RIGHT
    if dx == 0 and dy > 0:
        ret = Direction.DOWN
    if dx < 0 and dy > 0:
        ret = Direction.DOWN_LEFT
    if dx < 0 and dy == 0:
        ret = Direction.LEFT
    return ret

# Direction constants match keypad layout
#       7 8 9
#       4 5 6
#       1 2 3

# Direction constants in clockwise order for finding closest, second closest, third closest... direction from
# a given direction
DIRECT_ROTATION = [
    Direction.UP, Direction.UP_RIGHT,
    Direction.RIGHT, Direction.DOWN_RIGHT,
    Direction.DOWN, Direction.DOWN_LEFT,
    Direction.LEFT, Direction.UP_LEFT,
]

def direction_relative(direct, rotation):
    si = DIRECT_ROTATION.index(direct)
    i = (si + rotation) % len(DIRECT_ROTATION)
    return DIRECT_ROTATION[i]

# Handle move and collisions with monsters. Return True if move or attack was executed, false, if the move
# failed (hit a wall)
def move_peep(model, p, direct):
    dx, dy = direction_to_dxdy(direct)
    if dx == 0 and dy == 0:
        return True

    dst_pos = (p.pos[0] + dx, p.pos[1] + dy)
    dst = peep_at_pos(model.maze.peeps, dst_pos)
    if not dst:
        # players and ammo strike wall
        char = model.maze.wall_at(dst_pos)
        if char:
            if model.is_player(p) or getattr(p, 'move_tactic', None) == 'straight':
                wall = create_wally(model.maze, dst_pos)
                dst = wall
            else:
                return False # peep did not move

    if dst:
        src_attack = choose_melee_attack(p)
        if src_attack:
            attack_dst(p, dst, src_attack, model)
        return True

    # all clear. just move
    p.pos = (p.pos[0] + dx, p.pos[1] + dy)
    return True


def peep_at_pos(peeps, pos):
    for p in peeps:
        if p.pos == pos and p.hp > 0:
            return p
    return None

def create_wally(maze, pos):
    char = maze.wall_at(pos)
    if char == '#':
        wall = create_peep('wall', 'Wally', pos=pos)
    elif char == '%':
        wall = create_peep('permanent wall', '*WALLY*', pos=pos)
    else:
        raise ValueError(f'no wall located at {pos}')

    maze.walls.replace_region(pos[0], pos[1], ['.'])
    maze.new_peeps.append(wall)
    return wall


# if __name__ == "__main__":
    # from pprint import pprint
    # from lib.model import *
    #
    # model = get_model()
    # peeps = model['peeps'][1:3]
    #
    # move_counts = elapse_time(peeps)
    # [m_by_clicks, tot_clicks] = monsters_by_clicks(move_counts)
    # move_seq = calc_move_sequence(m_by_clicks, tot_clicks)
    # print(move_seq)

    # change keys to clicks per move = total clicks / move count
    # make a new dictionary and move each key across.

    # iterate counting up clicks (total_clicks = 1, =2, =3, ...) and see if total_clicks/key_clicks evenly divides
    #   if total_clicks % key_clicks == 0

    # if so, add that list of monster indexes to the return array. (building up a return array)
    # return that list.

#
#    move_counts = elapse_time(peeps)
#    pprint(peeps)
#    print('move_counts:', move_counts)
#
#    move_counts = elapse_time(peeps)
#    pprint(peeps)
#    print('move_counts:', move_counts)
#
#    move_counts = elapse_time(peeps)
#    pprint(peeps)
#    print('move_counts:', move_counts)
