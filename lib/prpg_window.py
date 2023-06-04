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

        # lm = self.model.lightmodel

        # need to update self.write_lines to draw only lit cells (passing the lightmodel into the function)
        def filter_line (xoff, yoff, line):
            ret = ''
            for i, c in enumerate(line):
                if sum(self.model.brightness_at([xoff + i, yoff])) > 0.2:
                    ret += c
                else:
                    ret += ' '
            return ret
        
        params['filter_line'] = filter_line
        self.write_lines(self.model.walls.text, **params)
        for it in self.model.items:
            x, y = it.pos
            if sum(self.model.brightness_at([x, y]))  > 0.2:
                self.write_str(x, y, it.char, **{**params, **{'fg': it.fgcolor, 'bg': it.bgcolor}})
            else:
                pass
        path = self.model.target_path
        if len(path):
            for p in path[1:-1]:
                self.write_str(p[0], p[1], '*', **{**params, **{'fg': COLOR.GREEN, 'bg': COLOR.BLACK}})
            last = path[-1]
            self.change_attr(last[0], last[1], 1, TEXTA.REVERSE, **params)

        for p in self.model.peeps:
            if p.hp > 0:
                x, y = p.pos
                if sum(self.model.brightness_at([x, y])) > 0.2:
                    self.write_str(x, y, p.char, **{**params, **{'fg': p.fgcolor, 'bg': p.bgcolor}})
                else:
                    pass



        if self.model.cursorvis:
            # todo: cursor does not print
            self.curses.curs_set(self.model.cursorvis)
            x, y = self.model.cursorpos
            self.scr.move(y, x)
            self.log(f'move({y}, {x})')

        if self.model.overlay.text:
            text_h = len(self.model.overlay.text)
            text_w = len(self.model.overlay.text[0])
            params = {**self.params, **{
                'align_x': SIDE.LEFT,
                'align_y': SIDE.TOP,
                'text_w': text_w,
                'text_h': text_h
            }}
            self.write_lines(self.model.overlay.text, **params)


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

class PlayerWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def handle_update_event(self, _model, _msg, **kwds):
        if kwds.get('key', '') in {'hp', 'maxhp', 'level', 'speed', 'xp', 'gold'}:
            self.needs_paint = True

    def do_paint(self):
        p = self.model.player  # player

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
            f'gold:   {p.gold}',
            # 'height: ' + str(p.body.size.h)
        ])

class EquipWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def handle_update_event(self, _model, _msg, **kwds):
        key = kwds.get('key', '')
        if key != 'set_player':
            return False
        self.needs_paint = True

    def do_paint(self):
        p = self.model.player
        lines = ['Wearing']
        item_tuples = p.body.item_tuples()
        if item_tuples:
            for index, part, slot, item in item_tuples:
                lines.append(f' {chr(index + 97)}) {item.name}     ')
        else:
            lines.append(' you are naked.                       ')

        lines.append('')
        lines.append('Stuff')
        if p.stuff:
            for item in p.stuff:
                lines.append(f'  {item.name}                    ')
        else:
            lines.append(' nothin.                ')

        self.write_lines(lines)

class StatsWindow(Window):
    def __init__(self, name, parent, **params):
        super().__init__(name, parent, **params)

    def handle_update_event(self, _model, _msg, **kwds):
        key = kwds.get('key', '')
        if key != 'set_player':
            return False
        self.needs_paint = True

    def do_paint(self):
        p = self.model.player
        lines = ['Stats']
        lines.append(' ')
        lines.append(f'Str: {int(p.statscur.str * 100)} / {int(p.stats.str) * 100}       ')
        lines.append(f'Int: {int(p.statscur.int * 100)} / {int(p.stats.int) * 100}       ')
        lines.append(f'Wis: {int(p.statscur.wis * 100)} / {int(p.stats.wis) * 100}       ')
        lines.append(f'Dex: {int(p.statscur.dex * 100)} / {int(p.stats.dex) * 100}       ')
        lines.append(f'Con: {int(p.statscur.con * 100)} / {int(p.stats.con) * 100}       ')
        lines.append(f'Cha: {int(p.statscur.cha * 100)} / {int(p.stats.cha) * 100}       ')

        self.write_lines(lines)

