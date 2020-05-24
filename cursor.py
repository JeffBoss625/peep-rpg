# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.moves as mlib
from curses import wrapper
from lib.moves import Direction
from lib.moves import calc_dx_dy

MAZE = [
    '%%%%%%%%%%%%%%%%%%%%',
    '%....####....######%',
    '%....####....######%',
    '%....####....####..%',
    '%............####..%',
    '%....####....####..%',
    '%....####..........%',
    '%....####....######%',
    '%....####....######%',
    '%%%%%%%%%%%%%%%%%%%%',
]

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
    'hp': 5,
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
    {'peep': PLAYER, 'x': 1, 'y': 2, 'hp': 10},
    {'peep': GOBLIN, 'x': 2, 'y': 2, 'hp': 10}
]

def draw_stats(scr, player):
    y, x = scr.getyx()
    scr.addstr(player['name'])
    scr.move(y+1, x)
    scr.addstr('hp:    ' + str(player['hp']))
    scr.move(y+2, x)
    scr.addstr('speed: ' + str(player['speed']))


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

def main(scr):
    scr.clear()
    player = PEEPS[0]

    scr.move(2, 10)
    draw_stats(scr, player['peep'])

    input_key = 0
    xoff = 10
    yoff = 10
    while input_key != 'Q':
        scr.move(yoff, xoff)
        draw_maze(scr, MAZE)
        for p in PEEPS:
            scr.move(yoff,xoff)
            draw_peep(scr, p)
        scr.move(0,0)
        scr.refresh()
        input_key = scr.getkey()
        dir = KEY_DIR[input_key]
        mlib.move_peep(PEEPS, MAZE, player, dir)
        for i in range(1, len(PEEPS)):
            enemy = PEEPS[i]
            dx = player['x'] - enemy['x']
            dy = player['y'] - enemy['y']
            if enemy['hp']/enemy['peep']['hp'] < 0.5:
                edir = mlib.direction_from_vector(-dx, -dy)
            else:
                edir = mlib.direction_from_vector(dx, dy)
            mlib.move_peep(PEEPS, MAZE, enemy, edir)



wrapper(main)
