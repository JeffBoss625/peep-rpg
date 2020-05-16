# Demonstrate simple cursor drawing and movement (h,j,k,l)

from curses import wrapper
from lib.moves import Direction
from lib.moves import calc_dx_dy

MAZE = [
    '.....###############',
    '.....####....#######',
    '.....####....#######',
    '.....####....####..#',
    '.....####....####..#',
    '.....####....####..#',
    '.....####..........#',
    '.....####....#######',
    '.....####....#######',
    '.....###############',
]

GOBLIN = {
    'type': 'goblin',
    'char': 'g',
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
        'scratch': {
            'damage': '3d1'
        },
        'tail': {
            'damage': '2d3'
        },
    },
}

PEEPS = [
    {'peep': PLAYER, 'x': 0, 'y': 2, 'hp': 3},
    {'peep': GOBLIN, 'x': 2, 'y': 2}
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
    'k': Direction.UP,
    'l': Direction.RIGHT,
    'h': Direction.LEFT
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
        dx, dy = calc_dx_dy(dir)
        player['x'] += dx
        player['y'] += dy


wrapper(main)
