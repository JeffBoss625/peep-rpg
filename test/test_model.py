import yaml

from lib.model import ModelList, ModelDict, Size, size, register_yaml, TextModel
from lib.monsters import MONSTERS_BY_NAME


class Hector:
    def __init__(self):
        self.args = []

    def collect(self, model, msg, **args):
        self.args.append((model, msg) + tuple(args.values()))

    def print_args(self):
        for a in self.args:
            print(a)

def test_model_list():
    hec1 = Hector()
    hec2 = Hector()
    brog = MONSTERS_BY_NAME['Brog']
    brog.hp = 65
    spark = MONSTERS_BY_NAME['Spark']

    a = ModelList()
    a.subscribe(hec1.collect)
    a.subscribe(hec2.collect)

    a.append(brog)
    assert a[0] == brog
    assert hec1.args.pop() == (a, 'update', None, brog, 0)
    assert hec2.args.pop() == (a, 'update', None, brog, 0)
    a.unsubscribe(hec2.collect)

    brog.hp = 333
    assert hec1.args.pop() == (brog, 'update', 65, 333, 'hp')
    assert hec2.args == []
    a[0] = spark

    assert hec1.args.pop() == (a, 'update', brog, spark, 0)
    brog.hp = 222
    a.append(brog)
    brog.hp = 111

    a.unsubscribe(hec1.collect)

def test_yaml():
    register_yaml([Size])

    s = size(3,4,5)
    sstr = yaml.dump({'s': s})
    assert sstr == 's: 3x4x5\n'

    a = ModelList()
    a.extend([1,2,3])
    astr = yaml.dump({'a': a}, default_flow_style=True)
    assert astr == '{a: [1, 2, 3]}\n'

def test_list():
    a = ModelList()
    a.extend([1,2,3])
    a.append(4)
    astr = yaml.dump(a, Dumper=yaml.Dumper, default_flow_style=True)
    assert astr == '[1, 2, 3, 4]\n'

def test_dict():
    a = ModelDict()
    a['a'] = 1
    a.b = 2
    a['c'] = 3

    assert a.b == 2
    assert a['b'] == 2

    astr = yaml.dump(a, Dumper=yaml.Dumper, default_flow_style=True)
    assert astr == '{a: 1, b: 2, c: 3}\n'

def test_text_model():
    t = TextModel()
    hec1 = Hector()
    t.subscribe(hec1.collect)

    txt = [
        'A 0123456789',
        'B 0123456789',
        'C 0123456789',
    ]
    t.extend(txt)
    u = hec1.args.pop()
    assert u[1] == 'update'
    assert u[2] is None
    assert u[3] == txt

    t.replace_region(0, 1, ['Z'])
    u = hec1.args.pop()
    assert u[1] == 'update'
    assert u[2] == ['B']
    assert u[3] == ['Z']
    assert t.text == [
        'A 0123456789',
        'Z 0123456789',
        'C 0123456789',
    ]

    t.replace_region(4, 1, ['@@@','###'])
    u = hec1.args.pop()
    assert u[1] == 'update'
    assert u[2] == ['234','234']
    assert u[3] == ['@@@','###']
    assert t.text == [
        'A 0123456789',
        'Z 01@@@56789',
        'C 01###56789',
    ]
