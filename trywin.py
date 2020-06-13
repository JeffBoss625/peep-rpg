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
        self.scr = scr

        root = rootwin(scr)
        row1 = root.addrow()
        self.win1 = row1.addwin(Con(10,15,10,15))
        self.win2 = row1.addwin(Con(20,60))

        # win3_h = int(h/2)
        # win3_w = int(w/2)
        # self.win3 = scr.derwin(win3_h, win3_w, h-win3_h, w-win3_w)
        # self.win4 = self.win3.derwin(win3_h-2, win3_w-2, 1, 1)
        # self.win4.scrollok(True)
        self.except_str = ''

    def paint(self):
        scr = self.scr
        win1 = self.win1.scr()
        win2 = self.win2.scr()

        win2.addch(0, win2.getmaxyx()[1] - 2, '@')
        win2.addstr(6, 2, 'scr.maxyx: ' + str(scr.getmaxyx()) + str(win1.getmaxyx()) + str(win2.getmaxyx()))
        win2.addstr(7, 2, repr(self.except_str))
        win2.clrtoeol()
        win2.addch(0, win2.getmaxyx()[1] - 1, '@')

        win1.addch(0, win1.getmaxyx()[1] - 1, '@')
        win1.move(0,0)

        win1.border()
        win2.border()


def main(scr):
    curses.raw()
    h = Handler(scr)

    while 1:
        h.paint()
        scr.refresh()
        c = scr.getch()
        if c == ord('q'):
            break


curses.wrapper(main)