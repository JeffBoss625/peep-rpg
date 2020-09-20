# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.

from lib.model import TextModel, DataModel

class MazeModel(DataModel):
    def __init__(self, maze, peeps):
        super().__init__()
        self.maze = maze
        self.peeps = peeps

class PeepsModel(DataModel):
    def __init__(self, player, peeps):
        super().__init__()
        self.player = player
        self.peeps = peeps if peeps else []

class PrpgModel(DataModel):
    def __init__(self, player=None, maze=None, peeps=None, seed=0):
        super().__init__()
        self.peeps = PeepsModel(player, peeps)
        self.maze = MazeModel(TextModel('maze', maze), self.peeps)
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
        return peep == self.peeps.player
