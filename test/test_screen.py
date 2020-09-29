from lib.screen import *
from lib.screen_layout import *
from lib.model import *
from lib.startup import create_root

def test_message_screen():
    root = create_root(Dim(10, 30))
    pan = root.panel('pan1', Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10))
    msg = pan.window('win2', Con(4,8,9,11), wintype=TextScreen)
    root.do_layout()
    sync_delegates(root)
    root.data.rebuild_screens()
    msg.data.model = TextModel('test-model')
    call_info = []
    msg.data.model.subscribe(lambda model, msg, **params: call_info.append((model.model_name, msg, params['new'])))
    msg.data.model.print('hi there', 'you')
    assert call_info == [('test-model', 'update', ['hi there you'])]
    assert msg.data.model.text == ['hi there you']
    msg.data.paint()
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.model.print('hi 1234567890')
    msg.data.paint()
    root.data.curses.doupdate()


