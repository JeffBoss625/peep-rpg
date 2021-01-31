from lib.logger import Logger
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as models

root_layout = dummy_root(logger=Logger('dbg.py'))
dungeon = models.create_dungeon('dungeon1')
control = PrpgControl(root_layout, dungeon)

main(control, dungeon)
