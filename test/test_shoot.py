import random

from lib.logger import Logger
from lib.peep_types import create_peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as models
from lib.constants import Key
from lib.win_layout import Dim


def dungeon_test(model, keys, paint=False):
    root_layout = dummy_root(dim=Dim(110, 14), logger=Logger('dbg.py'))

    control = PrpgControl(root_layout, model)

    def get_key():
        if paint:
            control.root_layout.window.paint()
        ret = keys.pop(0)
        return ret

    control.get_key = get_key
    main(control, model)


def test_shoot_wall():
    random.seed = 1
    model = models.create_dungeon({
        'walls': [
            '%%%%',
            '%..%',
            '%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
        ]
    })
    dungeon_test(model, keys=['a', 'l', '.', '.', Key.CTRL_Q])


def test_shoot_thru_monster():
    random.seed = 1
    model = models.create_dungeon({
        'walls': [
            '%%%%%%',
            '%....%',
            '%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('dodger', name='Dummy', pos=(4,1))
        ]
    })
    dungeon_test(model, keys=['a', 'l', '.', '.', '.', '.', Key.CTRL_Q], paint=False)

