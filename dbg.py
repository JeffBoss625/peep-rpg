from lib.dummy_curses import DummyCurses
from lib.logger import Logger
from lib.prpg_main import main
from lib.screen_layout import Dim, RootLayout

dcurses = DummyCurses(Dim(40, 120))
main(RootLayout(dim=dcurses.term.dim, scr=dcurses.term, curses=dcurses, border=0, logger=Logger('dbg.py')))
