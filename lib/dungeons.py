from lib.model import Size
from lib.monsters import monster_by_name
from lib.peep_types import create_peep
from lib.players import player_by_name
from lib.prpg_model import GameModel
from lib.items.item import Item

DUNGEONS = {
    'dungeon1': {
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%....####....######%.........%%%%%%%%%%%%%',
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
            player_by_name('Super Dad', pos=(1,2), maxhp=40),
            monster_by_name('Thark', pos=(2,2), maxhp=10),
            monster_by_name('Spark', pos=(24,7), maxhp=50),
            monster_by_name('Brog', pos=(14,20), maxhp=200),
            monster_by_name('Crystal', pos=(36, 17), maxhp=500),
            create_peep('big bird', name='Beaky', pos=(18,4)),
            create_peep('giant rat', name='Scriggle', pos=(19,4)),
        ],
        'items': [
            Item("belt", '=', Size(3,5,4), 10, '', pos=(1,1))
        ]
    },
    'level_1':{
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%.........................%',
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
        'level': 1,
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
            '%%%%.............%%%%',
            '%%%...............%%%',
            '%%.................%%',
            '%...................%',
            '%%.................%%',
            '%%%...............%%%',
            '%%%%.............%%%%',
            '%%%%%...........%%%%%',
            '%%%%%%.........%%%%%%',
            '%%%%%%%.......%%%%%%%',
            '%%%%%%%%.....%%%%%%%%',
            '%%%%%%%%%...%%%%%%%%%',
            '%%%%%%%%%%<%%%%%%%%%%',
            '%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps':[
            create_peep('balrog', name='Bolrog', pos=(10,18)),
        ],
        'level': 2,
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
            create_peep('human', name='Super Dad', pos=(2,1)),
            create_peep('dodger', name='Dummy', pos=(29,1))
        ]
    }
}

def create_game(info):
    if isinstance(info, str):
        info = DUNGEONS.get(info, None)
        if info is None:
            return None

    return GameModel(
        walls=info['walls'],
        peeps=info['peeps'],
        items=info.get('items', []),
        level=info.get('level', 1),
    )
