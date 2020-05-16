player = {
    'name': 'Bo Bo the Destroyer',
    'type': 'player',
    'char': '@',
    'hp': 5,
    'thaco': 19,
    'speed': 11,
    'tics': 0,
    'ac': 10,
    'weapons': {
        'teeth': {
            'damage': '1d5'
        },
        'scratch': {
            'damage': '3d1'
        },
        'tail': {
            'damage': '2d3'
        },
    },
}

goblin = {
    'name': 'Thark the Goblin',
    'type': 'goblin',
    'char': 'g',
    'hp': 7,
    'speed': 10,
    'tics': 0,
    'thaco': 18,
    'ac': 10,  # without armor
    'weapons': {
        'bite': {
            'damage': '1d3'
        },
        'scratch': {
            'damage': '2d1'
        },
        'short_sword': {
            'damage': '3d4'
        },
    },

}

rat = {
    'name': 'rat',
    'type': 'rat',
    'hp': 5,
    'speed': 13,
    'tics': 0,
    'thaco': 19,
    'ac': 10,
    'weapons': {
        'teeth': {
            'damage': '1d5'
        },
        'scratch': {
            'damage': '3d1'
        },
        'tail': {
            'damage': '2d3'
        },
    },
}

big_bird = {
    'name': 'big bird',
    'hp': 15,
    'speed': 19,
    'tics': 0,
    'thaco': 17,
    'ac': 8,
    'weapons': {
        'beak': {
            'damage': '1d10'
        },
        'talons': {
            'damage': '2d7'
        },
        'wing_blow': {
            'damage': '6d1'
        },
    },
}

model = {
    'walls': [
        '.....xxxxxxxxxxxxxxx',
        '.....xxxx....xxxxxxx',
        '.....xxxx....xxxxxxx',
        '.....xxxx....xxxx..x',
        '.....xxxx....xxxx..x',
        '.....xxxx....xxxx..x',
        '.....xxxx..........x',
        '.....xxxx....xxxxxxx',
        '.....xxxx....xxxxxxx',
        '.....xxxxxxxxxxxxxxx',
    ],
    # a peep is a thing that gets a turn when it's time/speed/elapse is calculated
    'peeps': [
        {'peep': player, 'x': 0, 'y': 2},
        {'peep': goblin, 'x': 0, 'y': 2},
        {'peep': rat, 'x': 2, 'y': 2},
        {'peep': big_bird, 'x': 3, 'y': 5},
    ],
}


def get_model():
    return model
