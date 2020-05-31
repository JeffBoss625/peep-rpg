# Demonstrate simple cursor drawing and movement (h,j,k,l)
import lib.move as mlib
import curses as curselib
import lib.attack as alib
from lib.move import Direction
from lib.monsters import monster_by_name
from lib.players import player_by_name
from lib.model_game import Model
from lib.screen import Screen
import random
import time

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
        elif input_key == '\x11':               # ^Q
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
        elif input_key == 'a':
            model.message('Where do you want to shoot?')
            screen.repaint()
            sec_input_key = screen.get_key()
            while sec_input_key not in DIRECTION_KEYS:
                sec_input_key = screen.get_key()
                model.message('That is not a valid direction to shoot')
                model.message('Where do you want to shoot?')
                screen.repaint()
            direct = DIRECTION_KEYS[sec_input_key]
            alib.create_projectile(direct, model)
            model.message('Projectile shot')
            screen.repaint()

        else:
            model.message('unknown command: "' + input_key + '"')

        screen.repaint()  # update messages
        # continue with loop to get more input


def monster_turn(model, monster):
    if monster.move_tactic == 'straight':
        direct = monster.direct
        mlib.move_peep(model, monster, direct)
    elif monster.move_tactic == 'seek':
        dx = model.player.x - monster.x
        dy = model.player.y - monster.y
        if model.player.hp <= 0:
            return 'q'
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

def main(scr):
    curselib.raw()
    model = Model(peeps=PEEPS, maze=MAZE, player=PEEPS[0])
    screen = Screen(scr, model)

    screen.repaint()

    # GET PLAYER AND MONSTER TURNS (move_sequence)
    while True:
        peeps = [p for p in model.peeps]
        turns = mlib.calc_turn_sequence(model.peeps)

        for ti, peep_indexes in enumerate(turns):
            for pi, peep_index in enumerate(peep_indexes):
                peep = peeps[peep_index]
                if model.is_player(peep):
                    if player_turn(screen) == 'q':
                        return 0     # QUIT GAME
                else:
                    if monster_turn(model, peep):
                        model.message('YOU DIED')
                        screen.repaint()
                        time.sleep(3)
                        return 0


                # update peeps list to living peeps
                model.peeps = [p for p in model.peeps if p.hp > 0]

                screen.repaint()


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


curselib.wrapper(main)
