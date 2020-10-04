import lib.move as mlib
import lib.attack as alib
from lib.constants import Key
from lib.move import Direction
from lib.monsters import monster_by_name
from lib.players import player_by_name
from lib.prpg_screen import PrpgControl
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
    player_by_name('Bo Bo the Destroyer', pos=(1,2), hp=100, speed=33),
    monster_by_name('Thark', pos=(2,2), hp=10),
    monster_by_name('Spark', pos=(24,7), hp=50),
    monster_by_name('Brog', pos=(14,20), hp=200,)
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

def player_turn(screen):
    while True:
        model = screen.model
        input_key = screen.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            if mlib.move_peep(model, model.maze.player, direct):
                return input_key
            # else didn't spend turn
        elif input_key == Key.CTRL_Q:
            return 'q'
        # elif input_key in ('=', '+', '-'):
        #     return input_key
        elif input_key == 'm':
            if len(model.maze.peeps) > 1:
                player = model.maze.player
                while model.maze.player == player:
                    player = model.maze.peeps[random.randint(0, len(model.maze.peeps) - 1)]
                model.maze.player = player
                model.message("You are now " + model.maze.player.name)
            else:
                model.message("You have nothing in range to brain-swap with")
        elif input_key == 'a':
            model.message('Where do you want to shoot?')
            sec_input_key = screen.get_key()
            while sec_input_key not in DIRECTION_KEYS:
                sec_input_key = screen.get_key()
                model.message('That is not a valid direction to shoot')
                model.message('Where do you want to shoot?')
            direct = DIRECTION_KEYS[sec_input_key]
            alib.create_projectile(direct, model)
            model.message('Projectile shot')
        else:
            model.message('unknown command: "{}"'.format(input_key))

        # continue with loop to get more input


def monster_turn(model, monster):
    if monster.move_tactic == 'straight':
        direct = monster.direct
        mlib.move_peep(model, monster, direct)
    elif monster.move_tactic == 'seek':
        dx = model.maze.player.pos[0] - monster.pos[0]
        dy = model.maze.player.pos[1] - monster.pos[1]
        if model.maze.player.hp <= 0:
            return 'q'
        if monster.hp/monster.maxhp < 0.3:
            direct = mlib.direction_from_vector(-dx, -dy)  # If low health, run away
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

def main(root):
    root.window.curses.raw()
    model = PrpgModel(walls=MAZE, peeps=PEEPS, player=PEEPS[0])
    control = PrpgControl(root, model)

    if sys.platform != "win32":
        register_resize_handler(control)

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    while True:
        peeps = tuple(p for p in model.maze.peeps)
        turns = mlib.calc_turn_sequence(model.maze.peeps)

        for peep_indexes in turns:
            for peep_index in peep_indexes:
                # if there are new peeps in the new_peeps list, break out of loop.
                # When broken out of loop take remaining clicks to go through from the turns variable
                # Add those remaining turns into a function that adds the new peeps's turns to it
                peep = peeps[peep_index]
                if peep.hp <= 0:
                    continue
                if model.is_player(peep):
                    if player_turn(control) == 'q':
                        return 0     # QUIT GAME
                    # elif key_input in ('=','+'):
                    #     term = root.window.curses.term
                    #     term.dim.w += 5
                    #     term.dim.h += 2
                    #     screen.size_to_terminal()
                else:
                    if monster_turn(model, peep) == 'q':
                        model.banner('  YOU DIED! (press "q" to exit)')
                        while control.get_key() not in ('q', Key.CTRL_Q):
                            pass
                        return 0

                # update peeps list to living peeps
                model.maze.peeps = [p for p in model.maze.peeps if p.hp > 0]

                # model.undirty()

def register_resize_handler(control):
    def resize_handler(_signum, _frame):
        try:
            if control.root_layout.size_to_terminal():
                control.main_screen.paint(force=True)

        except Exception as e:
            control.root_layout.log(e)

    signal.signal(signal.SIGWINCH, resize_handler)