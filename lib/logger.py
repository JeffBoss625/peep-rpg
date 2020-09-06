import sys
import logging
import re

# Simple logger with one level of logging. Logs if file name is given, otherwise no logging.
class Logger:
    def __init__(self, outfile):
        if outfile is None:
            self.mode = 'none'
        elif outfile == 'stdout':
            self.mode = 'stdout'
        elif outfile == 'stderr':
            self.mode = 'stderr'
        else:
            self.mode = 'delegate'

        if outfile:
            outfile = re.sub('\\.py$', '', outfile)
            delegate = logging.getLogger(outfile)
            hdlr = logging.FileHandler(outfile + ".log")
            hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
            delegate.addHandler(hdlr)
            delegate.setLevel(logging.DEBUG)
        else:
            delegate = None

        self.delegate = delegate

    def log(self, s):
        if self.mode == 'none':
            return

        if self.mode == 'delegate':
            self.delegate.info(s)
        elif self.mode == 'stdout':
            print(s)
        elif self.mode == 'stderr':
            sys.stderr.write('{}\n'.format(s))
        else:
            raise ValueError('unknown mode: {}'.format(self.mode))