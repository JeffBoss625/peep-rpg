from lib.constants import GAME_SETTINGS, TEXTA
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
            self.write_str(it.pos[0], it.pos[1], it.char, **{**params, **{'fg': it.fgcolor, 'bg': it.bgcolor}})

        for p in self.model.peeps:
            if p.hp > 0:
                self.write_str(p.pos[0], p.pos[1], p.char, **{**params, **{'fg': p.fgcolor, 'bg': p.bgcolor}})

        path = self.model.target_path
        if len(path):
            for p in path[1:-1]:
                self.write_str(p[0], p[1], '*', **{**params, **{'fg': COLOR.GREEN, 'bg': COLOR.BLACK}})
            last = path[-1]
            self.change_attr(last[0], last[1], 1, TEXTA.REVERSE, **params)

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
        p = self.model
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

    def handle_update_event(self, _model, _msg, **kwds):
        if kwds.get('key', '') in {'hp', 'maxhp', 'level', 'speed', 'xp'}:
            self.needs_paint = True

    def do_paint(self):
        p = self.model  # player

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

        hp_str = f'{hp}/{p.maxhp}'

        self.write_lines([
            p.name,
            f'level:  {p.level}',
            f'xp:     {floor(p.exp)}/{floor(xptolevel_calc(p.level, p.level_factor, GAME_SETTINGS.BASE_EXP_TO_LEVEL))}',
            f'hp:     {hp_str}',
            f'speed:  {p.speed}',
            # 'height: ' + str(p.body.size.h)
        ])

class EquipWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def handle_update_event(self, _model, _msg, **_kwds):
        return

    def do_paint(self):
        p = self.model
        lines = ['Equipment']
        for part in p.body.parts:
            for slot in part.slots:
                if slot.item:
                    lines.append(part.name)
                    lines.append(f'  {slot.item.name}')

        for item in p.stuff:
            lines.append(f'{item.name}                      ')

        if len(lines) == 1:
            lines.append(' you are naked.')
        self.write_lines(lines)
