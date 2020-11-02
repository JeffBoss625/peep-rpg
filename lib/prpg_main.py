import lib.move as mlib
from lib.constants import Key
from lib.move import Direction
from lib.monsters import monster_by_name
from lib.peep_types import create_peep
from lib.players import player_by_name
from lib.prpg_control import PrpgControl
from lib.prpg_model import PrpgModel
import random
import sys
import signal

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
    player_by_name('Super Dad', pos=(1,2), hp=40),
    monster_by_name('Thark', pos=(2,2), hp=10),
    monster_by_name('Spark', pos=(24,7), hp=50),
    monster_by_name('Brog', pos=(14,20), hp=200),
    create_peep('big bird', name='Beaky', pos=(18,4)),
    create_peep('giant rat', name='Scriggle', pos=(19,4)),
]
ITEMS = [

]

DIRECTION_KEYS = {
    '.': Direction.CENTER,
    'j': Direction.DOWN,
    'y': Direction.UP_LEFT,
    'k': Direction.UP,
    'u': Direction.UP_RIGHT,
    'l': Direction.RIGHT,
    'n': Direction.DOWN_RIGHT,
    'h': Direction.LEFT,
    'b': Direction.DOWN_LEFT,
}


def player_turn(control):
    while True:
        model = control.model
        maze = model.maze
        player = maze.player
        input_key = control.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            if mlib.move_peep(model, maze.player, direct):
                return input_key
            # else didn't spend turn
        elif input_key == Key.CTRL_Q:
            return 'q'
        elif input_key == 'm':
            if len(maze.peeps) > 1:
                while maze.player == player:
                    maze.player = player = maze.peeps[random.randint(0, len(maze.peeps) - 1)]
                model.message("You are now " + player.name)
            else:
                model.message("You have nothing in range to brain-swap with")
                # continue
        elif input_key == 'a':
            maze.cursorvis = 1
            maze.cursorpos = (3, 3)
            model.message('Where do you want to shoot?')
            sec_input_key = control.get_key()
            while sec_input_key not in DIRECTION_KEYS:
                model.message('That is not a valid direction to shoot')
            maze.create_projectile(player, 'fire breath', DIRECTION_KEYS[sec_input_key])

            return input_key
        else:
            model.message(f'unknown command: "{input_key}"')
            # continue

def monster_turn(control, monster):
    model = control.model
    maze = model.maze
    player = maze.player
    if monster.move_tactic == 'straight':
        direct = monster.direct
        mlib.move_peep(model, monster, direct)
    elif monster.move_tactic == 'hunt':
        dx = player.pos[0] - monster.pos[0]
        dy = player.pos[1] - monster.pos[1]
        if player.hp <= 0:
            control.player_died()
            return False

        if monster.hp/monster.maxhp < 0.3:
            direct = mlib.direction_from_vector(-dx, -dy)  # If low health, run away
        else:
            direct = mlib.direction_from_vector(dx, dy)

        if mlib.move_peep(model, monster, direct):
            return True

        # failed to move, try other directions (rotation 1,-1,2,-2,3,-3,4,-4)
        rotation = 1
        while rotation <= 4:
            d2 = mlib.direction_relative(direct, rotation)
            # model.print(monster.name, 'trying direction', d2)
            if mlib.move_peep(model, monster, d2):
                return True
            d2 = mlib.direction_relative(direct, -rotation)
            # model.print(monster.name, 'trying direction', d2)
            if mlib.move_peep(model, monster, d2):
                return True
            rotation += 1

    return True

def main(root_layout):
    model = PrpgModel(walls=MAZE, peeps=PEEPS, player=PEEPS[0], items=ITEMS)
    maze = model.maze
    control = PrpgControl(root_layout, model)

    if sys.platform != "win32":
        signal.signal(signal.SIGWINCH, control.resize_handler)

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    maze.elapse_time()
    while execute_turn_seq(control):
        maze.elapse_time()


def execute_turn_seq(control):
    model = control.model
    maze = model.maze
    while not maze.new_peeps and maze.ti < len(maze.turn_seq):
        peep_indexes = maze.turn_seq[maze.ti]
        # this loop moves simultaneous peeps - all moves complete together (before adding new projectiles/peeps/etc)
        for peep_index in peep_indexes:
            # if there are new peeps in the new_peeps list, break out of loop.
            # When broken out of loop take remaining clicks to go through from the turns variable
            # Add those remaining turns into a function that adds the new peeps's turns to it
            peep = maze.peeps[peep_index]
            if peep.hp <= 0:
                continue
            if model.is_player(peep):
                if player_turn(control) == 'q':
                    return False
            else:
                if not monster_turn(control, peep):
                    return False

        maze.ti += 1

    return True
