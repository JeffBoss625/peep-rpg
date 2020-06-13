# A simple debug function for printing with stacktrace depth

import traceback
import dataclasses

@dataclasses.dataclass
class History:
    min_depth: int = 10000


HISTORY = History()

def printd(*args):
    depth = len(traceback.extract_stack())
    HISTORY.min_depth = min(HISTORY.min_depth, depth)
    depth -= HISTORY.min_depth
    if depth <= 0:
        print(*args)
    else:
        print('   ' * depth, *args)

