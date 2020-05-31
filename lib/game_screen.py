from lib.term import Term

# An abstraction of a terminal game screen with controls to refresh and update what is shown
class Screen:
    def __init__(self, curses_scr, model):
        self._term = Term(curses_scr)
        self.model = model
        self.model.out = self  # allow the model itself to be used for term printed output

    # print messages and standard output
    def print(self, *args):
        line = ' '.join([str(a) for a in args])
        self.model.message(line)
        self.paint()

    def get_key(self):
        return self._term.get_key()

    # paint the entire screen - all that is visible
    def paint(self):
        term = self._term
        model = self.model
        x_margin = 3
        y_margin = 3
        term.clear()

        term.move_to(x_margin, y_margin)
        self._draw_stats()

        term.move(0, y_margin)
        self._draw_maze_area()

        term.move(0, y_margin)
        term.move_to(len(model.maze[0]) + x_margin * 2, y_margin)
        term.write_lines(model.messages[-12:])

        term.move_to(0, 0)
        term.refresh()

    def _draw_stats(self):
        p = self.model.player
        self._term.write_lines([
            p.name,
            'hp:    ' + str(p.hp) + '/' + str(p.maxhp),
            'speed: ' + str(p.speed),
            ])

    def _draw_maze_area(self):
        term = self._term
        model = self.model
        x, y = term.get_xy()

        term.write_lines(model.maze)

        for p in model.peeps:
            term.move_to(x + p.x, y + p.y)
            term.write_char(p.char,  p.fgcolor, p.bgcolor)

        term.move_to(x, y + len(model.maze))  # move cursor to end of maze
