from lib.dummy_screen import DummyScreen
from lib.screen import *
from lib.screen_layout import *
from lib.model import *

def test_message_screen():
    root_dim = Dim(10, 20)
    root = create_layout(root_dim)
    mwin = root.window('message_win', None, None, wintype=WIN.MESSAGE)
    create_win_data(root, DummyScreen(root_dim))
    root.do_layout()
    root.data.rebuild_screens()
    mwin.data.model = MessageModel()
    assert mwin.data.model._dirty is False
    mwin.data.model.message('hi there', 'you')
    mwin.data.refresh()
    assert mwin.data.model._dirty is True
    assert mwin.data.model.messages == ['hi there you']

    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.refresh()
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.model.message('oh boy')
    mwin.data.refresh()

