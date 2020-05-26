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
    player_by_name('Bo Bo the Destroyer', x=1, y=2, hp=10, speed=33),
    monster_by_name('Thark', x=2, y=2, hp=10),
    monster_by_name('Spark', x=24, y=7, hp=50),
]

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

# Term simplifies the interface with curses terminal. It narrows usage to only what is needed
class Term:
    def __init__(self, scr):
        self.scr = scr

    def clear(self):
        self.scr.clear()

    def refresh(self):
        self.scr.refresh()

    def get_key(self):
        return self.scr.getkey()

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

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class Screen:
    def __init__(self, term, model):
        self._term = term
        self.model = model
        self.model.out = self  # allow the model itself to be used for term printed output

    # print messages and standard output
    def print(self, *args):
        line = ' '.join([str(a) for a in args])
        self.model.message(line)
        self.repaint()

    def get_key(self):
        return self._term.get_key()

    # repaint the entire screen - all that is visible
    def repaint(self):
        term = self._term
        model = self.model
        x_margin = 3
        y_margin = 3
        term.clear()

        term.move_to(x_margin, y_margin)
        self._draw_stats()

        term.move(0, y_margin)
        self._draw_maze_area()

        term.move(0, y_margin)
        term.move_to(3, 20)
        term.write_lines(model.messages[-12:])

        term.move_to(0, 0)
        term.refresh()

    def _draw_stats(self):
        p = self.model.player
        self._term.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])

    def _draw_maze_area(self):
        term = self._term
        model = self.model
        x, y = term.get_xy()

        term.write_lines(model.maze)

        for p in model.peeps:
            term.move_to(x + p.x, y + p.y)
            term.write_char(p.char)

        term.move_to(x, y + len(model.maze))  # move cursor to end of maze

def main(scr):
    model = Model(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
    screen = Screen(Term(scr), model)

    screen.repaint()

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    while True:
        peeps = [p for p in model.peeps]
        turns = mlib.calc_turn_sequence(peeps)

        for ti, peep_indexes in enumerate(turns):
            for pi, peep_index in enumerate(peep_indexes):
                peep = peeps[peep_index]
                if peep.type == 'player':
                    if player_turn(screen) == 'q':
                        return      # QUIT GAME
                else:
                    monster_turn(model, peep)

                # update peeps list to living peeps
                model.peeps = [p for p in model.peeps if p.hp > 0]

                screen.repaint()


def player_turn(screen):
    model = screen.model
    while True:
        input_key = screen.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            if mlib.move_peep(model, model.player, direct):
                return input_key
            # else didn't spend turn
        elif input_key == 'q':
            return 'q'
        else:
            model.print('unknown command: "' + input_key + '"')

        # continue with loop to get more input

def monster_turn(model, monster):
    dx = model.player.x - monster.x
    dy = model.player.y - monster.y
    if monster.hp/monster.maxhp < 0.2:
        edir = mlib.direction_from_vector(-dx, -dy) #If low health, run away
    else:
        edir = mlib.direction_from_vector(dx, dy)
    mlib.move_peep(model, monster, edir)

#   while input_key != 'q':
#       GET PLAYER AND MONSTER TURNS (turn_sequence)
#       For each set of turns:
#           For each turn (in simultaneous set):
#               if it's a monster, MONSTER TAKES TURN
#               else (player), get input (input_key = scr.getkey()):
#                   if input is a move:
#                       MOVE PLAYER
#                   else if it's quit (q), stop program
#                   else... add message, "action not handled"
#               DRAW SCREEN CONTENTS


wrapper(main)
