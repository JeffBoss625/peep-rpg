from lib.logger import Logger
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as dungeons

root_layout = dummy_root(logger=Logger('dbg.py'))
dungeon = dungeons.get_dungeon('level_2')

main(root_layout, dungeon)
