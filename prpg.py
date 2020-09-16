from lib.prpg_main import startup
import curses
import os

curses.get_terminal_size = os.get_terminal_size     # bundle terminal-related functions together for injection

startup(curses)