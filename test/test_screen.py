from lib.dummy_curses import DummyCursesWindow
import lib.dummy_curses as curses
from lib.screen import *
from lib.screen_layout import *
from lib.model import *

def test_message_screen():
    root_dim = Dim(10, 30)
    root_scr = DummyCursesWindow(None, Pos(), root_dim)
    root = create_root(root_dim)
    pan = root.panel('pan1', Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10))
    msg = pan.window('win2', Con(4,8,9,11), wintype=WIN.TEXT)
    root.do_layout()
    create_win_data(root, root_scr, curses)
    root.data.rebuild_screens()
    msg.data.model = TextModel('test-model')
    call_info = []
    msg.data.model.subscribe('test-model', lambda *args: call_info.append(args))
    msg.data.model.print('hi there', 'you')
    assert call_info == [('test-model', 'extend', ['hi there you'])]
    assert msg.data.model.text == ['hi there you']
    msg.data.paint()
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.paint()
    curses.doupdate()


