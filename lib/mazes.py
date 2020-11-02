from lib.monsters import monster_by_name
from lib.peep_types import create_peep
from lib.players import player_by_name


dungeon1 = [
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
]
dungeon1_peeps = [
    player_by_name('Super Dad', pos=(1,2), hp=40),
    monster_by_name('Thark', pos=(2,2), hp=10),
    monster_by_name('Spark', pos=(24,7), hp=50),
    monster_by_name('Brog', pos=(14,20), hp=200),
    create_peep('big bird', name='Beaky', pos=(18,4)),
    create_peep('giant rat', name='Scriggle', pos=(19,4)),
]
dungeon1_items = [

]


open = [
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
]
open_peeps = [
    create_peep('human', name='Super Dad', pos=(2,2)),
    create_peep('red dragon', name='Spark', pos=(14,14))

]
shooting = [
    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
    '%.............................%',
    '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%',
]
shooting_peeps = [
    create_peep('human', name='Super Dad', pos=(2,2)),
    create_peep('red dragon', name='Spark', pos=(2,29))
]