import curses
import signal
import time
import traceback
import os
from lib.curwin import *

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

WINTER_EDEN_STR = WINTER_EDEN.replace('\n', ' ')
class Handler:
    def __init__(self, scr):
        self.root = rootwin(scr)
        col1 = self.root.addcol()
        self.win2 = col1.addwin(Con(10, 15, 10, 15))
        self.bottom_row = col1.addrow()
        self.winblank = self.bottom_row.addwin()

        self.win4 = self.bottom_row.addwin(Con(20,60))
        self.win4.scr().scrollok(True)
        self.except_str = ''
        self.term_size = os.get_terminal_size()

    def paint(self):
        scr = self.root.scr()
        win2 = self.win2.scr()
        win4 = self.win4.scr()

        win2.addch(0, win2.getmaxyx()[1] - 2, '@')
        win2.addstr(6, 2, 'scr.maxyx: ' + str(scr.getmaxyx()) + str(win2.getmaxyx()) + str(win4.getmaxyx()))
        win2.addstr(7, 2, repr(self.except_str))
        win2.clrtoeol()
        win2.addch(0, win2.getmaxyx()[1] - 1, '@')

        win4.addch(0, win4.getmaxyx()[1] - 1, '@')
        win4.move(0,0)
        win4.addstr(1, 1, WINTER_EDEN_STR)

        win2.border()
        win4.border()

    def size_to_term(self, force = False):
        if not force and self.term_size == os.get_terminal_size():
            return

        # wait for resize changes to stop for a moment before resizing
        t0 = time.time()
        scr = self.root.scr()
        win2 = self.win2.scr()
        win4 = self.win4.scr()
        self.term_size = os.get_terminal_size()
        while time.time() - t0 < 0.3:
            time.sleep(0.1)
            win2.addstr(3, 2, str(time.time() - t0) + ' elapsed')
            win2.refresh()
            if self.term_size != os.get_terminal_size():
                # size changed, reset timer
                self.term_size = os.get_terminal_size()
                t0 = time.time()

        try:
            self.root.resize()
            w, h = self.term_size
            curses.resizeterm(h, w)

            win3_h = int(h/2)
            win3_w = int(w/2)
            win4.resize(win3_h-2, win3_w-2)

            win2.resize(min(h, 20), min(w, 60))
            scr.resize(h, w)
            scr.clear()

        except Exception as e:
            self.except_str = 'resize failed: ' + str(e) + ''.join(traceback.format_tb(e.__traceback__))

def main(scr):
    curses.raw()
    h = Handler(scr)

    def resize_handler(signum, frame):
        h.size_to_term(True)

    signal.signal(signal.SIGWINCH, resize_handler)

    while 1:
        h.size_to_term()
        h.paint()
        scr.refresh()
        c = scr.getch()
        if c == ord('q'):
            break


curses.wrapper(main)