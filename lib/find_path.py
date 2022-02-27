from time import sleep

from lib.items import clothes

class FLog:
    def __init__(self, control):
        self.control = control
        self.game = control.game_model

    def is_wall (self, x, y):
        sleep(0.1)
        c = self.game.maze_model.walls.char_at(x, y)
        is_w = c == '%' or c == '&'
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
    x = src[0]
    y = src[1]
    while True:
        x += 1
        if flog.is_wall(x, y):
            flog.mark_exit(x, y+1)
            break

