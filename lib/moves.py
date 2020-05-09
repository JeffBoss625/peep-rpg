

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

# 7 8 9      -1,-1     0,-1     1,-1
# 4 5 6      -1, 0     0, 0     1, 0
# 1 2 3      -1, 1     0, 1     1,-1

x_modifiers = {
    7: -1,
    4: -1,
    1: -1,
    8: 0,
    5: 0,
    2: 0,
    9: 1,
    6: 1,
    3: 1,
}

y_modifiers = {
    1: 1,
    2: 1,
    3: 1,
    4: 0,
    5: 0,
    6: 0,
    7: -1,
    8: -1,
    9: -1,
}

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
