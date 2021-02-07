import lib.move as mlib
from lib.attack import peep_regenhp
from lib.calc import target_list
from lib.constants import Key
from lib.move import Direction
import random
import sys
import signal

from lib.target import line_points

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
    player = control.model.maze.player
    player.hp += peep_regenhp(player.maxhp, player.speed, player.regen_fac)
    if player.hp > player.maxhp: player.hp = player.maxhp
    while True:
        dungeon = control.model
        maze = dungeon.maze
        player = maze.player
        input_key = control.get_key()
        if input_key in DIRECTION_KEYS:
            direct = DIRECTION_KEYS[input_key]
            if mlib.move_peep(dungeon, maze.player, direct):
                return input_key
            # else didn't spend turn
        elif input_key == Key.CTRL_Q:
            return 'q'
        elif input_key == 'm':
            morph_peeps = list(p for p in maze.peeps if p.type == 'monster')
            if len(morph_peeps) > 1:
                while maze.player == player:
                    player = morph_peeps[random.randint(0, len(morph_peeps) - 1)]
                maze.player = player
                dungeon.message("You are now " + player.name)
            else:
                dungeon.message("You have nothing in range to brain-swap with")
                # continue
        elif input_key == 'a':
            maze.cursorvis = 1
            maze.cursorpos = (3, 3)
            dungeon.message('Where do you want to shoot? (* to target)')
            sec_input_key = control.get_key()
            target = None
            while target is None:
                if sec_input_key in DIRECTION_KEYS and sec_input_key != '.':
                    target = target_for_direction(sec_input_key)
                elif sec_input_key == '*':
                    target = select_target(control)
                else:
                    dungeon.message('That is not a valid direction to shoot')
                    sec_input_key = control.get_key()
            maze.create_projectile(player, 'arrow', target)

            return input_key
        else:
            dungeon.message(f'unknown command: "{input_key}"')
            # continue

def monster_turn(control, monster):
    model = control.model
    maze = model.maze
    player = maze.player
    monster.hp += peep_regenhp(monster.maxhp, monster.speed, monster.regen_fac)
    if monster.hp > monster.maxhp: monster.hp = monster.maxhp
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

def main(control, dungeon):
    if sys.platform != "win32" and hasattr(control, 'resize_handler'):
        signal.signal(signal.SIGWINCH, control.resize_handler)

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    dungeon.maze.elapse_time()
    while execute_turn_seq(control):
        dungeon.maze.elapse_time()


def execute_turn_seq(control):
    dungeon = control.model
    maze = dungeon.maze
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
            if dungeon.is_player(peep):
                if player_turn(control) == 'q':
                    return False
            else:
                if not monster_turn(control, peep):
                    return False

        maze.ti += 1

    return True


def select_target(control, origin):
    dungeon = control.model
    maze = dungeon.maze
    peeps = maze.peeps
    positions = []
    for p in maze.peeps:
        positions.append(peeps[p].pos)
    targets = target_list(positions, origin)
    target_positions = list((t[2], positions[t[2]]) for t in targets) # (peep index, peep position) tuples
    current = next_target(0, positions, maze.walls, origin)     # return -1 if no target
    input_key = None
    pathtotarget = None
    while input_key != 't':

        # draw path to current target
        # Advance to the next target in the list (wraparound)
        current = next_target(current, positions, maze.walls, origin)  # return -1 if no target
        # get player input

def next_target(start, target_positions, walls, origin):
    num_checks = len(target_positions)
    current = start
    ret = None
    while num_checks > 0:
        ti, pos = target_positions[current]
        if pos != origin and is_in_sight(origin, pos, walls):
            ret = line_points(origin, pos)
        num_checks -= 1
        current = (current + 1) % len(target_positions)

    return ret

def is_in_sight(origin, pos, walls):
    path = line_points(origin, pos)
    return True