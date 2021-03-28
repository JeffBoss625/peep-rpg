# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.
import sys
from dataclasses import dataclass
from lib.constants import GAME_SETTINGS
from lib.model import ModelList, DataModel, TextModel
from lib.pclass import level_calc, handle_level_up
from lib.peep_types import create_peep


class MazeModel(DataModel):
    def __init__(self, walls, peeps, player=None, items=(), logger=None):
        super().__init__()
        self.walls = TextModel('walls', walls)
        self.peeps = ModelList()
        self.peeps.extend(peeps)
        self.target_path = ()          # line of points (from source and target) drawn to select targets on the screen

        self.player = player
        self.items = items
        self.new_peeps = []
        self.turn_seq = None
        self.logger = logger
        self.ti = 0
        self.cursorpos = (0,0)
        self.cursorvis = 0

    def update_wall(self, pos, char):
        x, y = pos
        self.walls.replace_region(x, y, [char])

    def wall_at(self, pos):
        ret = self.walls.char_at(*pos)
        if ret == '#' or ret == '%':
            return ret

    def create_projectile(self, src, ptype, targetpath, attacks):
        shot = create_peep(ptype, pos=targetpath[0], attacks=attacks)
        shot.pos_path = targetpath
        shot.pos_i = 0

        self.new_peeps.append(shot)
        self.log(f'{src.name} shoots {shot.name}')
        return shot

    def log(self, s):
        if self.logger:
            self.logger.log(s)
        else:
            sys.stderr.write(s)
            sys.stderr.write('\n')

    def elapse_time(self):
        if self.new_peeps:
            move_counts = remaining_moves(self.turn_seq, self.ti, len(self.peeps))
            self.log(f'tseq {self.turn_seq} {self.ti}')
            self.log(f'move_counts {move_counts}')

            new_move_counts = elapse_time(self.new_peeps, self.ti/len(self.turn_seq))
            move_counts.extend(new_move_counts)
            self.peeps.extend(self.new_peeps)
            self.new_peeps = []
        else:
            move_counts = elapse_time(self.peeps, 1.0)

        self.turn_seq = calc_turn_sequence(move_counts)
        self.ti = 0

    def max_x(self):
        return len(self.walls.text[0])

    def max_y(self):
        return len(self.walls.text)


# update time for peeps
# return an array of same length as peeps with the number of moves for each peep, rounded down.
# store unused remainder tics into peep.tics.
#
# peeps: array of movable items with "speed" and "tics" properties
# fac: factor to apply to speed to represent only a fraction of a turn (for peeps that enter part-way through a turn)
def elapse_time(peeps, fac):
    move_counts = []                    # same array indexes as peeps
    for p in peeps:
        tics = (p.speed * fac) + p.tics
        move_counts.append(int(tics / 10))  # round-down division operator (python 3+)
        p.tics = round(tics % 10, 5)        # store remaining ticks (MOD operator)

    return move_counts

def peeps_by_clicks(move_counts):
    peepidx_by_mc = {}
    for peep_index, mc in enumerate(move_counts):
        if mc != 0:
            if mc not in peepidx_by_mc:
                peepidx_by_mc[mc] = []
            peepidx_by_mc[mc].append(peep_index)

    # peepidx_by_mc is something like {1:[0,2,3], 3:[4], 7:[1]}  (indexes of peeps moving once, three times and seven times)
    # peepidx_by_mc.keys would be [1,3,7]
    # peepidx_by_mc.keys[1] would be [0,2,3]                     (indexes of peeps moving only once)

    # calculate total clicks (= 1 * 2 * 3, in the example)
    tot_clicks = 1
    for move_count in peepidx_by_mc.keys():
        tot_clicks = tot_clicks * move_count

    # create a new structured keyed by CLICKS per move, not moves (clicks = tot_clicks/moves)
    # = {6:[0,2,3], 3:[4], 2:[1]} for this example
    peepsbyclicks = {}
    for move_count in peepidx_by_mc.keys():
        peepsbyclicks[int(tot_clicks / move_count)] = peepidx_by_mc[move_count]

    return [peepsbyclicks, tot_clicks]


# create an array the length of all clicks and put at each
# click/index where there is a move an array of monster (indexes) that get a move at
# that click.
#
# For example, in the returned array below, m1 has a move at clicks 1, 5, and 9.
# m2 has a move at clicks 3 and 7
# m3 has a move only at click 5 (simultaneously with m1's second move)
# [
#   1       [m1]
#   2       []
#   3       [m2]
#   4       []
#   5       [m1,m3]
#   6       []
#   7       [m2]
#   8       []
#   9       [m1]
# ]
def _calc_turn_sequence(peepsbyclicks, tot_clicks):
    # walk through tot_clicks and sequence monster moves for every click
    ret = [[] for _ in range(tot_clicks)]
    for click_count in range(1, tot_clicks + 1):
        for clicks in peepsbyclicks.keys():
            if click_count % clicks == 0:
                peeps = peepsbyclicks[clicks]
                for p in peeps:
                    ret[click_count - 1].append(p)
    return ret

def remaining_moves(turn_seq, turn_offset, npeeps):
    ret = [0 for _ in range(npeeps)]
    for tsi in range(turn_offset, len(turn_seq)):
        peep_idxs = turn_seq[tsi]
        for pi in peep_idxs:
            ret[pi] += 1
    return ret


def calc_turn_sequence(move_counts):
    p_by_clicks, tot_clicks = peeps_by_clicks(move_counts)
    return _calc_turn_sequence(p_by_clicks, tot_clicks)

@dataclass
class Logger:
    def __init__(self, logger):
        self.logger = logger

    def log(self, s):
        self.logger.log(s)

class Dungeon(DataModel):
    def __init__(self, walls=(), peeps=(), player=None, items=(), level=1, seed=0):
        super().__init__()
        peepmodel = ModelList()
        peepmodel.extend(peeps)
        itemsmodel = ModelList()
        itemsmodel.extend(items)
        self.level = level

        # passing self as logger creates a PubSub subscribe() cycle, so use dict instead.
        self.maze = MazeModel(walls, peeps, player, items, logger=Logger(self))

        self.title = self.maze
        self.message_model = TextModel('messages')
        self.log_model = TextModel('log')
        self.banner_model = TextModel('banner')
        self.stats = self.maze
        self.equip = self.maze
        self.seed = seed

    # add a message or all messages in an iterable to the messages array
    def message(self, *args):
        self.message_model.print(*args)

    # To keep parameter passing to a reasonable level, model, which is passed to many handlers provides an
    # alternative for stdout. When using terminal curses library, output is switched to the messages area
    def log(self, *args):
        self.log_model.print(*args)

    def banner(self, lines):
        self.banner_model.replace(lines)

    def is_player(self, peep):
        return peep == self.maze.player

    def monster_killed(self, src, src_attack, dst):
        self.message(f"the {dst.name} has died to the {src.name}'s {src_attack.name}!")
        src.exp += dst.exp_value()
        current_level = level_calc(src.exp, src.level_factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL)
        handle_level_up(src, current_level, self)

