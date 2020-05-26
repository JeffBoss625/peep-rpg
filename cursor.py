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

def draw_stats(screen, player):
    screen.write_lines([
        player.name,
        'hp:    ' + str(player.hp) + '/' + str(player.maxhp),
        'speed: ' + str(player.speed),
    ])

def draw_maze_area(screen, model):
    x, y = screen.get_xy()

    screen.write_lines(model.maze)

    for p in model.peeps:
        screen.move_to(x + p.x, y + p.y)
        screen.write_char(p.char)

    screen.move_to(x, y + len(model.maze))  # move cursor to end of maze


DIRECTION_KEYS = {
    'j': Direction.DOWN,
    'y': Direction.UP_LEFT,
    'k': Direction.UP,
    'u': Direction.UP_RIGHT,
    'l': Direction.RIGHT,
    'n': Direction.DOWN_RIGHT,
    'h': Direction.LEFT,
    'b': Direction.DOWN_LEFT,
}

# Screen simplifies the interface with curses. It narrows usage to only what is needed
class Screen:
    def __init__(self, scr):
        self.scr = scr

    def clear(self):
        self.scr.clear()

    def refresh(self):
        self.scr.refresh()

    def get_xy(self):
        y, x = self.scr.getyx()
        return x, y

    # Relative move of cursor
    def move(self, dx, dy):
        y, x = self.scr.getyx()
        self.scr.move(y + dy, x + dx)

    # Absolute move of cursor
    def move_to(self, x, y):
        self.scr.move(y, x)

    def write_lines(self, lines):
        scr = self.scr
        y, x = scr.getyx()
        for i, line in enumerate(lines):
            scr.move(y+i, x)
            scr.addstr(line)

        scr.move(y + len(lines), x)

    def write_char(self, char):
        self.scr.addch(char)


def draw_screen(screen, model, x_margin, y_margin):
    screen.clear()

    screen.move_to(x_margin, y_margin)
    draw_stats(screen, model.player)

    screen.move(0, y_margin)
    draw_maze_area(screen, model)

    screen.move(0, y_margin)
    screen.write_lines(model.messages[-12:])

    screen.move_to(0, 0)

    screen.refresh()


def main(scr):
    screen = Screen(scr)
    model = Model(peeps=PEEPS, maze=MAZE, player=PEEPS[0])

    input_key = 0
    turn = 0
    while input_key != 'q':
        turn += 1
        draw_screen(screen, model, 3, 3)

        # GET AND HANDLE PLAYER MOVE
        input_key = scr.getkey()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            # PLAYER TURN
            msg = mlib.move_peep(model, model.player, direct)
            model.message(msg)

            # MONSTER TURNS
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
