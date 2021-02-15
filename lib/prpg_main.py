import lib.move as mlib
from lib.attack import peep_regenhp, choose_ranged_attack
from lib.calc import target_list
from lib.constants import Key
from lib.move import Direction
import random
import sys
import signal
from lib.calc import distance

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
            dst = mlib.adjacent_pos(maze.player.pos, DIRECTION_KEYS[input_key])
            if mlib.move_peep(dungeon, maze.player, dst):
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
            player_aim(control)
            return input_key
        else:
            dungeon.message(f'unknown command: "{input_key}"')
            # continue

def player_aim(control):
    dungeon = control.model
    maze = dungeon.maze
    player = maze.player
    maze.cursorvis = 1
    maze.cursorpos = (3, 3)
    dungeon.message('Where do you want to shoot? (* to target)')
    key = control.get_key()
    target = 'UNSET'
    while target == 'UNSET':
        if key in DIRECTION_KEYS and key != '.':
            target = target_for_direction(player.pos, DIRECTION_KEYS[key], maze)
        elif key == '*':
            target = choose_target(control, player)
        elif key == 'q' or key == Key.CTRL_Q:
            target = None
        else:
            dungeon.message(f'{key} is not a valid direction to shoot')
            key = control.get_key()
            continue

    if target is not None:
        target_pos = getattr(target, 'pos', target)     # target may be a peep or a position
        path = list(line_points(player.pos, target_pos))[0:]
        attack = choose_ranged_attack(player)
        maze.create_projectile(player, attack.name, path, (attack.projectile_attack(),))


def monster_turn(control, monster):
    dungeon = control.model
    maze = dungeon.maze
    player = maze.player
    monster.hp += peep_regenhp(monster.maxhp, monster.speed, monster.regen_fac)
    ranged_attack = choose_ranged_attack(monster)
    if monster.type != 'projectile':
        if ranged_attack is not None:
            if is_in_sight(monster, player.pos, maze.walls) and distance(monster.pos, player.pos) < ranged_attack.range:
                path = list(line_points(monster.pos, player.pos))
                maze.create_projectile(player, ranged_attack.name, path, (ranged_attack.projectile_attack(),))
                return True
    if monster.hp > monster.maxhp: monster.hp = monster.maxhp
    if monster.move_tactic == 'pos_path':
        if monster.pos_i < len(monster.pos_path) - 1:
            monster.pos_i += 1
            dst_pos = monster.pos_path[monster.pos_i]
            mlib.move_peep(dungeon, monster, dst_pos)
        else:
            dungeon.message(f'{monster.name} hits the ground')
            monster.hp = 0  # todo: convert to item with chance of breaking
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

        dst_pos = mlib.adjacent_pos(monster.pos, direct)
        if mlib.move_peep(dungeon, monster, dst_pos):
            return True

        # failed to move, try other directions (rotation 1,-1,2,-2,3,-3,4,-4)
        rotation = 1
        while rotation <= 4:
            d2 = mlib.direction_relative(direct, rotation)
            # model.print(monster.name, 'trying direction', d2)
            dst_pos = mlib.adjacent_pos(monster.pos, d2)
            if mlib.move_peep(dungeon, monster, dst_pos):
                return True
            d2 = mlib.direction_relative(direct, -rotation)
            # model.print(monster.name, 'trying direction', d2)
            dst_pos = mlib.adjacent_pos(monster.pos, d2)
            if mlib.move_peep(dungeon, monster, dst_pos):
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


# Interactively select a target to shoot
# Return a selected peep or position (int, int) for the target.
def choose_target(control, src_peep):
    dungeon = control.model
    maze = dungeon.maze
    top = f'*: choose next, t: target, q: quit'
    targets = target_list(src_peep, maze.peeps)  # peeps sorted in order of distance and relative angle from origin
    ti = next_target(src_peep, targets, maze.walls, 0)  # return None if no target
    if ti == -1:
        dungeon.message('No targets in sight')
        return None     # todo: start cursor on self to allow manual selection
    while True:
        maze.target_path = tuple(line_points(src_peep.pos, targets[ti].pos))    # draws the target path
        dungeon.banner([top, f'Aiming at {targets[ti].name}'])
        input_key = control.get_key()
        if input_key == 't':
            maze.target_path = ()
            dungeon.banner('')
            return targets[ti]
        elif input_key == 'q' or input_key == Key.CTRL_Q:
            maze.target_path = ()
            dungeon.banner('')
            return None
        elif input_key == '*':
            ti = next_target(src_peep, targets, maze.walls, ti + 1)
        else:
            dungeon.message(f'unknown command "{input_key}"')


# return the index of the next target in the list (by distance from origin)
def next_target(origin, targets, walls, starti):
    num_checks = len(targets)
    current = starti % len(targets)
    while num_checks > 0:
        t = targets[current]
        if is_in_sight(origin, t.pos, walls):
            return current
        num_checks -= 1
        current = (current + 1) % len(targets)

    return -1

def is_in_sight(origin, pos, walls):
    path = tuple(line_points(origin.pos, pos))
    for p in path:
        row = walls.text[p[1]]
        if row[p[0]] in ['#', '%']:
            return False
    return True

def target_for_direction(origin, direction, maze):
    mx = maze.max_x()
    my = maze.max_y()
    x, y = origin
    if direction == Direction.UP:
        y = 0
    elif direction == Direction.UP_RIGHT:
        dx = mx - x
        dy = my - y
        d = dx if dx < dy else dy
        x = x + d
        y = y - d
    elif direction == Direction.RIGHT:
        x = mx
    elif direction == Direction.DOWN_RIGHT:
        dx = mx - x
        dy = my - y
        d = dx if dx < dy else dy
        x = x + d
        y = y + d
    elif direction == Direction.DOWN:
        y = my
    elif direction == Direction.DOWN_LEFT:
        dx = mx - x
        dy = my - y
        d = dx if dx < dy else dy
        x = x - d
        y = y + d
    elif direction == Direction.LEFT:
        x = 0
    elif direction == Direction.UP_LEFT:
        dx = mx - x
        dy = my - y
        d = dx if dx < dy else dy
        x = x - d
        y = y - d
    return x, y