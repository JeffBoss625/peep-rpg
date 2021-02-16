#!/usr/bin/python

if __name__ == '__main__':
    codes = [
        ('TAB', 10),
        ('RET', 13),
        ('ESC', 27),
        ('SPC', 32),
    ]
    for i in range(33, 127):
        codes.append((chr(i), i))
    codes.append(('DEL', 127))

    print('class KEY:')
    for name, code in codes:
        print(f'    {name} = {code}')