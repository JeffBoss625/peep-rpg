from lib.startup import dummy_root
from lib.window import *
from lib.win_layout import *
from lib.model import *

def test_text_win():
    root = dummy_root(Dim(30,10))
    pan = root.panel('pan1', Orient.VERT, None, None)
    pan.window('win1', Con(4,6,8,10)).initwin(TextWindow, model=TextModel('foo'))
    textwin = pan.window('win2', Con(4,8,9,11))
    textwin.initwin(TextWindow, model=TextModel('test-model'))
    root.do_layout()
    call_info = []
    textwin.window.model.subscribe(lambda model, msg, **params: call_info.append((model.model_name, msg, params['new'])))
    textwin.window.model.print('hi there', 'you')
    assert call_info == [('test-model', 'update', ['hi there you'])]
    assert textwin.window.model.text == ['hi there you']
    root.window.paint()
    textwin.window.model.print('hi 1234567890')
    textwin.window.model.print('hi 1234567890')
    textwin.window.model.print('hi 1234567890')
    textwin.window.model.print('hi 1234567890')
    textwin.window.model.print('hi 1234567890')
    textwin.window.model.print('hi 1234567890')
    root.window.paint()


