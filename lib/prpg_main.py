import lib.move as mlib
from lib import dungeons
from lib.attack import choose_attack
from lib.calc import target_list
from lib.constants import Key
from lib.items import clothes
from lib.items.item import Item
from lib.move import Direction
import random
import sys
import signal
from lib.calc import distance
from lib.pclass import PABILITIES_BY_NAME, pability_by_name, activate_ability
from lib.prpg_control import PrpgControl
from lib.constants import GAME_SETTINGS
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
    result = None
    while not result:
        input_key = control.get_key()
        if input_key in control.game_model.macros:
            for key in control.game_model.macros[input_key]:
                result = do_player_turn(control, key)
        else:
            result = do_player_turn(control, input_key)

    return result

# returns None if the turn didn't happen and needs more input
def do_player_turn(control, input_key):
    game = control.game_model
    mm = game.maze_model
    player = game.player
    if input_key in DIRECTION_KEYS:
        dst_pos = mlib.adjacent_pos(game.player.pos, DIRECTION_KEYS[input_key])
        if mlib.move_peep(game, game.player, dst_pos):
            post_player_move(control)
            return input_key
        # else didn't spend turn
    elif input_key == Key.CTRL_Q:
        return 'q'

    elif input_key == 'm':
        morph_peeps = list(p for p in mm.peeps if p.type == 'monster')
        if len(morph_peeps) > 1:
            while game.player == player:
                player = morph_peeps[random.randint(0, len(morph_peeps) - 1)]
            game.set_player(player)
            game.message("You are now " + player.name)
        else:
            game.message("You have nothing in range to brain-swap with")
    elif input_key == 'A':
        if player.aabilities:
            game.banner(['choose an ability to use'])
            ability = control.choose_item('What ability will you use', player.aabilities)
            if not activate_ability(player, ability):
                game.message(f'Ability on cooldown')
            else:
                game.message(f'Used ability')
        else:
            game.message('No ability to activate')

    elif input_key == 'a':
        attack = choose_attack(player, False)
        if attack:
            player_aim(attack, control)
        else:
            game.message(f'{player.name} has no ranged attack')
        return input_key
    elif input_key == '>':

        if mm.char_at(*player.pos) == GAME_SETTINGS.CHARS.STAIR_DOWN:
            return input_key
        else:
            game.message(f'you are not standing at a down staircase')

    elif input_key == '<':
        if mm.char_at(*player.pos) == GAME_SETTINGS.CHARS.STAIR_UP:
            return input_key
        else:
            game.message(f'you are not standing at an up staircase')

    elif input_key == 'w':
        if not player.stuff:
            game.message("you don't have any stuff to wear")
        else:
            item = control.choose_item('what will you wear?', player.stuff)
            if item:
                slots = player.body.slots_for(item.fit_info)
                if slots:
                    player.put_item(slots[0], item, game)

                else:
                    game.banner(f'you cannot wear the {item.name}')
            else:
                game.message(f'Wear aborted')

    elif input_key == 't':
        items = player.body.item_tuples()
        if items:
            # 'a' is ascii 97
            items_by_code = {index + 97: (slot, item) for index, part, slot, item in items}
            game.banner(['what do you remove?'])
            choice = control.get_ch()
            while choice != 27 and choice not in items_by_code:
                game.banner(['what do you remove?', f'  invalid choice "{chr(choice)}"'])
                choice = control.get_ch()
            if choice == 27:
                game.banner([])
            else:
                slot, item = items_by_code[choice]
                player.remove_item(slot, item, game) # slot.items.remove(item)

                player.stuff.append(item)
                game.banner([f'{item.name} removed'])


    elif input_key == 'g':
        on_items = mm.items_at(player.pos, False)
        nitems = len(on_items)
        if nitems > 1:
            item = control.choose_item('What will you pick up?', on_items,)
            if item:
                game.message(f'You picked up the {item.name}')
                pick_up(control, item, player, mm)
            else:
                game.message(f'Pick up aborted')
        if nitems == 1:
            game.message(f'You picked up a(n) {on_items[0].name}')
            pick_up(control, on_items[0], player, mm)
        if nitems == 0:
            game.message(f'You are not standing on any items to pick up.')

    elif input_key == 'd':
        if len(player.stuff) >= 1:
            item = control.choose_item('What would you like to drop?', player.stuff)
            if item:
                drop(control, item, player, mm, game)
            else:
                game.message(f'Drop aborted')
        else:
            game.message(f"You don't have anything to drop")

    else:
        game.message(f'unknown command: "{input_key}"')
        game.message(f'would you like to macro "{input_key}"? (y/n)')
        answer = control.get_key()
        while answer not in ('y', 'n'):
            game.message(f'"{answer}" is not y or n. Please input y or n')
            answer = control.get_key()
        if answer == 'y':
            game.message(f'Hit keystrokes and end with "{input_key}" to macro this key, q to cancel.')
            control.game_model.macros[input_key] = macro(input_key, game, control)
        else:
            game.message('Macro aborted.')

