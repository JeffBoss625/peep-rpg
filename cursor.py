# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.moves as mlib
from curses import wrapper
from lib.moves import Direction
from lib.moves import calc_dx_dy
import lib.attack as attacklib

MAZE = [
    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
    '%....####....######%.........%',
    '%....####....######%.........%',
    '%....####....####..#.........%',
    '%............####..#.........%',
    '%....####....####............%',
    '%....####..........#.........%',
    '%....####....#######.........%',
    '%....####....#######.........%',
    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
]

DRAGON = {
    'name': 'Spark',
    'type': 'dragon',
    'char': 'D',
    'hp': 50,
    'thaco': 10,
    'speed': 16,
    'tics': 0,
    'ac': 10,
    'weapons': {
        'bite': {
            'damage': '1d10'
        },
        'fire breath': {
            'damage': '2d10'
        },
        'claws': {
            'damage': '2d7'
        },
        'tail': {
            'damage': '7d1'
        },
    },
}

GOBLIN = {
    'name': 'Thark',
    'type': 'goblin',
    'char': 'g',
    'hp': 10,
    'thaco': 18,
    'speed': 13,
    'tics': 0,
    'ac': 19,
    'weapons': {
        'bite': {
            'damage': '1d3'
        },
        'scratch': {
            'damage': '2d2'
        },
        'punch': {
            'damage': '2d1'
        }
    }
}

PLAYER = {
    'name': 'Bo Bo the Destroyer',
    'type': 'player',
    'char': '@',
    'hp': 50,
    'thaco': 19,
    'speed': 11,
    'tics': 0,
    'ac': 10,
    'weapons': {
        'teeth': {
            'damage': '1d5'
        },
        'tail': {
            'damage': '3d1'
        },
        'scratch': {
            'damage': '2d3'
        },
    },
}

PEEPS = [
    {'peep': PLAYER, 'x': 1, 'y': 2, 'hp': 50},
    {'peep': GOBLIN, 'x': 2, 'y': 2, 'hp': 10},
    {'peep': DRAGON, 'x': 24, 'y': 4, 'hp': 50},
]

def draw_stats(scr, player):
    y, x = scr.getyx()
    blank = '                                  '
    scr.addstr(blank)
    scr.move(y, x)
    scr.addstr(str(player['peep']['name']))
    scr.move(y+1, x)
    scr.addstr(blank)
    scr.move(y+1, x)
    scr.addstr('hp:    ' + str(player['hp']) + '/' + str(player['peep']['hp']))
    scr.move(y+2, x)
    scr.addstr(blank)
    scr.move(y+2, x)
    scr.addstr('speed: ' + str(player['peep']['speed']))


def draw_maze(scr, maze):
    y, x = scr.getyx()
    for i, line in enumerate(maze):
        scr.move(y+i, x)
        scr.addstr(line)
        # for c in line:
        #     scr.addch(c)

def draw_peep(scr, p):
    y, x = scr.getyx()
    scr.move(p['y'] + y, p['x'] + x)
    scr.addch(p['peep']['char'])

def draw_messages(scr, messages):
    y, x = scr.getyx()
    for i, m in enumerate(messages):
        scr.move(y+i, x)
        scr.addstr(m)

KEY_DIR = {
    'j': Direction.DOWN,
    'y': Direction.UP_LEFT,
    'k': Direction.UP,
    'u': Direction.UP_RIGHT,
    'l': Direction.RIGHT,
    'n': Direction.DOWN_RIGHT,
    'h': Direction.LEFT,
    'b': Direction.DOWN_LEFT,
}

MARGIN_SIZE = 3

def main(scr):
    MESSAGES = []
    scr.clear()
    player = PEEPS[0]
    input_key = 0
    xoff = 10
    yoff = 10
    turn = 0
    while input_key != 'q':
        turn += 1
        scr.move(2, 10)
        draw_stats(scr, player)
        scr.move(yoff, xoff)
        draw_maze(scr, MAZE)
        for p in PEEPS:
            scr.move(yoff,xoff)
            draw_peep(scr, p)
        if len(MESSAGES) > 8:
            MESSAGES = MESSAGES[-12:]
        scr.move(yoff + len(MAZE) + MARGIN_SIZE, xoff)
        draw_messages(scr, MESSAGES)
        scr.move(0,0)
        scr.refresh()
        turns(model, screen)

def turns(player, model, control):
    move_counts = mlib.elapse_time(PEEPS)
    [m_by_clicks, tot_clicks] = mlib.monsters_by_clicks(move_counts)
    move_seq = mlib.calc_move_sequence(m_by_clicks, tot_clicks)
    for i in range(0, len(move_seq) - 1):
        peep_moving = move_seq[i]
        if peep_moving['type'] == 'player':
            player_turn(PEEPS, MAZE, player, scr)
        else:
            enemy = peep_moving
            msg = enemy_turn(PEEPS, MAZE, player, enemy)
            messages.extend(msg)

def player_turn(model, player, screen):
    input_key = scr.getkey()
    msg = []
    if input_key in KEY_DIR:
        msg = mlib.move_peep(peeps, maze, player, input_key)
        messages.extend(msg)

        return msg
    return input_key

def enemy_turn(peeps, maze, player, enemy):
    dx = player['x'] - enemy['x']
    dy = player['y'] - enemy['y']
    if enemy['hp']/enemy['peep']['hp'] < 0.2:
        edir = mlib.direction_from_vector(-dx, -dy)
    else:
        edir = mlib.direction_from_vector(dx, dy)
    return mlib.move_peep(peeps, maze, enemy, edir)


def old_main(scr):
    MESSAGES = []
    scr.clear()
    player = PEEPS[0]
    input_key = 0
    xoff = 10
    yoff = 10
    turn = 0
    while input_key != 'q':
        turn += 1
        scr.move(2, 10)
        draw_stats(scr, player)
        scr.move(yoff, xoff)
        draw_maze(scr, MAZE)
        for p in PEEPS:
            scr.move(yoff,xoff)
            draw_peep(scr, p)
        if len(MESSAGES) > 8:
            MESSAGES = MESSAGES[-12:]
        scr.move(yoff + len(MAZE) + MARGIN_SIZE, xoff)
        draw_messages(scr, MESSAGES)
        scr.move(0,0)
        scr.refresh()
        input_key = scr.getkey()
        if input_key in KEY_DIR:
            dir = KEY_DIR[input_key]
            msg = mlib.move_peep(PEEPS, MAZE, player, dir)
            MESSAGES.extend(msg)
            for i in range(1, len(PEEPS)):
                enemy = PEEPS[i]
                dx = player['x'] - enemy['x']
                dy = player['y'] - enemy['y']
                if enemy['hp']/enemy['peep']['hp'] < 0.2:
                    edir = mlib.direction_from_vector(-dx, -dy)
                else:
                    edir = mlib.direction_from_vector(dx, dy)
                msg = mlib.move_peep(PEEPS, MAZE, enemy, edir)
                MESSAGES.extend(msg)


wrapper(main)
