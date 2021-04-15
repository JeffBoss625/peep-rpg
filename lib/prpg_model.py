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

from lib import dungeons
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

        self.new_peeps = []
        self.turn_seq = None
        self.ti = 0

        self.level = -1

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

    def add_peep(self, peep):
        if self.peeps.count(peep) or self.new_peeps.count(peep):
            return False
        self.new_peeps.append(peep)
        return True

    def remove_peep(self, peep):
        try:
            self.peeps.remove(peep)
            return True
        except ValueError:
            pass
        try:
            self.new_peeps.remove(peep)
            return True
        except ValueError:
            pass
        return False

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
            self.peeps.extend(self.new_peeps)
            self.new_peeps = []

        self.turn_seq = elapse_time(self.peeps)
        self.ti = 0

    def max_x(self):
        return len(self.walls.text[0])

    def max_y(self):
        return len(self.walls.text)

# NEW
# Add the smallest increment of time (the fastest peep) to all peep stored movement (tics). Wrap around
# (mod increment) tics that equal or exceed this incremented amount and return the list of such
# peeps sorted by highest-to-lowest tics value - the order of peeps to move.
def elapse_time(peeps):
    ret = []

    peeps.sort(key=lambda p: -p.speed)
    inc = round(1/peeps[0].speed, 5)   # increment for the fastest peep (smallest increment)
    for p in peeps:
        if p.speed > 0:
            p._tics = round(p._tics + inc, 5)
            thresh = 1/p.speed
            if p._tics >= thresh:
                p._tics = round(p._tics - thresh, 5)
                ret.append(p)

    ret.sort(key=lambda p: -p._tics)
    return ret

@dataclass
class Logger:
    def __init__(self, logger):
        self.logger = logger

    def log(self, s):
        self.logger.log(s)

class GameModel(DataModel):
    def __init__(self, player=None, seed=0):
        super().__init__()

        # passing self as logger creates a PubSub subscribe() cycle, so use dict instead.
        self.maze_model = None
        self.player = player
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
        return peep == self.player

    def goto_level(self, level, placement=None):
        if self.maze_model and self.maze_model.level == level:
            self.maze_model.add_peep(self.player)
            if placement:
                self.player.pos = self.maze_model.pos_of(placement)
            return

        maze = dungeons.create_level(level)
        if not maze:
            self.message('This staircase has been caved in.')
            return

        if self.maze_model:
            self.maze_model.remove_peep(self.player)
        maze.add_peep(self.player)
        if placement:
            self.player.pos = maze.pos_of(placement)

        pmaze = self.maze_model
        self.maze_model = maze

        self.publish_update(pmaze, maze, attrib='maze_model')

    def set_player(self, peep, placement=None):
        if peep == self.player:
            return

        if self.maze_model:
            self.goto_level(self.maze_model.level, placement)

        self.player = peep
        peep.publish_update(None, peep)

    def monster_killed(self, src, src_attack, dst):
        self.message(f"{dst.name} has died to the {src.name}'s {src_attack.name}!")
        src.exp += dst.exp_value()
        current_level = level_calc(src.exp, src.level_factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL)
        handle_level_up(src, current_level, self)