def macro(input_key, game, control):
    keybinds = []
    game.message(f'Start hitting keys to macro')
    key = control.get_key()
    while key not in (input_key, 'q'):
        game.message(f'Added "{key}"')
        keybinds.append(key)
        key = control.get_key()

    if key == 'q':
        game.message(f'Canceled macro')
        return None
    else:
        game.message(f'Macro set')
        return keybinds

def pick_up(control, item, peep, mm):
    peep.stuff.append(item)
    mm.items.remove(item)
    game = control.game_model
    mm = game.maze_model
    player = game.player
    on_items = mm.items_at(player.pos, True)
    nitems = len(on_items)
    if nitems == 1:
        game.banner(['You see a ' + on_items[0].name,''])
    elif nitems > 1:
        game.banner([f'You see {nitems} items',''])
    else:
        game.banner(['',''])

def drop(control, item, peep, mm, game):
    peep.stuff.remove(item)
    mm.items.append(Item(item.name, item.char, item.size, pos=peep.pos))
    game.message(f'You dropped the {item.name}')
    game = control.game_model
    mm = game.maze_model
    player = game.player
    on_items = mm.items_at(player.pos, True)
    nitems = len(on_items)
    if nitems == 1:
        game.banner(['You see a ' + on_items[0].name,''])
    elif nitems > 1:
        game.banner([f'You see {nitems} items',''])
    else:
        game.banner(['',''])

def player_aim(attack, control):
    game = control.game_model
    mm = game.maze_model
    player = game.player
    mm.cursorvis = 1
    mm.cursorpos = (3, 3)
    game.banner(['Where do you want to shoot?', '  (* to target)'])
    key = control.get_key()
    target = 'UNSET'
    while target == 'UNSET':
        if key in DIRECTION_KEYS and key != '.':
            target = target_for_direction(player.pos, DIRECTION_KEYS[key], mm)
        elif key == '*':
            target = choose_target(control, player)
        elif key == 'q' or key == Key.CTRL_Q:
            target = None
        else:
            game.message(f'{key} is not a valid direction to shoot')
            key = control.get_key()
            continue

    if target is not None:
        target_pos = getattr(target, 'pos', target)  # target may be a peep or a position
        path = list(line_points(player.pos, target_pos))[0:]
        mm.create_projectile(player, attack.name, path, (attack.projectile_attack(),))
        game.banner(['', '                TWANG!'])
        player._tics = player._tics - 1/player.speed * 1/attack.speed


def monster_turn(control, monster):
    game = control.game_model
    mm = game.maze_model
    player = game.player
    ranged_attack = choose_attack(monster, False)
    if monster.type != 'projectile' \
            and ranged_attack is not None \
            and is_in_sight(monster, player.pos, mm.walls) \
            and distance(monster.pos, player.pos) < ranged_attack.range:
        path = list(line_points(monster.pos, player.pos))
        mm.create_projectile(monster, ranged_attack.name, path, (ranged_attack.projectile_attack(),))
        monster._tics = monster._tics - 1/monster.speed * 1/ranged_attack.speed
    if monster.hp > monster.maxhp: monster.hp = monster.maxhp
    if monster.move_tactic == 'pos_path':
        if monster.pos_i < len(monster.pos_path) - 1:
            monster.pos_i += 1
            dst_pos = monster.pos_path[monster.pos_i]
            mlib.move_peep(game, monster, dst_pos)
        else:
            game.message(f'{monster.name} hits the ground')
            monster.hp = 0  # todo: convert to item with chance of breaking
        return True
    elif monster.move_tactic == 'hunt':
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
            direct = mlib.direction_from_vector(-dx, -dy)  # If low health, run away
        else:
            direct = mlib.direction_from_vector(dx, dy)

        dst_pos = mlib.adjacent_pos(monster.pos, direct)
        if mlib.move_peep(game, monster, dst_pos):
            return True

        # failed to move, try other directions (rotation 1,-1,2,-2,3,-3,4,-4)
        rotation = 1
        while rotation <= 4:
            d2 = mlib.direction_relative(direct, rotation)
            dst_pos = mlib.adjacent_pos(monster.pos, d2)
            if mlib.move_peep(game, monster, dst_pos):
                return True
            d2 = mlib.direction_relative(direct, -rotation)
            dst_pos = mlib.adjacent_pos(monster.pos, d2)
            if mlib.move_peep(game, monster, dst_pos):
                return True
            rotation += 1
            if abs(rotation) >= 5:
                monster._tics = monster._tics - 1 / monster.speed
                continue

    return True

def choose_monster_target(monster, control):
    return control.game_model.player

