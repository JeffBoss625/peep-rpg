# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import curses
from lib.winlayout import *

class CurWin:
    def __init__(self, winfo):
        self.winfo = winfo      # layout window information
        self.border = 1
        self.scr = None         # curses window

    #
    # TREE Navigation/Initialization functions
    #

    # delete and rebuild curses screens using layout information in winfo (recursive on children)
    def rebuild_screens(self):
        self.winfo.iterate_win(_rebuild_screen)

    #
    # CURSES Interface
    #
    def derwin(self, dim, pos):
        ret = self.scr.derwin(dim.h, dim.w, pos.y, pos.x)
        if self.border:
            ret.border()
        return ret

    def write_lines(self, lines, x_margin, y_margin):
        scr = self.scr
        y, x = scr.getyx()
        y += y_margin
        x += x_margin
        # todo: enforce bottom/right margins and truncate strings
        for i, line in enumerate(lines):
            scr.move(y+i, x)
            scr.addstr(line)

# delete and re-create derived curses windows/screens using parent windows/screens
def _rebuild_screen(winfo, v, xoff, yoff, d):
    if not winfo.winparent:         # don't build root screen - root screen is fixed
        return

    if winfo.data.scr:
        del winfo.data.scr

    winfo.data.scr = winfo.winparent.data.derwin(winfo.dim, winfo.pos)
    if winfo.data.border:
        winfo.data.scr.border()


# initialize Win wrappers, populating all WinInfo with wrappers and set up root screen.
def init_win(root_info, scr):
    # set up root
    root_info.data = CurWin(root_info)
    root_info.data.scr = scr
    root_info.data.border = 0

    # build Win wrappers for children
    def _build_win(winfo, v, xoff, yoff, d):
        root_info.log('_build_win({}, depth:{})'.format(winfo, d))
        winfo.data = CurWin(winfo)

    for c in root_info.children:
        c.iterate_win(_build_win)



