import yaml

from lib.util import DotDict


def test_dot_dict():
    d1 = DotDict({'a':1, 'b':2})
    assert d1 == {'a':1, 'b':2}
    dstr = yaml.dump(d1, default_flow_style=True)

    assert dstr == '{a: 1, b: 2}\n'

    d2 = dict(d1)
    assert d2 == d1
