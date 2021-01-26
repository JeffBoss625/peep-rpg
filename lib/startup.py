from lib.dummy_curses import DummyCurses
from lib.logger import Logger
from lib.win_layout import Dim, RootLayout

def dummy_root(dim=Dim(120,40), border=0, logger=Logger('stderr')):
    dcurses = DummyCurses(dim)
    return RootLayout(dim=dim, border=border, logger=logger, scr=dcurses.term, curses=dcurses)

