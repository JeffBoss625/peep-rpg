import curses
import signal
import time
import traceback
import os
from lib.curwin import *
import logging
import curses

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

def create_windows(comp, v, xoff, yoff, depth):
    for c in comp.children:
        if isinstance(c, Win):
            del c.data
            c.data = None
            if c.dim.h > 2 and c.dim.w > 2:
                comp.log('derwin({}, {})'.format(c.dim, c.pos))
                c.data = c.winparent.data.derwin(c.dim.h, c.dim.w, c.pos.y, c.pos.x)
                if c.conf.border:
                    c.data.border()

        v = create_windows(c, v, 0, 0, depth + 1)
    return v


WINTER_EDEN_STR = WINTER_EDEN.replace('\n', ' ')

class Handler:
    def __init__(self, scr):
        # use os.get_terminal_size() since scr.getmaxyx() does not change with resizing (on macos)
        w, h = self.term_size = os.get_terminal_size()
        root = self.root = rootwin(Dim(h, w), __file__)

        root.data = scr
        h_pan = root.panel(Orient.HORI, Pos(0,0), Con(0,0))
        h_pan.window('leftwin', Con(10,40,15,80))
        h_pan.window('rightwin', Con(8,22,12,30))

        root.do_layout()
        create_windows(root, None, 0, 0, 1)
        root.data.refresh()

    def size_to_term(self, force = False):
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
            curses.resizeterm(h, w)
            root.dim.w = root.con.wmin = root.con.wmax = w
            root.dim.h = root.con.hmin = root.con.hmax = h
            root.clear_layout()
            root.do_layout()

            root.data.clear()
            create_windows(root, None, 0, 0, 1)
            leftwin = root.info.win_by_name['leftwin']
            if leftwin.data:
                leftwin.data.addstr(2,2, "term_size: {}".format(leftwin.dim))
            rightwin = root.info.win_by_name['rightwin']
            if rightwin.data:
                rightwin.data.addstr(2,2, "term_size: {}".format(rightwin.dim))
            root.data.refresh()

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


curses.wrapper(main)