
import lib.attack as attacklib
# update time for monsters
# return the number of moves (rounded down) for each monster as a structure of
#   { number-of-moves: monster-list (indexes) }
# put remainder ticks into monster state
def elapse_time(peeps):
    move_counts = []
    for pinfo in peeps:
        p = pinfo['peep']
        tics = p['speed'] + p['tics']
        move_counts.append(tics // 10)  # Special division operator (python 3+)
        p['tics'] = tics % 10  # MOD operator

    return move_counts

# divide tot_clicks by each key
# take the new numbers and check for mod by dividing new number by click it is going through currently
# If mod is = 0 then add the whole key group to a new list inside a list


# convert move counts into number of clicks (total clicks is a number divisible by all moster clicks-per-move

# walk through ALL clicks "i" and check for each i
#   for each clicks-per-move "j" check that divides "i" without remainder
#      if so, put "j" in that move list (for that click) - j is the monster index
#   add move list to total moves list (return list). perhaps only add lists with length > 0


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


def calc_dx_dy(direction):
    return X_MODIFIERS[direction], Y_MODIFIERS[direction]


# def handle_moves(model, moves)
#    # check if monsters collide with monsters
#    # go through every monster move. handle collided monsters and capture non-colliding in a 'remaining' list
#    monsters = model['monsters']
#    collided = []
#    remaining = []
#    num_monsters = len(monsters)
#    for i in range(0, num_monsters):
#        print('check collission ' + str(i))
#        d = moves[i]['direction']
#        if (d == 0):
#            continue
#        # d is 1 through 9
#        m = monsters[i]
#        new_position = { 'x': m['x'] + x_modifiers[d] , 'y': m['y'] + y_modifiers[d] }
#        print('checking new_position ' + str(new_position))
#        
#        
#            
#    monsters = remaining
#    
#    # check if remaining (non-colliding) monsters collide with walls
#    
#
#    # update remaining monsters location
#    moving_monsters = remaining
#   
#    # check monsters again land on an item with their new location (e.g. pick up)


def monsters_by_clicks(move_counts):
    monsters_by_mc = {}
    for i, mc in enumerate(move_counts):
        if mc not in monsters_by_mc:
            monsters_by_mc[mc] = []
        monsters_by_mc[mc].append(i)

    print('monsters_by_mc:', monsters_by_mc)
    # monstersbymoves is something like {1:[0,2,3], 2:[4], 3:[1]}
    # monstersbymoves.keys would be [1,2,3]
    # monstersbymoves.keys[1] would be [0,2,3]

    # calculate total clicks (= 1 * 2 * 3, in the example)
    tot_clicks = 1
    for moves in monsters_by_mc.keys():
        tot_clicks = tot_clicks * moves

    print('tot_clicks:', tot_clicks)

    # create a new structured keyed by CLICKS per move, not moves (clicks = tot_clicks/moves)
    # = {6:[0,2,3], 3:[4], 2:[1]} for this example
    monstersbyclicks = {}
    for moves in monsters_by_mc.keys():
        monstersbyclicks[int(tot_clicks / moves)] = monsters_by_mc[moves]

    print('monstersbyclicks', monstersbyclicks)

    return [monstersbyclicks, tot_clicks]


#
def calc_move_sequence(monstersbyclicks, tot_clicks):
    print('calc_move_sequence(', monstersbyclicks, ',', tot_clicks, ')')
    # walk through tot_clicks and sequence monster moves for every click
    ret = [[] for _ in range(tot_clicks)]
    for click_count in range(1, tot_clicks + 1):
        print('  click_count:', click_count)
        for clicks in monstersbyclicks.keys():
            # if ret[click_count-1] is None:
            #     ret[click_count-1] = []
            print('    monster clicks:', clicks)
            if click_count % clicks == 0:
                monsters = monstersbyclicks[clicks]
                print('    monsters:', monsters)
                for m in monsters:
                    ret[click_count - 1].append(m)
            print('    moves_by_click_count', ret)

    return ret

def handle_enemy_move(peeps, maze, enemy, dir):
    dx, dy = calc_dx_dy(dir)
    if check_wall_collide(maze, enemy['x']+dx, enemy['y']+dy) is None:
        if check_unbreakable_collide(maze, enemy['x']+dx, enemy['y']+dy) is None:
            if check_peep_at(peeps, enemy['x']+dx, enemy['y']+dy) is None:
                enemy['x'] += dx
                enemy['y'] += dy
            else:
                dst = check_peep_at(peeps, enemy['x']+dx, enemy['y']+dy)
                attacklib.attack(enemy, dst, 'bite')
                if dst['hp'] <= 0:
                    peeps.remove(dst)

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

def handle_player_move(peeps, maze, player, dir):
    ps = player                     # player state (current position, hit points...)
    player_info = player['peep']    # other player reference data (weapons, original hit points...)
    dx, dy = calc_dx_dy(dir)
    if check_wall_collide(maze, ps['x'] + dx, ps['y'] + dy) is None:
        if check_unbreakable_collide(maze, ps['x'] + dx, ps['y'] + dy) is None:
            if check_peep_at(peeps, ps['x'] + dx, ps['y'] + dy) is None:
                ps['x'] += dx
                ps['y'] += dy
            else:
                dst = check_peep_at(peeps, ps['x'] + dx, ps['y'] + dy)
                weapon = attacklib.choose_melee_weapon(player_info)
                attacklib.attack(ps, dst, weapon)
                if dst['hp'] <= 0:
                    peeps.remove(dst)
    # else: do nothing

def check_peep_at(peeps, player_x, player_y):
    for p in peeps:
        if player_x == p['x']:
            if player_y == p['y']:
                return p
    return None

def check_wall_collide(maze, player_x, player_y):
    line = maze[player_y]
    cell = line[player_x]
    if cell == '#':
        return {'type': 'wall', 'x': str(player_x), 'y': str(player_y)}
    else:
        return None
def check_unbreakable_collide(maze, player_x, player_y):
    line = maze[player_y]
    cell = line[player_x]
    if cell == '%':
        return {'type': 'unbreakable', 'x': str(player_x), 'y': str(player_y)}
    else:
        return None

if __name__ == "__main__":
    from pprint import pprint
    from lib.model import *

    model = get_model()
    peeps = model['peeps'][1:3]

    move_counts = elapse_time(peeps)
    move_counts = [1,2,1,3]
    [m_by_clicks, tot_clicks] = monsters_by_clicks(move_counts)
    move_seq = calc_move_sequence(m_by_clicks, tot_clicks)
    print(move_seq)

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
