# Model is a master model containing all the game state: messages, player and monster locations and state, equipment,
# current dungeon etc.
# State is mutable/changing.
# Model will also be responsible for exposing simple serial view of state for saving the game as well as methods
# that may update state from loaded or generated sources (new levels, mazes etc).
#
# Model is designed to be open and simple - an understandable collection of simple data structures that reflects
# the state of the game. It eschew's traditional object encapsulation of internal state for a transparent model
# that will be costly to change, but easier to work with and understand.

import dataclasses as dclib
from lib.peep import Peep

@dclib.dataclass
class Model:
    player: Peep = None
    maze: list = dclib.field(default_factory=list)
    peeps: list = dclib.field(default_factory=list)
    messages: list = dclib.field(default_factory=list)
    seed: int = 0   # random number seed. non-zero will keep game consistent (pseudo-random)

    # add a message or all messages in an interable to the messages array
    def message(self, msg):
        if isinstance(msg, str):
            self.messages.append(msg)
        else:
            self.messages.extend(msg)

def create_model():
    return Model()