def post_player_move(control):
    game = control.game_model
    mm = game.maze_model
    player = game.player
    on_items = mm.items_at(player.pos, True)
    for i in on_items:
        if i.name == 'gold':
            player.gold = player.gold + i.amount
            mm.items.remove(i)
            game.message(f'You have scrounged {i.amount} gold')
    on_items = mm.items_at(player.pos, True)
    nitems = len(on_items)
    for i in on_items:
        if i.name == 'gold':
            player.gold = player.gold + i.amount
            mm.items.remove(i)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for n in numbers:
            if i.name == f'shop {n}':
                store_inventory = {1: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   2: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   3: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   4: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   5: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   6: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   7: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   8: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),),
                                   9: (clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),)}
                input = 0
                while input != 'q':
                    idx_line = tuple((index, f'{item.name}') for index, item in enumerate(store_inventory[n]))
                    game.banner(['b to buy, s to sell, q to quit'])
                    control.show_lines('You walk into a store and see lines of items to buy.', idx_line, False)
                    input = 0
                    while input not in ['q', 'b', 's']:
                        if input != 0:
                            control.game_model.message("Please select a key 'q', 'b', or 's' please")
                        input = control.get_key()
                    if input == 'q':
                        control.game_model.maze_model.overlay.replace([])
                    elif input == 'b':
                        control.game_model.maze_model.overlay.replace([])
                        if player.gold < 10:
                            control.game_model.message(f"You don't have enough gold to buy anything")
                        else:
                            item = control.choose_item('What would you like to buy?', store_inventory[n])
                            player.stuff.append(item)
                            player.gold -= 10
                            control.game_model.message(f'You bought a {item.name} for 10 gold')
                    elif input == 's':
                        control.game_model.maze_model.overlay.replace([])
                        if len(player.stuff) == 0:
                            control.game_model.message(f"You don't have anything to sell")
                        elif len(player.stuff) == 1:
                            item = player.stuff[0]
                            player.stuff.remove(item)
                            player.gold += 7
                            control.game_model.message(f'You sold a {item.name} for 7 gold')
                        else:
                            item = control.choose_item('What would you like to sell?', player.stuff)
                            player.stuff.remove(item)
                            player.gold += 7
                            control.game_model.message(f'You sold a {item.name} for 7 gold')

    if nitems == 1:
        game.banner(['You see a ' + on_items[0].name,''])
    elif nitems > 1:
        game.banner([f'You see {nitems} items',''])
    else:
        game.banner(['',''])


def main(root_layout, game, get_key=None):
    control = PrpgControl(root_layout, game)
    if get_key is not None:
        control.get_key = get_key
    if sys.platform != "win32" and hasattr(control, 'resize_handler'):
        signal.signal(signal.SIGWINCH, control.resize_handler)

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    while True:
        control.game_model.maze_model.elapse_time()
        res = execute_turn_seq(control)
        if res == 'quit' or res == 'player_died':
            return 0
        elif res == 'down_level':
            control.game_model.goto_level(control.game_model.maze_model.level + 1, GAME_SETTINGS.CHARS.STAIR_UP)
        elif res == 'up_level':
            control.game_model.goto_level(control.game_model.maze_model.level - 1, GAME_SETTINGS.CHARS.STAIR_DOWN)

        control.game_model.maze_model.elapse_time()


def execute_turn_seq(control):
    game = control.game_model
    mm = game.maze_model
    while mm.ti < len(mm.turn_seq):
        # print(f'turn_seq {mm.ti}/{mm.turn_seq}')
        peep = mm.turn_seq[mm.ti]
        mm.ti += 1
        if peep.hp <= 0:
            continue
        if game.is_player(peep):
            res = player_turn(control)
            if res == 'q':
                return 'quit'
            elif res == '>':
                return 'down_level'
            elif res == '<':
                return 'up_level'
        else:
            if not monster_turn(control, peep):
                return 'player_died'

    return True


# Interactively select a target to shoot
# Return a selected peep or position (int, int) for the target.
def choose_target(control, src_peep):
    game = control.game_model
    mm = game.maze_model
    top = f'*: choose next, t: target, q: quit'
    targets = target_list(src_peep, mm.peeps)  # peeps sorted in order of distance and relative angle from origin
    ti = next_target(src_peep, targets, mm.walls, 0)  # return None if no target
    if ti == -1:
        game.message('No targets in sight')
        return None  # todo: start cursor on self to allow manual selection
    while True:
        mm.target_path = tuple(line_points(src_peep.pos, targets[ti].pos))  # draws the target path
        game.banner([top, f'Aiming at {targets[ti].name}'])
        input_key = control.get_key()
        if input_key == 't':
            mm.target_path = ()
            return targets[ti]
        elif input_key == 'q' or input_key == Key.CTRL_Q:
            mm.target_path = ()
            game.banner('')
            return None
        elif input_key == '*':
            ti = next_target(src_peep, targets, mm.walls, ti + 1)
        else:
            game.message(f'unknown command "{input_key}"')


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
