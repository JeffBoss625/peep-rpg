import curses as curses

RED_BLACK = 1
def test(scr):

    curses.init_pair(RED_BLACK, curses.COLOR_RED, curses.COLOR_BLACK)
    yoff = 0

    curses.use_default_colors()
    for i in range(0, 255):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            scr.addstr(str(i), curses.color_pair(i))

    except:
        pass

    # for i in range (255, clib.KEY_BACKSPACE):
    #     if clib.has_key(i):
    #         scr.move(yoff + 3, 3)
    #         scr.addstr(clib.keyname(i).decode('utf-8') + ' [' + str(i) + ']', clib.color_pair(RED_BLACK))
    #         yoff += 1

    scr.getch()

curses.wrapper(test)
