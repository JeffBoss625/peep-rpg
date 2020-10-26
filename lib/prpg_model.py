# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.

from lib.model import ModelList, DataModel, TextModel
from lib.move import direction_to_dxdy
from lib.peep_types import create_peep


class MazeModel(DataModel):
    def __init__(self, walls, peeps, player=None, items=()):
        super().__init__()
        self.walls = TextModel('walls', walls)
        self.peeps = ModelList()
        self.peeps.extend(peeps)

        self.player = player
        self.items = items
        self.new_peeps = []

    def update_wall(self, pos, char):
        x, y = pos
        self.walls.replace_region(x, y, [char])

    def wall_at(self, pos):
        ret = self.walls.char_at(*pos)
        if ret == '#' or ret == '%':
            return ret

class PrpgModel(DataModel):
    def __init__(self, walls=(), peeps=(), player=None, items=(), seed=0):
        super().__init__()
        peepmodel = ModelList()
        peepmodel.extend(peeps)
        itemsmodel = ModelList()
        itemsmodel.extend(items)
        self.maze = MazeModel(walls, peeps, player, items)
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

    def banner(self, *args):
        self.banner_model.print(*args)

    def is_player(self, peep):
        return peep == self.maze.player

    def create_projectile(self, direct):
        dx, dy = direction_to_dxdy(direct)

        ret = create_peep(
            'arrow',
            pos=(self.maze.player.pos[0] + dx, self.maze.player.pos[1] + dy),
        )
        ret.direct = direct
        return ret

