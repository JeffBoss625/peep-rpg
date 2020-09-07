# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import curses
# from lib.winlayout import *
from lib.constants import Color

class CurWin:
    def __init__(self, winfo):
        self.winfo = winfo      # layout window information
        self.border = 1
        self.x_margin = 1
        self.y_margin = 1
        self.scr = None         # curses window

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair

    #
    # TREE Navigation/Initialization functions
    #

    # delete and rebuild curses screens using layout information in winfo (recursive on children)
    def rebuild_screens(self):
        self.winfo.iterate_win(_rebuild_screen)

    #
    # CURSES Interface
    #
    def clear(self):
        self.scr.clear()

    def derwin(self, dim, pos):
        ret = self.scr.derwin(dim.h, dim.w, pos.y, pos.x)
        if self.border:
            ret.border()
        return ret

    def write_lines(self, lines):
        scr = self.scr
        x = self.x_margin
        y = self.y_margin
        # todo: enforce bottom/right margins and truncate strings
        for i, line in enumerate(lines):
            scr.addstr(y+i, x, line)

    def refresh(self):
        self.scr.refresh()

    def get_key(self):
        return self.scr.getkey()

    def write_char(self, x, y, char, fg=Color.WHITE, bg=Color.BLACK):
        cpair = self.color_pair(fg, bg)
        self.scr.addstr(y + self.y_margin, x + self.x_margin, char, cpair)

    def color_pair(self, fg, bg):
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            fgc = getattr(curses, 'COLOR_' + fg.name)
            bgc = getattr(curses, 'COLOR_' + bg.name)
            curses.init_pair(self.color_pair_count, fgc, bgc)
            self.color_pairs[key] = curses.color_pair(self.color_pair_count)

        return self.color_pairs[key]

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



