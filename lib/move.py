from lib.attack import attack_dst, choose_attack
from lib.direction import Direction, direction_to_dxdy, direction_from_vector
from lib.pclass import check_states
from lib.peep_types import create_peep


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
    direct = direction_from_vector(peep.pos[0]-dst_pos[0], peep.pos[1]-dst_pos[1])
    peep.direct = direct
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
            src_attack = choose_attack(peep, 'melee')
            if src_attack:
                if attack_dst(peep, tgt_peep, src_attack, game):
                    # hit!
                    return True
        if peep != game.player:
            if tgt_peep == game.player:
                src_attack = choose_attack(peep, 'melee')
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
                    if s.handle_move_into_monster(peep, tgt_peep, s, game):
                        skip = True
                        return True
                if skip is False:
                    src_attack = choose_attack(peep, 'melee')
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
                src_attack = choose_attack(peep, 'melee')
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

def move_along_path(monster, game):
    if monster.pos_i < len(monster.pos_path) - 1:
        monster.pos_i += 1
        dst_pos = monster.pos_path[monster.pos_i]
        move_peep(game, monster, dst_pos)
    else:
        game.message(f'{monster.name} hits the ground')
        monster.hp = 0  # todo: convert to item with chance of breaking
    return True

def monster_hunt(monster, player, control, choose_monster_target):
    game = control.game_model
    if monster._hunt_target:
        if monster._hunt_target.hp <= 0:
            monster._hunt_target = choose_monster_target(monster, control)
    else:
        monster._hunt_target = choose_monster_target(monster, control)
    dx = monster._hunt_target.pos[0] - monster.pos[0]
    dy = monster._hunt_target.pos[1] - monster.pos[1]
    if player.hp <= 0:
        control.player_died()
        return False

    if monster.hp / monster.maxhp < 0.2:
        direct = direction_from_vector(-dx, -dy)  # If low health, run away
    else:
        direct = direction_from_vector(dx, dy)

    dst_pos = adjacent_pos(monster.pos, direct)
    if move_peep(game, monster, dst_pos):
        return True

    # failed to move, try other directions (rotation 1,-1,2,-2,3,-3,4,-4)
    rotation = 1
    while rotation <= 4:
        d2 = direction_relative(direct, rotation)
        dst_pos = adjacent_pos(monster.pos, d2)
        if move_peep(game, monster, dst_pos):
            return True
        d2 = direction_relative(direct, -rotation)
        dst_pos = adjacent_pos(monster.pos, d2)
        if move_peep(game, monster, dst_pos):
            return True
        rotation += 1
        if abs(rotation) >= 5:
            monster._tics = monster._tics - 1 / monster.speed
            continue