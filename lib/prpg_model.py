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
    def __init__(self, walls, peeps, items=(), logger=None):
        super().__init__()
        self.walls = TextModel('walls', walls)
        self.peeps = ModelList()
        self.peeps.extend(peeps)
        self.target_path = ()          # line of points (from source and target) drawn to select targets on the screen
        self.items = items

        self.player = None
        self.new_peeps = []
        self.turn_seq = None
        self.ti = 0

        self.logger = logger

        self.cursorpos = (0,0)
        self.cursorvis = 0

    def update_wall(self, pos, char):
        x, y = pos
        self.walls.replace_region(x, y, [char])

    def wall_at(self, pos):
        ret = self.walls.char_at(*pos)
        if ret == '#' or ret == '%':
            return ret

    def char_at(self, x, y):
        return self.walls.char_at(x, y)

    def set_player(self, player):
        if self.player == player:
            return

        if self.player and self.player != player:
            raise RuntimeError('player is already set')

        self.peeps.append(player)
        self.player = player

    def remove_player(self):
        if self.player is None:
            raise RuntimeError('no player to remove')

    def pos_of(self, char):
        x = -1
        y = -1
        for l in self.walls.text:
            y += 1
            x = -1
            for c in self.walls.text[y]:
                x += 1
                if c == char:
                    return x, y

        # python conventional way to loop with index: use enumerate()
        #
        # for y, line in enumerate(self.walls.text):
        #    for x, c in enumerate(line):
        #        if c == char:
        #            return x, y

        raise LookupError (f'Character "{char}" not found in maze')

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

    def elapse_time(self):
        if self.new_peeps:
            # moves by index. e.g. [2, 0, 1]
            move_counts = remaining_moves(self.turn_seq, self.ti, len(self.peeps))
            # self.log(f'tseq {self.turn_seq} {self.ti}')
            # self.log(f'move_counts {move_counts}')

            # moves by index for fraction of time remaining e.g. [0,3]
            new_move_counts = elapse_time(self.new_peeps, (len(self.turn_seq) - self.ti)/len(self.turn_seq))
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
# e.g. : [1, 1, 1, 1, 1, 1, 1, 1, 2, 3]. store unused remainder tics into peep.tics.
# peeps: array of movable items with "speed" and "tics" properties
# fac: factor to apply to speed to represent only a fraction of a turn (for peeps that enter part-way through a turn)
def elapse_time(peeps, fac):
    move_counts = []                    # same array indexes as peeps
    for p in peeps:
        tics = (p.speed * fac) + p.tics
        move_counts.append(int(tics / 10))  # round-down
        p.tics = round(tics % 10, 5)        # store remaining ticks with 5 decimal precision

    return move_counts

# return peep indexes by clicks and total clicks:
# e.g. {6:[0,2,3], 3:[4], 2:[1]}, 6
def peeps_by_clicks(move_counts):
    peepidx_by_mc = {}
    for peep_index, mc in enumerate(move_counts):
        if mc != 0:
            if mc not in peepidx_by_mc:
                peepidx_by_mc[mc] = []
            peepidx_by_mc[mc].append(peep_index)

    # peepidx_by_mc is something like {1:[0,2,3], 3:[4], 7:[1]}  (indexes of peeps moving once, three times and seven times)

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
# click/index where there is a move an array of peep (indexes) that get a move at
# that click.
#
# For example, in the returned array below, p0 has a move at clicks 1, 5, and 9.
# p1 has a move at clicks 3 and 7
# p2 has a move only at click 5 (simultaneously with p0's second move)
# [
#   1       [p0]
#   2       []
#   3       [p1]
#   4       []
#   5       [p0,p2]
#   6       []
#   7       [p1]
#   8       []
#   9       [p0]
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

# return the number of remaining moves for each peep (by offset in the returned array):
# [2,0,1]  means two moves for p0, zero moves for p1 and one move for p2
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

class GameModel(DataModel):
    def __init__(self, maze_model, level=1, seed=0):
        super().__init__()
        self.level = level

        # passing self as logger creates a PubSub subscribe() cycle, so use dict instead.
        self.maze_model = maze_model
        self.message_model = TextModel('messages')
        self.log_model = TextModel('log')
        self.banner_model = TextModel('banner')
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
        return peep == self.maze_model.player

    def set_player(self, peep, placement='<'):
        mm = self.maze_model
        mm.set_player(peep)
        pos = mm.pos_of(placement)
        mm.player.pos = pos

    def monster_killed(self, src, src_attack, dst):
        self.message(f"the {dst.name} has died to the {src.name}'s {src_attack.name}!")
        src.exp += dst.exp_value()
        current_level = level_calc(src.exp, src.level_factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL)
        handle_level_up(src, current_level, self)

