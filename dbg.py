from lib.dummy_curses import DummyCurses
from lib.logger import Logger
from lib.prpg_main import main
from lib.screen_layout import Dim, RootLayout

dim = Dim(40, 120)
curseslib = DummyCurses(dim)
main(RootLayout(dim.dup(), logger=Logger('dbg.py')), curseslib.term, curseslib)
