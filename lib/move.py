from lib.attack import attack_dst, choose_attack
from lib.pclass import check_states
from lib.peep_types import create_peep

# x and y modifiers for each directions on keypad
# Direction constants match keypad layout 1-9
#       7 8 9
#       4 5 6
#       1 2 3
class Direction: DOWN_LEFT, DOWN, DOWN_RIGHT, LEFT, CENTER, RIGHT, UP_LEFT, UP, UP_RIGHT = range(1,10)


X_MODIFIERS = {
    Direction.UP_LEFT: -1,
    Direction.LEFT: -1,
    Direction.DOWN_LEFT: -1,
    Direction.UP: 0,
    Direction.CENTER: 0,
    Direction.DOWN: 0,
    Direction.UP_RIGHT: 1,
    Direction.RIGHT: 1,
    Direction.DOWN_RIGHT: 1,
}

Y_MODIFIERS = {
    Direction.UP_LEFT: -1,
    Direction.UP: -1,
    Direction.UP_RIGHT: -1,
    Direction.LEFT: 0,
    Direction.CENTER: 0,
    Direction.RIGHT: 0,
    Direction.DOWN_LEFT: 1,
    Direction.DOWN: 1,
    Direction.DOWN_RIGHT: 1,
}


def direction_to_dxdy(direction):
    return X_MODIFIERS[direction], Y_MODIFIERS[direction]


def direction_from_vector(dx, dy):
    ret = Direction.CENTER

    if dx < 0 and dy < 0:
        ret = Direction.UP_LEFT
    if dx == 0 and dy < 0:
        ret = Direction.UP
    if dx > 0 and dy < 0:
        ret = Direction.UP_RIGHT
    if dx > 0 and dy == 0:
        ret = Direction.RIGHT
    if dx > 0 and dy > 0:
        ret = Direction.DOWN_RIGHT
    if dx == 0 and dy > 0:
        ret = Direction.DOWN
    if dx < 0 and dy > 0:
        ret = Direction.DOWN_LEFT
    if dx < 0 and dy == 0:
        ret = Direction.LEFT
    return ret

# Direction constants match keypad layout
#       7 8 9
#       4 5 6
#       1 2 3


# Direction constants in clockwise order for finding closest, second closest, third closest... direction from
# a given direction
DIRECT_ROTATION = [
    Direction.UP, Direction.UP_RIGHT,
    Direction.RIGHT, Direction.DOWN_RIGHT,
    Direction.DOWN, Direction.DOWN_LEFT,
    Direction.LEFT, Direction.UP_LEFT,
]

def direction_relative(direct, rotation):
    si = DIRECT_ROTATION.index(direct)
    i = (si + rotation) % len(DIRECT_ROTATION)
    return DIRECT_ROTATION[i]

def adjacent_pos(src_pos, direct):
    dx, dy = direction_to_dxdy(direct)
    return src_pos[0] + dx, src_pos[1] + dy

# Handle move and collisions with monsters. Return True if move or attack was executed, false, if the move
# failed (hit a wall)
def move_peep(game, peep, dst_pos):
    tgt_peep = game.maze_model.peep_at(dst_pos)
    # todo: separate projectile move from monster melee attack (speed and handling)
    # if peep.type == 'projectile':
    #   ...
    # else:
    #   ...

    char = game.maze_model.wall_at(dst_pos)
    if char and not tgt_peep:
        # players and ammo strike wall
        if peep.type == 'projectile':
            wall = create_wally(game.maze_model, dst_pos)
            tgt_peep = wall
        else:
            return False # peep tried wall - did not move

    if tgt_peep:
        if peep.type == 'projectile':
            src_attack = choose_attack(peep, True)
            if src_attack:
                if attack_dst(peep, tgt_peep, src_attack, game):
                    # hit!
                    return True
        if peep != game.player:
            if tgt_peep == game.player:
                src_attack = choose_attack(peep, True)
                if src_attack:
                    if attack_dst(peep, tgt_peep, src_attack, game):
                        # hit!
                        return True
                    else:
                        # missed
                        if peep.type != 'projectile':
                            # used up move with miss
                            return True
                        # else continue to move (below)
            else:
                return False # monster attacking monster
        else:
            skip = False
            if peep.states:
                for s in peep.states:
                    if s.handle_move_into_monster(peep, tgt_peep, game):
                        skip = True
                        return True
                if skip is False:
                    src_attack = choose_attack(peep, True)
                    if src_attack:
                        if attack_dst(peep, tgt_peep, src_attack, game):
                            # hit!
                            return True
                        else:
                            # missed
                            if peep.type != 'projectile':
                                # used up move with miss
                                return True
                            # else continue to move (below)
            else:
                src_attack = choose_attack(peep, True)
                if src_attack:
                    if attack_dst(peep, tgt_peep, src_attack, game):
                        # hit!
                        return True
                    else:
                        # missed
                        if peep.type != 'projectile':
                            # used up move with miss
                            return True
                        # else continue to move (below)

    # move
    direct = direction_from_vector(peep.pos[0]-dst_pos[0], peep.pos[1]-dst_pos[1])
    peep.direct = direct
    peep.pos = dst_pos
    peep._tics = peep._tics - 1/peep.speed
    for s in peep.states:      #todo:Should subscribe to peep aging events
        peeps = game.maze_model.peeps
        inc = round(1/peeps[0].speed, 5)
        check_states(peep, s, inc)
    return True


def peep_at_pos(peeps, pos):
    for p in peeps:
        if p.pos == pos and p.hp > 0:
            return p
    return None

def create_wally(maze, pos):
    char = maze.wall_at(pos)
    if char == '#':
        wall = create_peep('wall', 'FIGHTER', 'Wally', pos=pos)
    elif char == '%':
        wall = create_peep('permanent wall', 'FIGHTER', '*WALLY*', pos=pos)
    else:
        raise ValueError(f'no wall located at {pos}')

    maze.walls.replace_region(pos[0], pos[1], ['.'])
    maze.peeps.append(wall)
    return wall
