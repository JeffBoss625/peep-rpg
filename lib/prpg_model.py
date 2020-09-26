# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.

from lib.model import TextModel, ModelList, DataModel

class MazeModel(DataModel):
    def __init__(self, walls, peeps, player):
        super().__init__()
        self.walls = TextModel('walls', walls)
        self.peeps = ModelList()
        self.peeps.extend(peeps)
        self.player = player

class PrpgModel(DataModel):
    def __init__(self, walls=None, peeps=None, player=None, seed=0):
        super().__init__()
        self.maze = MazeModel(walls, peeps, player)
        self.message_model = TextModel('messages')
        self.log_model = TextModel('log')
        self.billboard = TextModel('billboard')
        self.seed = seed

    # add a message or all messages in an iterable to the messages array
    def message(self, *args):
        self.message_model.print(*args)

    # To keep parameter passing to a reasonable level, model, which is passed to many handlers provides an
    # alternative for stdout. When using terminal curses library, output is switched to the messages area
    def log(self, *args):
        self.log_model.print(*args)

    def is_player(self, peep):
        return peep == self.maze.player
