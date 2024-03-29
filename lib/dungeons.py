from lib.attack import AttackInfo
from lib.model import Size
from lib.monsters import monster_by_name
from lib.peep_types import create_peep
from lib.players import player_by_name
from lib.prpg_model import GameModel, MazeModel
from lib.items.item import Item
import lib.items.weapons as weapons
import lib.items.clothes as clothes
import lib.items.armor as armor
from lib.peeps import Attack

DUNGEONS = {
    'level_4': {
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%<...####....######%.........%%%%%%%%%%%%%',
            '%....####....######%.........%%%%%%%%%%%%%',
            '%....####....####..#.........%%%%%%%%%%%%%',
            '%............####..#.........%%%%%%%%%%%%%',
            '%....####....####............%%%%%%%%%%%%%',
            '%....####..........#.........%%%%%%%%%%%%%',
            '%....####....#######.........%%%%%%%%%%%%%',
            '%....####....#######.........%%%%%%%%%%%%%',
            '%###########################.%%%%%%%%%%%%%',
            '%###########################.%%%%%%%%%%%%%',
            '%#############...............%%%%%%%%%%%%%',
            '%#############.##############%%%%%%%%%%%%%',
            '%#############.##############%#####.#####%',
            '%#########.........##########%###....####%',
            '%#####..................#####%#........##%',
            '%####...................................#%',
            '%####....................####%#........##%',
            '%#####..................#####%###....####%',
            '%#########.........##########%#####.#####%',
            '%#############.##############%%%%%%%%%%%%%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps':[
            monster_by_name('Thark', pos=(2,2), maxhp=10),
            monster_by_name('Spark', pos=(24,7), maxhp=50),
            monster_by_name('Brog', pos=(14,20), maxhp=200),
            monster_by_name('Crystal', pos=(36, 17), maxhp=500),
            # create_peep('big bird', name='Beaky', pos=(18,4)),
            # create_peep('giant rat', name='Scriggle', pos=(19,4)),
        ],
        'items': [
            clothes.belt(pos=(1,1))
        ]
    },
    'level_0':{
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%.........................>........................%',
            '%......#####...#####.............#####...#####.....%',
            '%.....######...######...........######...######....%',
            '%.....######...#####2...........5#####...#####6....%',
            '%.....######...######...........######...######....%',
            '%......##1##...#####.............#####...#####.....%',
            '%..................................................%',
            '%..................................................%',
            '%......##3##...#####.............#####...#####.....%',
            '%.....######...######...........######...######....%',
            '%.....######...8####4...........7#####...#####9....%',
            '%.....######...######...........######...######....%',
            '%......#####...#####.............#####...#####.....%',
            '%..................................................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps':[],
    },
    'level_1':{
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%<..>.....................%',
            '%.........................%',
            '%.........................%',
            '%.........................%',
            '%#############.###########%',
            '%..>......##.....##...>...%',
            '%........##.......##......%',
            '%.......##.........##.....%',
            '%.......##.........##.....%',
            '%.......##.........##.....%',
            '%........##.......##......%',
            '%.........##.....##.......%',
            '%..........###.###........%',
            '%.........................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps': [
            # player_by_name('Super Dad', pos=(1, 2), maxhp=40),
            create_peep('giant rat', name='Scraggle', pos=(24, 1)),
            create_peep('giant rat', name='Scriggy', pos=(25, 1)),
            create_peep('giant rat', name='Scritch', pos=(24, 2)),
            create_peep('giant rat', name='Wriggle', pos=(25, 2)),
            create_peep('giant rat', name='Scatter', pos=(24, 3)),
            create_peep('giant rat', name='Skitter', pos=(25, 3)),
            create_peep('giant rat', name='Skreet', pos=(24, 4)),
            create_peep('giant rat', name='Squeak', pos=(25, 4)),
            create_peep('giant rat leader', name='Pipsqueak', pos=(14, 13)),
        ],
        'items': [
            clothes.belt(name='leather belt', pos=(4,3)),
            clothes.belt(name='metal belt', pos=(4,4)),
        ]
    },
    'level_2':{
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%',
            '%%%%%%%%%%<%%%%%%%%%%',
            '%%%%%%%%%...%%%%%%%%%',
            '%%%%%%%%.....%%%%%%%%',
            '%%%%%%%.......%%%%%%%',
            '%%%%%%.........%%%%%%',
            '%%%%%...........%%%%%',
            '%%%%......>......%%%%',
            '%%%...............%%%',
            '%%.................%%',
            '%#########.#########%',
            '%%.................%%',
            '%%%...............%%%',
            '%%%%.............%%%%',
            '%%%%%...........%%%%%',
            '%%%%%%.........%%%%%%',
            '%%%%%%%.......%%%%%%%',
            '%%%%%%%%.....%%%%%%%%',
            '%%%%%%%%%...%%%%%%%%%',
            '%%%%%%%%%%>%%%%%%%%%%',
            '%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps':[
            create_peep('big bird', name='Steve', pos=(10,18)),
        ],
        'items': [
            weapons.sword(name="sword_of_justice", size=Size(1.2,1.1,1.0), attack=AttackInfo('righteous_slice', '5d3'), pos=(10, 3)),
            armor.shield(name="shield_of_justice", size=Size(1.1, 1.1, 1.1), pos=(11, 3)),
            weapons.bow(name="bow_of_justice", size=Size(1.2, 1.1, 1), attack=Attack('righteous_arrow', '5d4', speed=0.7, range=20, blowback=100), pos=(9, 3)),
            armor.helm(name="helm_of_justice", size=Size(1.1,1.1,1.1), pos=(10, 4)),
            armor.chestplate(name="chestplate_of_justice", size=Size(1.1,1.1,1.1), pos=(11, 4)),
            armor.boots(name="boots_of_justice", size=Size(1.1,1.1,1.1), pos=(12, 4)),
            Item("leggings_of_justice", '=', Size(3, 5, 4), 10, '', pos=(9, 4)),
            armor.gauntlets(name="gloves_of_justice", size=Size(1.1,1.1,1.1), pos=(8, 4)),
            Item("robes_of_justice", '(', Size(3, 5, 4), 10, '', pos=(10, 5)),
        ]
    },
    'level_3': {
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%<....>.............................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%.%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%.%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%...................................%',
            '%>..................................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps': [
            create_peep('cat', name='Mrow', pos=(2, 9)),
            create_peep('big bird', name='Crawww', pos=(35, 14)),
            create_peep('big bird', name='Cheep', pos=(2, 19)),
            create_peep('big bird', name='Peep', pos=(2, 19)),
            create_peep('red dragon', name='Sparky', pos=(35, 24)),
            create_peep('queen mosquito', name='Queen Bzzz the Bzzzt', pos=(2, 30)),
            create_peep('mosquito', name='EeeEEEeeEeeeEe', pos=(35, 1)),
            create_peep('mosquito', name='eeEEeeeEEEEeee', pos=(35, 2)),
            create_peep('mosquito', name='EeEeEeeeeeEEEe', pos=(35, 3)),
            create_peep('mosquito', name='EEEEEEEEeeeeEe', pos=(35, 4)),
            create_peep('mosquito', name='eeeeeeEEeEeeEE', pos=(34, 1)),
            create_peep('mosquito', name='eeeeeEeEeEeeEE', pos=(34, 2)),
            create_peep('mosquito', name='eeEEeeEEeEeeEE', pos=(34, 3)),
            create_peep('mosquito', name='eeeeeeEEeeeeee', pos=(34, 4)),
            create_peep('mosquito', name='eeeEEeEEeeeeee', pos=(33, 1)),
            create_peep('mosquito', name='eeeeeeEEeeeeEE', pos=(33, 2)),
            create_peep('mosquito', name='eeeEeeeEeEeeEE', pos=(33, 3)),
        ],
    },
    'open':{
        'walls': [
            '%%%%%%%%%%%%%%%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%.............%',
            '%%%%%%%%%%%%%%%',
        ],
        'peeps':[
            create_peep('human', name='Super Dad', pos=(1,1)),
            create_peep('red dragon', name='Spark', pos=(13,13))

        ]
    },
    'shooting': {
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%.............................%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps': [
            # create_peep('human', name='Super Dad', pos=(2,1)),
            create_peep('dodger', name='Dummy', pos=(29,1))
        ]
    }
}

def create_level(level):
    ret = create_maze(f'level_{level}')
    if ret:
        ret.level = level
    return ret

def create_maze(info):
    if isinstance(info, str):
        info = DUNGEONS.get(info, None)
        if info is None:
            return None

    return MazeModel(
        info['walls'],
        info['peeps'],
        items=info.get('items', []),
    )

# convenient set up for testing
def create_game(info):
    game = GameModel()
    maze = create_maze(info)
    game.player = maze.peeps[0]
    game.maze_model = maze
    return game
