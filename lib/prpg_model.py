# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.

from dataclasses import dataclass
from lib.model import MessageModel

@dataclass
class PrpgModel:
    def __init__(self, player=None, maze=None, peeps=None, seed=0):
        self.player = player
        self.maze = maze if maze else []
        self.peeps = peeps if peeps else []
        self.message_model = MessageModel()
        self.seed = seed
        self.log_output = []

    # add a message or all messages in an iterable to the messages array
    def message(self, *args):
        self.message_model.message(args)

    # To keep parameter passing to a reasonable level, model, which is passed to many handlers provides an
    # alternative for stdout. When using terminal curses library, output is switched to the messages area
    def log(self, *args):
        s = ' '.join(str(a) for a in args)
        self.log_output.extend(s.split('\n'))

    def is_player(self, peep):
        return peep == self.player
