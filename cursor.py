# Demonstrate simple cursor drawing and movement (h,j,k,l)

from curses import wrapper
from lib.moves import DIRECTION as DIR
from lib.moves import movexy

maze = [
    '.....xxxxxxxxxxxxxxx',
    '.....xxxx....xxxxxxx',
    '.....xxxx....xxxxxxx',
    '.....xxxx....xxxx..x',
    '.....xxxx....xxxx..x',
    '.....xxxx....xxxx..x',
    '.....xxxx..........x',
    '.....xxxx....xxxxxxx',
    '.....xxxx....xxxxxxx',
    '.....xxxxxxxxxxxxxxx',
]

player = {
    'name': 'Bo Bo the Destroyer',
    'type': 'player',
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
player = {'peep': player, 'x': 0, 'y': 2, 'hp': 3}


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
    scr.refresh()


def draw_peep(scr, p):
    scr.move(p['y'], p['x'])
    scr.addch('@')

KEY_DIR = {
    'j': DIR['D'],
    'k': DIR['U'],
    'l': DIR['R'],
    'h': DIR['L']
}

def main(scr):
    scr.clear()

    scr.move(2, 10)
    draw_stats(scr, player['peep'])

    input_key = 0
    xoff = 10
    yoff = 10
    player['x'] += xoff
    player['y'] += yoff
    while input_key != 'Q':
        scr.move(yoff, xoff)
        draw_maze(scr, maze)
        draw_peep(scr, player)
        scr.move(0,0)

        input_key = scr.getkey()
        dir = KEY_DIR[input_key]
        dx, dy = movexy(dir)
        player['x'] += dx
        player['y'] += dy

wrapper(main)
