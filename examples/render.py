import curses
import signal
import time
import traceback
import os

from lib.screen import sync_delegates
from lib.startup import create_root
from lib.screen_layout import Orient, Pos, Con, Dim

WINTER_EDEN = """
A winter garden in an alder swamp,
Where conies now come out to sun and romp,
As near a paradise as it can be
And not melt snow or start a dormant tree.

It lifts existence on a plane of snow
One level higher than the earth below,
One level nearer heaven overhead,
And last year's berries shining scarlet red.

It lifts a gaunt luxuriating beast
Where he can stretch and hold his highest feat
On some wild apple tree's young tender bark,
What well may prove the year's high girdle mark.

So near to paradise all pairing ends:
Here loveless birds now flock as winter friends,
Content with bud-inspecting. They presume
To say which buds are leaf and which are bloom.

A feather-hammer gives a double knock.
This Eden day is done at two o'clock.
An hour of winter day might seem too short
To make it worth life's while to wake and sport.
Robert Frost
"""

# def create_windows(comp, v, xoff, yoff, depth):
#     for c in comp.children:
#         if isinstance(c, WinInfo):
#             del c.window.scr
#             c.window.scr = None
#             if c.dim.h > 2 and c.dim.w > 2:
#                 comp.log('derwin({}, {})'.format(c.dim, c.pos))
#                 c.window = c.winparent.window.derwin(c.dim, c.pos)
#
#         v = create_windows(c, v, 0, 0, depth + 1)
#     return v


WINTER_EDEN_STR = WINTER_EDEN.replace('\n', ' ')

class Handler:
    def __init__(self, root, curses):
        self.root = root
        self.curses = curses
        # use os.get_terminal_size() since scr.getmaxyx() does not change with resizing (on macos)
        h_pan = root.panel(Orient.HORI, 'h_pan', Pos(0,0), Con(0,0))
        h_pan.window('leftwin', Con(10,40,15,80))

        v_pan = h_pan.panel(Orient.VERT, None)
        v_pan.window('rightwin', Con(8,22,12,30))
        v_pan.window('lowerwin', Con(6,10))

        root.do_layout()
        sync_delegates(root)
        root.window.rebuild_screens()
        root.window.scr.refresh()

    def size_to_term(self, force=False):
        if not force and self.term_size == os.get_terminal_size():
            return

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            if self.term_size != os.get_terminal_size():
                # size changed, reset timer
                self.term_size = os.get_terminal_size()
                t0 = time.time()

        try:
            root = self.root
            w, h = self.term_size
            self.curses.resizeterm(h, w)
            root.dim.w = root.con.wmin = root.con.wmax = w
            root.dim.h = root.con.hmin = root.con.hmax = h
            root.clear_layout()
            root.do_layout()

            root.window.scr.clear()
            root.window.rebuild_screens()

            leftwin = root.info.comp_by_name['leftwin']
            if leftwin.window.scr:
                leftwin.window.scr.addstr(2,2, "term_size: {}".format(leftwin.dim))
            rightwin = root.info.comp_by_name['rightwin']
            if rightwin.window.scr:
                rightwin.window.scr.addstr(2,2, "term_size: {}".format(rightwin.dim))
            lowerwin = root.info.comp_by_name['lowerwin']
            if lowerwin.window.scr:
                lowerwin.window.scr.addstr(2,2, "term_size: {}".format(rightwin.dim))

            root.window.scr.refresh()

        except Exception as e:
            raise RuntimeError('resize failed: ' + str(e) + ''.join(traceback.format_tb(e.__traceback__)))


def main(scr):
    curses.raw()

    h = Handler(scr)

    def resize_handler(_signum, _frame):
        h.size_to_term(True)

    signal.signal(signal.SIGWINCH, resize_handler)
    while 1:
        h.size_to_term()
        scr.refresh()
        c = scr.getch()
        if c == ord('q'):
            break

        create_root(Dim(h, w), __file__)

curses.wrapper(create_root(None, __file__))