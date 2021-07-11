from lib import dungeons
from lib.attack import calc_deflection, attack_dst
from lib.constants import Key
from lib.logger import Logger
from lib.pclass import level_calc
from lib.peep_types import create_peep
from lib.peeps import Attack, Peep
from lib.prpg_control import PrpgControl
from lib.prpg_main import main
from lib.startup import dummy_root
from lib.body import create_body
import random
import math

from lib.win_layout import Dim


class Out:
    def __init__(self):
        self.args = []

    def message(self, *args):
        self.args.append(args)

    def log(self, *args):
        self.args.append(args)

def assert_game(model, keys, paint=False):
    root_layout = dummy_root(dim=Dim(110, 14), logger=Logger('dbg.py'))

    control = PrpgControl(root_layout, model)

    def get_key():
        if paint:
            control.root_layout.window.paint()
        ret = keys.pop(0)
        return ret

    main(root_layout, model, get_key=get_key)


# def test_calc_deflection():
#     data = (
#         # defl, skill   str     dex    exp
#         #       ratio
#         (0.5,   1.0,    1.0,    1.0,  0.5),
#         (0.5,   1.5,    1.0,    1.0,  0.667),
#         (0.5,   1.0,    1.5,    1.0,  0.6),
#         (0.5,   1.0,    1.0,    1.5,  0.667),
#
#         (0.5,   1.0,    1.5,    1.5,  0.733),
#         (0.5,   1.5,    1.5,    1.0,  0.733),
#
#         (0.5,   1.5,    1.5,    1.5,  0.822),
#
#         (0.3,   3.0,    0.2,    2.0,  0.787),
#         (0.3,   1.0,    0.2,    3.0,  0.54),
#         (0.3,   3.0,    0.2,    1.0,  0.54),
#         (0.3,   0.3,    0.2,    1.0,  0.054),
#     )
#     for defl, skill, str, dex, exp in data:
#         d = calc_deflection(defl, skill, PlayerStats(str=str, dex=dex))
#         assert d == exp

def test_attack():
    p1 = Peep(name='p1', hp=4, attacks=(Attack('teeth', damage='1d3'),), body=create_body('humanoid'))
    m1 = Peep(name='m1', hp=5, attacks=(Attack('kick', damage='1d3'),), body=create_body('humanoid'))

    out = Out()
    random.seed(5)
    attack_dst(p1, m1, p1.attacks[0], out)
    assert m1.hp == 3.5
    for n in range(0,6):
        attack_dst(m1, p1, m1.attacks[0], out)
    assert p1.hp == 1.75

    # try this.... not changing.
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)
    # attack(p1, p2, 'teeth', out, 3)
    # attack(p2, p1, 'teeth', out, 3)
    # print(p1.hp, p2.hp)

def xptolevel_calc(level, factor, base):
    ret = 0
    for i in range(0, level):
        addon = base*math.pow(factor, i)
        ret += addon
    return ret

def test_xptolevel_calc():
    data = (
        (1, 2, 100, 100),
        (2, 2, 100, 300),
        (3, 2, 100, 700),
        (1, 2.5, 100, 100),
        (2, 2.5, 100, 350),
        (3, 2.5, 100, 975),
    )
    for level, factor, base, exp in data:
        lc = xptolevel_calc(level, factor, base)
        # print(lc)
        assert lc == exp

def test_level_calc():
    data = (
        (0, 2, 1),
        (1, 2, 1),
        (99, 2, 1),
        (100, 2, 2),
        (101, 2, 2),
        (299, 2, 2),
        (300, 2, 3),
        (301, 2, 3),
        (699, 2, 3),
        (700, 2, 4),
        (701, 2, 4),
        (1499, 2, 4),
    )
    for xp, factor, exp in data:
        lc = level_calc(xp, factor, 100)
        # print(f'level_calc({xp}, {factor}) = {lc}/{exp})')
        # assert lc == exp

def test_shield_block():
    random.seed = 1
    game = dungeons.create_game({
        'walls': [
            '%%%%',
            '%..%',
            '%%%%',
        ],
        'peeps': [
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('big bird', name='birdy!', pos=(2,1)),
        ]
    })

    class shield:
        type: str = 'rect'
        height: int = 2
        width: int = 2

    p = game.maze_model.peeps[0]
    game.maze_model.peeps[0].inventory.hand1 = shield()
    print(p)
    assert_game(game, ['a', 'l', '.', '.',  '.', '.', '.', '.', '.', Key.CTRL_Q], paint=False)

def choose_melee_attack(src):
    numattacks = len(src.attacks)
    attacks = []
    for a in src.attacks:
        if a.range > 0:
            numattacks -= 1
        else:
            attacks.append(a)
    if numattacks == 0:
        return None
    elif numattacks == 1:
        return src.attacks[0]
    else:
        # parsed = ((att.damage.split('d'), att) for att in src.attacks)
        # by_dmg = ((avg_dmg(atup[0][0], atup[0][1]), atup[1]) for atup in parsed)
        # att = max(by_dmg, 0)
        dmg = 0
        attack = None
        for a in attacks:
            parts = a.damage.split('d')
            a_dmg = avg_dmg(int(parts[0]), int(parts[1]))
            if a_dmg >= dmg:
                dmg = a_dmg
                attack = a
        return attack

def avg_dmg(n, q):
    return n * ((q+1)/2)

def test_choose_melee_attack():
    p1 = Peep(name='p1', hp=4, attacks=(Attack('teeth', damage='1d3'), Attack('punch', damage='2d3'), Attack('stab', damage='3d2')), body=create_body('humanoid'))
    m1 = Peep(name='m1', hp=5, attacks=(Attack('kick', damage='1d3'), Attack('shoot', damage='17d17', range=5), Attack('bite', damage='1d2'),), body=create_body('humanoid'))
    out = Out()
    attack_dst(p1, m1, choose_melee_attack(p1), out)
    attack = choose_melee_attack(p1)
    assert attack.name == 'stab'
    attack2 = choose_melee_attack(m1)
    assert attack2.name == 'kick'