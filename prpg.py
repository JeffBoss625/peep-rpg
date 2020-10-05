from lib.startup import curses_wrapper
from lib.prpg_main import main

curses_wrapper(main, out=__file__)
