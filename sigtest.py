import signal
import time
import os
import inspect

def resize_handler(signum, frame):
    print('resize({}, {})'.format(signum, inspect.getframeinfo(frame)))
    print('  term: {}'.format(os.terminal_size))

def quit_handler(signum, frame):
    print('quit({}, {})'.format(signum, frame))


signal.signal(signal.SIGWINCH, resize_handler)

while 1:
    time.sleep(0.3)
    print('loop')

