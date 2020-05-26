import curses as clib

def test(scr):
    keys = (
        clib.KEY_BACKSPACE,
    )

    yoff = 0
    for i in range (255, clib.KEY_BACKSPACE+55):
        if clib.has_key(i):
            scr.move(yoff + 3, 3)
            scr.addstr(clib.keyname(i).decode('utf-8') + ' [' + str(i) + ']')
            yoff += 1

    scr.getch()

clib.wrapper(test)
