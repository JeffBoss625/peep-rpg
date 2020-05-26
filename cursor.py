# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.move as mlib
from curses import wrapper
from lib.move import Direction
from lib.monsters import monster_by_name
from lib.players import player_by_name
from lib.model import Model

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


PEEPS = [
    player_by_name('Bo Bo the Destroyer', x=1, y=2, hp=10),
    monster_by_name('Thark', x=2, y=2, hp=10),
    monster_by_name('Spark', x=24, y=7, hp=50),
]

def draw_stats(scr, player):
    y, x = scr.getyx()
    scr.move(y, x)
    scr.addstr(player.name)
    scr.move(y+1, x)
    scr.addstr('hp:    ' + str(player.hp) + '/' + str(player.maxhp))
    scr.move(y+2, x)
    scr.addstr('speed: ' + str(player.speed))


def draw_maze(scr, maze):
    y, x = scr.getyx()
    for i, line in enumerate(maze):
        scr.move(y+i, x)
        scr.addstr(line)

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

def draw_screen(scr, model, xoff, yoff):
    scr.clear()

    scr.move(yoff, xoff)
    draw_stats(scr, model.player)
    yoff += 8       # stats height

    scr.move(yoff, xoff)
    draw_maze(scr, MAZE)

    for p in model.peeps:
        scr.move(yoff,xoff)
        draw_peep(scr, p)

    yoff += len(MAZE) + MARGIN_SIZE
    scr.move(yoff, xoff)
    draw_messages(scr, model.messages[-12:])

    scr.move(0,0)
    scr.refresh()


def main(scr):
    model = Model(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
    scr.clear()

    input_key = 0
    turn = 0
    while input_key != 'q':
        turn += 1
        draw_screen(scr, model, 10, 2)

        # GET AND HANDLE PLAYER MOVE
        input_key = scr.getkey()
        if input_key in KEY_DIR:
            dir = KEY_DIR[input_key]

            # MOVE PLAYER
            msg = mlib.move_peep(model, model.player, dir)
            model.message(msg)

            # MOVE MONSTERS
            for i in range(1, len(model.peeps)):
                monster_turn(model, model.peeps[i])
            model.peeps = [p for p in model.peeps if p.hp > 0]
            # Before Drawing, peeps = peeps-without-dead-guys (new list)

def monster_turn(model, monster):
    dx = model.player.x - monster.x
    dy = model.player.y - monster.y
    if monster.hp/monster.maxhp < 0.2:
        edir = mlib.direction_from_vector(-dx, -dy) #If low health, run away
    else:
        edir = mlib.direction_from_vector(dx, dy)
    msg = mlib.move_peep(model, monster, edir)
    model.message(msg)

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
