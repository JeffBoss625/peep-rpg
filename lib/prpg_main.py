import lib.move as mlib
from lib.constants import Key
from lib.move import Direction
from lib.monsters import monster_by_name
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
    monster_by_name('Brog', pos=(14,20), hp=200,)
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

def player_turn(mainwin, new_peeps):
    end_with_key = ''   # ends the loop when set to a character key
    while not end_with_key:
        model = mainwin.model
        input_key = mainwin.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            mlib.move_peep(model, model.maze.player, direct)
            end_with_key = input_key
            # else didn't spend turn
        elif input_key == Key.CTRL_Q:
            end_with_key = 'q'
        elif input_key == 'm':
            if len(model.maze.peeps) > 1:
                player = model.maze.player
                while model.maze.player == player:
                    player = model.maze.peeps[random.randint(0, len(model.maze.peeps) - 1)]
                model.maze.player = player
                model.message("You are now " + model.maze.player.name)
            else:
                model.message("You have nothing in range to brain-swap with")
                # continue
        elif input_key == 'a':
            model.message('Where do you want to shoot?')
            sec_input_key = mainwin.get_key()
            while sec_input_key not in DIRECTION_KEYS:
                sec_input_key = mainwin.get_key()
                model.message('That is not a valid direction to shoot')
                model.message('Where do you want to shoot?')
            direct = DIRECTION_KEYS[sec_input_key]
            new_peeps.append(model.create_projectile(direct))
            model.message('Projectile shot')
            return input_key
        else:
            model.message(f'unknown command: "{input_key}"')
            # continue

    return end_with_key

def monster_turn(model, monster, new_peeps):
    if monster.move_tactic == 'straight':
        direct = monster.direct
        mlib.move_peep(model, monster, direct)
    elif monster.move_tactic == 'hunt':
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

def main(root_layout):
    model = PrpgModel(walls=MAZE, peeps=PEEPS, player=PEEPS[0], items=ITEMS)
    control = PrpgControl(root_layout, model)

    if sys.platform != "win32":
        signal.signal(signal.SIGWINCH, control.resize_handler)

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    turn_seq = mlib.calc_turn_sequence(model.maze.peeps, 1.0)
    while True:
        turn_state = { 'new_peeps':[], 'turn_index':0 }
        ret_status = execute_turns(control, turn_seq, turn_state)
        if ret_status == 'quit':
            return 0
        elif ret_status == 'died':
            model.banner('  YOU DIED! (press "q" to exit)')
            return 0
        else:
            if turn_state['new_peeps']:
                pass


def execute_turns(control, turn_seq, turn_state):
    model = control.model
    peeps = tuple(p for p in model.maze.peeps)
    ti = 0
    new_peeps = turn_state['new_peeps']
    while not new_peeps and ti < len(turn_seq):
        peep_indexes = turn_seq[ti]
        # this loop moves simultaneous peeps - all moves complete together (before adding new projectiles/peeps/etc)
        for peep_index in peep_indexes:
            # if there are new peeps in the new_peeps list, break out of loop.
            # When broken out of loop take remaining clicks to go through from the turns variable
            # Add those remaining turns into a function that adds the new peeps's turns to it
            peep = peeps[peep_index]
            if peep.hp <= 0:
                continue
            if model.is_player(peep):
                if player_turn(control, new_peeps) == 'q':
                    return 'quit'
            else:
                if monster_turn(model, peep, new_peeps) == 'q':
                    while control.get_key() not in ('q', Key.CTRL_Q):
                        pass
                    return 'died'

            # update peeps list to living peeps
            model.maze.peeps = [p for p in model.maze.peeps if p.hp > 0]

        ti += 1

    return ti
