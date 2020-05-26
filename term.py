import curses as clib

RED_BLACK = 1
def test(scr):

    clib.init_pair(RED_BLACK, clib.COLOR_RED, clib.COLOR_BLACK)
    yoff = 0
    for i in range (255, clib.KEY_BACKSPACE):
        if clib.has_key(i):
            scr.move(yoff + 3, 3)
            scr.addstr(clib.keyname(i).decode('utf-8') + ' [' + str(i) + ']', clib.color_pair(RED_BLACK))
            yoff += 1

    scr.getch()

clib.wrapper(test)
