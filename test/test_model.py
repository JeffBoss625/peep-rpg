from typing import Tuple

from lib.model import *
from lib.monsters import *


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
    assert hec1.args.pop() == (brog, 'update', 0, 333, 'hp')
    assert hec2.args == []
    a[0] = spark

    assert hec1.args.pop() == (a, 'update', brog, spark, 0)
    brog.hp = 222
    a.append(brog)
    brog.hp = 111

    a.unsubscribe(hec1.collect)

def test_yaml():
    register_yaml([Size])

    s = Size(3,4,5)
    sstr = yaml.dump({'xxx': s})
    assert sstr == 'xxx: 3x4x5\n'
