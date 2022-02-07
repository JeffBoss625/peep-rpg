from lib.logger import Logger
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as dungeons

root_layout = dummy_root(logger=Logger('dbg.py'))
game = dungeons.create_game('level_2')
control = PrpgControl(root_layout, game)

main(control)
