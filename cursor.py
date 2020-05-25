# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.move as mlib
from lib.monsters import monster_by_name
from lib.peeps import peep_by_name
from curses import wrapper
from lib.move import Direction

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

PEEPS = [
    peep_by_name('Bo Bo the Destroyer', x=1, y=2, hp=10),
    monster_by_name('Thark', x=2, y=2, hp=10),
]

def draw_stats(scr, player):
    y, x = scr.getyx()
    blank = '                                  '
    scr.move(y, x)
    scr.addstr(blank)
    scr.move(y, x)
    scr.addstr(player.name)

    scr.move(y+1, x)
    scr.addstr(blank)
    scr.move(y+1, x)
    scr.addstr('hp:    ' + str(player.hp) + '/' + str(player.maxhp))

    scr.move(y+2, x)
    scr.addstr(blank)
    scr.move(y+2, x)
    scr.addstr('speed: ' + str(player.speed))


def draw_maze(scr, maze):
    y, x = scr.getyx()
    for i, line in enumerate(maze):
        scr.move(y+i, x)
        scr.addstr(line)
        # for c in line:
        #     scr.addch(c)

def draw_peep(scr, p):
    y, x = scr.getyx()
    scr.move(p.y + y, p.x + x)
    scr.addch(p.char)

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

    scr.move(2, 10)
    draw_stats(scr, player)

    input_key = 0
    xoff = 10
    yoff = 10
    turn = 0
    while input_key != 'q':
        turn += 1

        # DRAW SCREEN CONTENTS...

        scr.move(2, 10)
        draw_stats(scr, player)

        scr.move(yoff, xoff)
        draw_maze(scr, MAZE)

        for p in PEEPS:
            scr.move(yoff,xoff)
            draw_peep(scr, p)

        if len(MESSAGES) > 12:
            MESSAGES = MESSAGES[-12:]
        scr.move(yoff + len(MAZE) + MARGIN_SIZE, xoff)
        draw_messages(scr, MESSAGES)

        scr.move(0,0)
        scr.refresh()

        # GET AND HANDLE PLAYER MOVE
        input_key = scr.getkey()
        if input_key in KEY_DIR:
            dir = KEY_DIR[input_key]

            # MOVE PLAYER
            msg = mlib.move_peep(PEEPS, MAZE, player, dir)
            MESSAGES.extend(msg)

            # MOVE MONSTERS
            for i in range(1, len(PEEPS)):
                enemy = PEEPS[i]
                # MOVE MONSTER
                dx = player.x - enemy.x
                dy = player.y - enemy.y
                if enemy.hp/enemy.hp < 0.2:
                    edir = mlib.direction_from_vector(-dx, -dy)
                else:
                    edir = mlib.direction_from_vector(dx, dy)
                msg = mlib.move_peep(PEEPS, MAZE, enemy, edir)
                MESSAGES.extend(msg)

    # while input_key != 'q':
        # DRAW SCREEN CONTENTS...
        # GET AND HANDLE PLAYER MOVE

        # input_key = scr.getkey()

        # if input_key in KEY_DIR:
            # MOVE PLAYER
            # MOVE MONSTERS


#   while input_key != 'q':
#       GET PLAYER AND MONSTER MOVES (move_sequence)
#       For each set of moves:
#           For each move (in simultaneous set):
#               if it's a monster, MOVE MONSTER
#               else (player), get input (input_key = scr.getkey()):
#                   if input is a move:
#                       MOVE PLAYER
#                   else if it's quit (q), stop program
#                   else... add message, "action not handled"
#               DRAW SCREEN CONTENTS



wrapper(main)
