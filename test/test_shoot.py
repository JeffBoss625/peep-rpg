import random

from lib.logger import Logger
from lib.peep_types import create_peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
import lib.dungeons as dungeons
from lib.constants import Key
from lib.win_layout import Dim


def assert_dungeon(dungeon, keys, paint=False):
    root_layout = dummy_root(dim=Dim(110, 14), logger=Logger('dbg.py'))

    control = PrpgControl(root_layout, dungeon)

    def get_key():
        if paint:
            control.root_layout.window.paint()
        ret = keys.pop(0)
        return ret

    main(root_layout, dungeon, get_key)


def test_shoot_wall():
    random.seed = 1
    dungeon =  dungeons.create_dungeon({
        'walls': [
            '%%%%',
            '%..%',
            '%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
        ]
    })
    assert_dungeon(dungeon, ['a', 'l', '.', '.', Key.CTRL_Q])


def test_shoot_thru_monster():
    random.seed = 1
    dungeon =  dungeons.create_dungeon({
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
    assert_dungeon(dungeon, ['a', 'l', '.', '.', '.', '.', Key.CTRL_Q], paint=False)

def test_shoot_monster():
    random.seed = 1
    dungeon =  dungeons.create_dungeon({
        'walls': [
            '%%%%%%',
            '%....%',
            '%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('goblin', name='Gark', pos=(4,1))
        ]
    })
    assert_dungeon(dungeon, ['a', '*', 't', '.', Key.CTRL_Q], paint=False)

def test_shoot_monster_blocked():
    random.seed = 1
    dungeon =  dungeons.create_dungeon({
        'walls': [
            '%%%%%%',
            '%..%.%',
            '%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('goblin', name='Gark', pos=(4,1))
        ]
    })
    assert_dungeon(dungeon, ['a', '*', 't', '.', Key.CTRL_Q], paint=False)


def test_balrog_whip():
    random.seed = 1
    dungeon = dungeons.create_dungeon({
        'walls': [
            '%%%%%%',
            '%....%',
            '%%%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('balrog', name='Gark', pos=(3,1))
        ]
    })
    assert_dungeon(dungeon, ['.', '.', '.', Key.CTRL_Q], paint=True)
    print('hi')
