from time import sleep

from lib.items import clothes

class FLog:
    def __init__(self, control):
        self.control = control
        self.game = control.game_model

    def is_wall(self, x, y):
        sleep(0.03)
        c = self.game.maze_model.walls.char_at(x, y)
        is_w = c == '%' or c == '#'
        item = clothes.belt(pos=(x, y))
        if is_w:
            item.char = '&'
        else:
            item.char = '_'

        self.game.maze_model.items.append(item)
        self.control.root_layout.window.paint()
        return is_w

    def mark_exit(self, x, y):
        sleep(0.2)
        item = clothes.belt(pos=(x, y))
        item.char = 'X'
        self.game.maze_model.items.append(item)
        self.control.root_layout.window.paint()

def find_rooms(control, input_key):
    _find_rooms(control.game_model.player.pos, (), FLog(control))

def _find_rooms(src, tgt, flog):
    facing = None
    hall = []
    pos = list(src)
    been = []
    while flog.is_wall(pos[0] - 1, pos[1]) is False:
        pos[0] = pos[0] - 1
    if flog.is_wall(pos[0], pos[1] - 1) is False:
        facing = 'up'
    else:
        facing = 'right'
    while pos not in been:

        while facing == 'up':
            while flog.is_wall(pos[0], pos[1] - 1) is False and flog.is_wall(pos[0] - 1, pos[1]):  # FACING UP
                if flog.is_wall(pos[0] + 1, pos[1]):
                    flog.mark_exit(pos[0], pos[1])
                    pos[0] = pos[0] + 1
                    pos[1] = pos[1] + 1
                    facing = 'right'
                    break
                been.append(list(pos))
                pos[1] = pos[1] - 1
            if facing == 'up':
                if flog.is_wall(pos[0], pos[1] - 1):
                    facing = 'right'
                    pos[0] = pos[0] + 1
                else:
                    facing = 'left'
                    pos[0] = pos[0] - 1

        while facing == 'down':
            while flog.is_wall(pos[0], pos[1] + 1) is False and flog.is_wall(pos[0] + 1, pos[1]):  # FACING DOWN
                if flog.is_wall(pos[0] - 1, pos[1]):
                    flog.mark_exit(pos[0], pos[1])
                    pos[0] = pos[0] - 1
                    pos[1] = pos[1] - 1
                    facing = 'right'
                    break
                # been here
                been.append(list(pos))
                pos[1] = pos[1] + 1
            if facing == 'down':
                if flog.is_wall(pos[0], pos[1] + 1):
                    facing = 'left'
                    pos[0] = pos[0] - 1
                else:
                    facing = 'right'
                    pos[0] = pos[0] + 1

        while facing == 'right':
            while flog.is_wall(pos[0] + 1, pos[1]) is False and flog.is_wall(pos[0], pos[1] - 1):  # FACING RIGHT
                if flog.is_wall(pos[0], pos[1] + 1):
                    flog.mark_exit(pos[0], pos[1])
                    pos[0] = pos[0] - 1
                    pos[1] = pos[1] + 1
                    facing = 'down'
                    break
                # been here
                been.append(list(pos))
                pos[0] = pos[0] + 1
            if facing == 'right':
                if flog.is_wall(pos[0] + 1, pos[1]):
                    facing = 'down'
                    pos[1] = pos[1] + 1
                else:
                    facing = 'up'
                    pos[1] = pos[1] - 1

        while facing == "left":
            while flog.is_wall(pos[0] - 1, pos[1]) is False and flog.is_wall(pos[0], pos[1] + 1):  # FACING LEFT
                if flog.is_wall(pos[0], pos[1] - 1):
                    flog.mark_exit(pos[0], pos[1])
                    pos[0] = pos[0] + 1
                    pos[1] = pos[1] - 1
                    facing = 'up'
                    break
                # been here
                been.append(list(pos))
                pos[0] = pos[0] - 1
            if facing == 'left':
                if flog.is_wall(pos[0] - 1, pos[1]):
                    facing = 'up'
                    pos[1] = pos[1] - 1
                else:
                    facing = 'down'
                    pos[1] = pos[1] + 1
