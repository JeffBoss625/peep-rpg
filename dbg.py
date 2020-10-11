from lib.dummy_curses import DummyCurses
from lib.logger import Logger
from lib.prpg_main import main
from lib.screen_layout import Dim, RootLayout

dcurses = DummyCurses(Dim(40, 120))
main(RootLayout(dcurses.term.dim, border=0, logger=Logger('dbg.py')), dcurses.term, dcurses)
