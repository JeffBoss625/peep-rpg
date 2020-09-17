from lib.dummy_curses import DummyWin
import lib.dummy_curses as curses
from lib.screen import *
from lib.screen_layout import *
from lib.model import *

def test_message_screen():
    root_dim = Dim(10, 30)
    root_scr = DummyWin(None, Pos(), root_dim)
    root = create_layout(root_dim)
    pan = root.panel(Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10))
    msg = pan.window('win2', Con(4,8,9,11), wintype=WIN.TEXT)
    root.do_layout()
    create_win_data(root, root_scr, curses)
    root.data.rebuild_screens()
    msg.data.model = MessageModel()
    msg.data.model.message('hi there', 'you')
    assert msg.data.model._dirty is True
    assert msg.data.model.messages == ['hi there you']
    msg.data.refresh()
    msg.data.model.message('hi 1234567890')
    msg.data.model.message('hi 1234567890')
    msg.data.model.message('hi 1234567890')
    msg.data.model.message('hi 1234567890')
    msg.data.model.message('hi 1234567890')
    msg.data.model.message('hi 1234567890')
    msg.data.refresh()


