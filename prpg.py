# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.move as mlib
import curses as clib
from lib.move import Direction
from lib.monsters import monster_by_name
from lib.players import player_by_name
from lib.model import Model
import random
from lib.constants import Color

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
    '%###########################.%',
    '%###########################.%',
    '%#############...............%',
    '%#############.##############%',
    '%#############.##############%',
    '%#########.........##########%',
    '%#####..................#####%',
    '%####....................####%',
    '%####....................####%',
    '%#####..................#####%',
    '%#########.........##########%',
    '%#############.##############%',
    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
]


PEEPS = [
    player_by_name('Bo Bo the Destroyer', x=1, y=2, hp=100, speed=33),
    monster_by_name('Thark', x=2, y=2, hp=10),
    monster_by_name('Spark', x=24, y=7, hp=50),
    monster_by_name('Brog', x=14, y=20, hp=200,)
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

CURSES_COLORS = {
    Color.BLACK: clib.COLOR_BLACK,
    Color.WHITE: clib.COLOR_WHITE,
    Color.BLUE: clib.COLOR_BLUE,
    Color.CYAN: clib.COLOR_CYAN,
    Color.MAGENTA: clib.COLOR_MAGENTA,
    Color.GREEN: clib.COLOR_GREEN,
    Color.YELLOW: clib.COLOR_YELLOW,
    Color.RED: clib.COLOR_RED,
}

# Term simplifies the interface with curses terminal. It narrows usage to only what is needed
class Term:
    def __init__(self, scr):
        self.scr = scr
        self.color_pairs = {} # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0

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

    def write_char(self, char, fg=Color.WHITE, bg=Color.BLACK):
        cpair = self.color_pair(fg, bg)
        self.scr.addstr(char, cpair)

    def color_pair(self, fg, bg):
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            clib.init_pair(self.color_pair_count, CURSES_COLORS[fg], CURSES_COLORS[bg])
            self.color_pairs[key] = clib.color_pair(self.color_pair_count)

        return self.color_pairs[key]

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
        term.move_to(len(model.maze[0]) + x_margin * 2, y_margin)
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
            term.write_char(p.char,  p.fgcolor, p.bgcolor)

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
                if peep == model.player:
                    if player_turn(screen) == 'q':
                        return 0     # QUIT GAME
                else:
                    monster_turn(model, peep)

                # update peeps list to living peeps
                model.peeps = [p for p in model.peeps if p.hp > 0]

                screen.repaint()


def player_turn(screen):
    while True:
        model = screen.model
        screen.repaint()  # update messages
        input_key = screen.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            if mlib.move_peep(model, model.player, direct):
                return input_key
            # else didn't spend turn
        elif input_key in ('\x11', '\x03'):
            return 'q'
        elif input_key == 'm':
            if len(model.peeps) > 1:
                player = model.player
                while model.player == player:
                    player = model.peeps[random.randint(0, len(model.peeps) - 1)]
                model.player = player
                model.message("You are now " + model.player.name)
            else:
                model.message("You have nothing in range to brain-swap with")
        else:
            model.message('unknown command: "' + input_key + '"')

        screen.repaint()  # update messages
        # continue with loop to get more input


def monster_turn(model, monster):
    dx = model.player.x - monster.x
    dy = model.player.y - monster.y
    if monster.hp/monster.maxhp < 0.3:
        direct = mlib.direction_from_vector(-dx, -dy) #If low health, run away
    else:
        direct = mlib.direction_from_vector(dx, dy)

    if mlib.move_peep(model, monster, direct):
        return

    # failed to move, try other directions (rotation 1,-1,2,-2,3,-3,4,-4)
    rotation = 1
    while rotation <= 4:
        d2 = mlib.direction_relative(direct, rotation)
        # model.print(monster.name, 'trying direction', d2)
        if mlib.move_peep(model, monster, d2):
            return
        d2 = mlib.direction_relative(direct, -rotation)
        # model.print(monster.name, 'trying direction', d2)
        if mlib.move_peep(model, monster, d2):
            return
        rotation += 1

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


clib.wrapper(main)
