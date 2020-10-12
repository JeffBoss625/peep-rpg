from lib.logger import Logger
from lib.prpg_main import main
from lib.screen_layout import Dim
from lib.startup import dummy_root

main(dummy_root(dim=Dim(40,120), logger=Logger('dbg.py')))
