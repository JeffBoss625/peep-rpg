from lib.constants import GAME_SETTINGS
from lib.window import *
from lib.pclass import xptolevel_calc
from math import floor

class MazeWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        text_h = len(self.model.walls.text)
        text_w = len(self.model.walls.text[0])
        params = {**self.params, **{'text_w': text_w, 'text_h': text_h}}
        self.write_lines(self.model.walls.text, **params)

        for it in self.model.items:
            self.write_str(it.pos[0], it.pos[1], it.char, it.fgcolor, it.bgcolor, **params)

        for p in self.model.peeps:
            if p.hp > 0:
                self.write_str(p.pos[0], p.pos[1], p.char, p.fgcolor, p.bgcolor, **params)

        for p in self.model.target_path[1:]:
            self.write_str(p[0], p[1], '*', **params)

        if self.model.cursorvis:
            # todo: cursor does not print
            self.curses.curs_set(self.model.cursorvis)
            x, y = self.model.cursorpos
            self.scr.move(y, x)
            self.log(f'move({y}, {x})')

class TitleWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            p.name,
            # class
            # level
            # height
            # age
        ])

class StatsWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player

        # x = 0
        # y = 0
        # self.write_str(x, y, p.name)
        # y += 1
        # self.write_str(x, y, f'level:  {p.level}')
        # y += 1
        #

        hp = floor(p.hp)
        hp_rat = hp/p.maxhp
        if hp_rat < 0.25:
            hp_col = COLOR.RED
        elif hp_rat < 0.8:
            hp_col = COLOR.YELLOW
        else:
            hp_col = COLOR.GREEN

        self.write_lines([
            p.name,
            f'level:  {p.level}',
            f'xp:     {floor(p.exp)}/{floor(xptolevel_calc(p.level, p.level_factor, GAME_SETTINGS.BASEEXPTOLEVEL))}',
            f'hp:     <:fg:{hp_col}:>{floor(p.hp)}/{p.maxhp}',
            f'speed:  {p.speed}',
            # 'height: ' + str(p.body.size.h)
        ])

class EquipWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def do_paint(self):
        p = self.model.player
        self.write_lines([
            'equip',
        ])
