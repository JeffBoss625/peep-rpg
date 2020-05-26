from lib.peep import Peep
import lib.attack as attacklib
# update time for monsters
# return the number of moves (rounded down) for each monster as a structure of
#   { number-of-moves: monster-list (indexes) }
# put remainder ticks into monster state
def elapse_time(peeps):
    move_counts = []
    for p in peeps:
        tics = p.speed + p.tics
        move_counts.append(tics // 10)  # Special division operator (python 3+)
        p.tics = tics % 10  # MOD operator

    return move_counts

def peeps_by_clicks(move_counts):
    monsters_by_mc = {}
    for i, mc in enumerate(move_counts):
        if mc not in monsters_by_mc:
            monsters_by_mc[mc] = []
        monsters_by_mc[mc].append(i)

    # monstersbymoves is something like {1:[0,2,3], 2:[4], 3:[1]}
    # monstersbymoves.keys would be [1,2,3]
    # monstersbymoves.keys[1] would be [0,2,3]

    # calculate total clicks (= 1 * 2 * 3, in the example)
    tot_clicks = 1
    for moves in monsters_by_mc.keys():
        tot_clicks = tot_clicks * moves

    # create a new structured keyed by CLICKS per move, not moves (clicks = tot_clicks/moves)
    # = {6:[0,2,3], 3:[4], 2:[1]} for this example
    monstersbyclicks = {}
    for moves in monsters_by_mc.keys():
        monstersbyclicks[int(tot_clicks / moves)] = monsters_by_mc[moves]

    return [monstersbyclicks, tot_clicks]


def _calc_turn_sequence(monstersbyclicks, tot_clicks):
    # walk through tot_clicks and sequence monster moves for every click
    ret = [[] for _ in range(tot_clicks)]
    for click_count in range(1, tot_clicks + 1):
        for clicks in monstersbyclicks.keys():
            if click_count % clicks == 0:
                monsters = monstersbyclicks[clicks]
                for m in monsters:
                    ret[click_count - 1].append(m)

    return ret

def calc_turn_sequence(peeps):
    turn_counts = elapse_time(peeps)
    p_by_clicks, tot_clicks = peeps_by_clicks(turn_counts)
    return _calc_turn_sequence(p_by_clicks, tot_clicks)

# x and y modifiers for each directions on keypad
# Direction constants match keypad layout
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
    if maze_at_xy(model.maze, p.x + dx, p.y + dy):
        # hit wall
        model.print(p.name + ' says OOF!')
        return False

    dst = peep_at_xy(model.peeps, p.x + dx, p.y + dy)
    if dst:
        if p.type == 'player':
            weapon = attacklib.choose_melee_attack(p)
            attacklib.attack(p, dst, weapon, model)
            return True
        elif dst.type == 'player':
            model.print(p.name, 'says "DIE ' + dst.name + '!"')
            weapon = attacklib.choose_melee_attack(p)
            attacklib.attack(p, dst, weapon, model)
            return True
        else:
            # monsters are polite to each other... for now
            model.print(p.name, 'says "Oh, excuse me', dst.name + '"')
            return False

    # all clear. just move
    p.x += dx
    p.y += dy
    return True


def peep_at_xy(peeps, x, y):
    for p in peeps:
        if x == p.x:
            if y == p.y:
                return p
    return None

def maze_at_xy(maze, x, y):
    line = maze[y]
    char = line[x]
    if char == '#' or char == '%':
        return Peep(name='Wally', type='wall', char=char, x=x, y=y)
    else:
        return None


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
