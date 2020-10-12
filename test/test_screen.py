from lib.screen import *
from lib.screen_layout import *
from lib.model import *
from lib.startup import create_root

def test_message_screen():
    root = create_root(Dim(10, 30))
    pan = root.panel('pan1', Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10))
    msg = pan.window('win2', Con(4,8,9,11), wintype=TextWindow)
    root.do_layout()
    sync_delegates(root)
    root.window.rebuild_screens()
    msg.window.model = TextModel('test-model')
    call_info = []
    msg.window.model.subscribe(lambda model, msg, **params: call_info.append((model.model_name, msg, params['new'])))
    msg.window.model.print('hi there', 'you')
    assert call_info == [('test-model', 'update', ['hi there you'])]
    assert msg.window.model.text == ['hi there you']
    msg.window.paint()
    msg.window.model.print('hi 1234567890')
    msg.window.model.print('hi 1234567890')
    msg.window.model.print('hi 1234567890')
    msg.window.model.print('hi 1234567890')
    msg.window.model.print('hi 1234567890')
    msg.window.model.print('hi 1234567890')
    msg.window.paint()
    root.window.curses.doupdate()


