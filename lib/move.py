from lib.attack import attack_dst, choose_melee_attack
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
    dst = peep_at_pos(game.maze_model.peeps, dst_pos)
    if not dst:
        # players and ammo strike wall
        char = game.maze_model.wall_at(dst_pos)
        if char:
            if peep.type == 'projectile':
                wall = create_wally(game.maze_model, dst_pos)
                dst = wall
            else:
                return False # peep tried wall - did not move

    if dst:
        src_attack = choose_melee_attack(peep)
        if src_attack:
            if attack_dst(peep, dst, src_attack, game):
                # hit!
                return True
            else:
                # missed
                if peep.type is not 'projectile':
                    # used up move with miss
                    return True
                # else continue to move (below)

    # move
    peep.pos = dst_pos
    peep._tics = peep._tics - 1/peep.speed
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
