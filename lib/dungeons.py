from lib.model import Size
from lib.monsters import monster_by_name
from lib.peep_types import create_peep
from lib.players import player_by_name
from lib.dungeon import Dungeon
from lib.items.item import Item
# import lib.items.bow

DUNGEONS = {
    'dungeon1': {
        'walls': [
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
            '%....####....######%.........%',
            '%....####....######%.........%',
            '%....####....####..#.........%',
            '%............####..#.........%',
            '%....####....####............%',
            '%....####..........#.........%',
            '%....####....#######.........%',
            '%....####....#######.........%',
            '%###########################.%',
            '%###########################.%',
            '%#############...............%',
            '%#############.##############%',
            '%#############.##############%',
            '%#########.........##########%',
            '%#####..................#####%',
            '%####....................####%',
            '%####....................####%',
            '%#####..................#####%',
            '%#########.........##########%',
            '%#############.##############%',
            '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
        ],
        'peeps':[
            player_by_name('Super Dad', pos=(1,2), maxhp=40),
            monster_by_name('Thark', pos=(2,2), maxhp=10),
            monster_by_name('Spark', pos=(24,7), maxhp=50),
            monster_by_name('Brog', pos=(14,20), maxhp=200),
            create_peep('big bird', name='Beaky', pos=(18,4)),
            create_peep('giant rat', name='Scriggle', pos=(19,4)),
        ],
        'items': [
            Item("belt", '=', Size(3,5,4), 10, '', pos=(1,1))
        ]
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

def create_dungeon(info):
    if isinstance(info, str):
        info = DUNGEONS[info]

    return Dungeon(
        walls=info['walls'],
        peeps=info['peeps'],
        player=info['peeps'][0],
        items=info.get('items', []),
    )