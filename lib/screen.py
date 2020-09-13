# wrappers around curses windows that narrow the interface with curses and add convenience functions for the game.
import curses
from lib.constants import Color

IGNORED_KEYS = {
    'KEY_RESIZE': 1,
}

# abstraction wrapping a curses screen.
# todo: extend cureses behavior into subclass "CursesScreen" and implent another "PrintScreen" subclass for testing
class Screen:
    def __init__(self, winfo):
        self.winfo = winfo      # layout window information
        self.border = 1
        self.x_margin = 1
        self.y_margin = 1
        self.scr = None               # curses window

        self.color_pairs = {}       # color pair codes by (fg, bg) tuple
        self.color_pair_count = 0   # color pairs are defined with integer references. this is used to define next pair

    def __repr__(self):
        return '{}: margin:[{},{}] scr:{}'.format(self.winfo, self.x_margin, self.y_margin, self.scr)
    #
    # TREE Navigation/Initialization functions
    #

    # delete and rebuild curses screens using layout information in winfo (recursive on children)
    def rebuild_screens(self):
        self.winfo.iterate_win(_rebuild_screen, self.winfo.root())

    #
    # CURSES Interface
    #
    def clear(self):
        self.scr.clear()

    def derwin(self, dim, pos):
        # self.log('derwin({}, {}, {})'.format(self, dim, pos))
        ret = self.scr.derwin(dim.h, dim.w, pos.y, pos.x)
        if self.border:
            ret.border()
        return ret

    def getmax_wh(self):
        max_y, max_x = self.scr.getmaxyx()
        max_h = max_y - self.y_margin * 2
        max_w = max_x - self.x_margin * 2
        if max_h < 0 or max_h < 0:
            return 0, 0

        return max_w, max_h

    def log(self, *args):
        self.winfo.log(args)

    def write_lines(self, lines):
        if not len(lines):
            return
        scr = self.scr
        max_w, max_h = self.getmax_wh()
        if not max_h:
            return

        # scr.clear()
        x = self.x_margin
        y = self.y_margin

        nlines = len(lines)
        if nlines > max_h:
            lines = lines[nlines - max_h:]
        for i, line in enumerate(lines):
            if len(line) > max_w:
                line = line[0:max_w-1]
            scr.addstr(y+i, x, line)

    def refresh(self):
        self.scr.refresh()

    def get_key(self):
        while 1:
            try:
                ret = self.scr.getkey()
                if ret not in IGNORED_KEYS:
                    return ret

            except Exception as e:
                # self.winfo.log('get_key failed: type:"{}", trace: {}'.format(
                #     str(e),
                #     ''.join(traceback.format_tb(e.__traceback__)))
                # )
                pass        # ignore failed calls to getkey() following resize events etc.

    def write_char(self, x, y, char, fg=Color.WHITE, bg=Color.BLACK):
        max_w, max_h = self.getmax_wh()
        if x >= max_w or y >= max_h:
            return

        cpair = self.color_pair(fg, bg)
        self.scr.addstr(y + self.y_margin, x + self.x_margin, char, cpair)

    def color_pair(self, fg, bg):
        key = (fg, bg)
        if key not in self.color_pairs:
            self.color_pair_count += 1
            fgc = getattr(curses, Color.curses_color(fg))
            bgc = getattr(curses, Color.curses_color(bg))
            curses.init_pair(self.color_pair_count, fgc, bgc)
            self.color_pairs[key] = curses.color_pair(self.color_pair_count)

        return self.color_pairs[key]

# delete and re-create derived curses windows/screens using parent windows/screens
def _rebuild_screen(winfo, v, xoff, yoff, d):
    if not winfo.winparent:         # don't build root screen - root screen is fixed
        return

    if winfo.data.scr:
        del winfo.data.scr
        winfo.data.scr = None # allow .scr to be checked

    winfo.data.scr = winfo.winparent.data.derwin(winfo.dim, winfo.pos)
    if winfo.data.border:
        winfo.data.scr.border()


# initialize Win wrappers, populating all WinInfo with wrappers and set up root screen.
def init_screens(root_info, scr):
    # set up root
    root_info.data = Screen(root_info)
    root_info.data.scr = scr
    root_info.data.border = 0

    # build Win wrappers for children
    def _build_win(winfo, v, xoff, yoff, d):
        winfo.data = Screen(winfo)

    for c in root_info.children:
        c.iterate_win(_build_win)



