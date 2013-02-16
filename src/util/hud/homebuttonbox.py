from .. import joy
from ... import util


class HomeButtonBox:
    def __init__(self, win, x, y):
        self.win = win
        self.x, self.y = x, y
        self.fgcolor = (60, 60, 60)
        self.bgcolor = (200, 200, 200)
        self.tint = (-100, -10, -100)

        self.backdrop = ['O======O',
                        '( HOME )',
                        'O======O']

    def draw_backdrop(self):
        util.put_chars_array(self.win, self.backdrop, self.x, self.y, self.fgcolor, self.bgcolor)

    def set_tint(self):
        if joy.peek_button('HOME'):
            r, g, b = self.tint
            self.win.settint(r, g, b, (self.x, self.y, 8, 3))
        else:
            self.win.settint(0, 0, 0, (self.x, self.y, 8, 3))

    def update(self):
        self.draw_backdrop()
        self.set_tint()
