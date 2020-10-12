from lib.startup import dummy_root
from lib.window import *
from lib.win_layout import *
from lib.model import *

def test_message_win():
    root = dummy_root(Dim(10,30))
    pan = root.panel('pan1', Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10)).initwin(TextWindow, model=TextModel('foo'))
    msg = pan.window('win2', Con(4,8,9,11))
    msg.initwin(TextWindow, model=TextModel('test-model'))
    root.do_layout()
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


