from lib.logger import Logger
from lib.prpg_main import main
from lib.startup import dummy_root

main(dummy_root(logger=Logger('dbg.py')))
