# Create sub-array from array selection
a = [1, 2, 3, 4, 5, 6]
b = [v for v in a if 3 < v < 5]

def bad_call():
    raise Exception("I'm bad to the bone")

import traceback

def except_example():
    try:
        bad_call()
    except Exception as e:
        return 'here it is:\n-->' + '-->'.join(traceback.format_tb(e.__traceback__))

def test_args_kwargs(arg1, arg2, arg3, **kwargs):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
    print("kwargs", kwargs)

kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
test_args_kwargs(arg7=7, arg2='2', arg3='3', arg1=1)
# test_args_kwargs('one', 'two', 'three')
# print(except_example())


