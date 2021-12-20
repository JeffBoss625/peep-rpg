import random

from lib.logger import Logger
from lib.peep_types import create_peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as dungeons
from lib.constants import Key
from lib.win_layout import Dim


def assert_game(game, keys, paint=False):
    root_layout = dummy_root(dim=Dim(110, 30), logger=Logger('dbg.py'))

    control = PrpgControl(root_layout, game, pack=True)

    def get_key():
        if paint:
            control.root_layout.window.paint()
        ret = keys.pop(0)
        return ret

    control.get_key = get_key
    main(control)


def test_shoot_wall():
    random.seed = 1
    game = dungeons.create_game({
        'walls': [
            '%%%%',
            '%..%',
            '%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
        ]
    })
    assert_game(game, ['a', 'l', '.', '.', Key.CTRL_Q], paint=True)

