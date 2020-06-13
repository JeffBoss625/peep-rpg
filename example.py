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


print(except_example())
