# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.move as mlib
from lib.monsters import monster_by_name
from lib.peeps import peep_by_name
from curses import wrapper
from lib.move import Direction

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

PEEPS = [
    peep_by_name('Bo Bo the Destroyer', x=1, y=2, hp=10),
    monster_by_name('Thark', x=2, y=2, hp=10),
]

def draw_stats(scr, player):
    y, x = scr.getyx()
    scr.addstr(player.name)
    scr.move(y+1, x)
    scr.addstr('hp:    ' + str(player.hp))
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
        scr.move(yoff, xoff)
        draw_maze(scr, MAZE)
        for p in PEEPS:
            scr.move(yoff,xoff)
            draw_peep(scr, p)
        MESSAGES.append('turn ' + str(turn) + ': hi there')
        if len(MESSAGES) > 8:
            MESSAGES = MESSAGES[-8:]
        scr.move(yoff + len(MAZE) + MARGIN_SIZE, xoff)
        draw_messages(scr, MESSAGES)
        scr.move(0,0)
        scr.refresh()
        input_key = scr.getkey()
        if input_key in KEY_DIR:
            dir = KEY_DIR[input_key]
            mlib.move_peep(PEEPS, MAZE, player, dir)
            for i in range(1, len(PEEPS)):
                enemy = PEEPS[i]
                dx = player.x - enemy.x
                dy = player.y - enemy.y
                if enemy.hp/enemy.hp < 0.5:
                    edir = mlib.direction_from_vector(-dx, -dy)
                else:
                    edir = mlib.direction_from_vector(dx, dy)
                mlib.move_peep(PEEPS, MAZE, enemy, edir)


wrapper(main)
