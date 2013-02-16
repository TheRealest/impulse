from .. import joy
from ... import util


class ControlBox():
    def __init__(self, win, x, y, fgcolor, bgcolor):
        self.win = win
        self.x, self.y = x, y
        self.centerx, self.centery = 0, 0
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor

        self.backdrop = ''
        self.x_axis = ''
        self.y_axis = ''

        self.mark_char = 'X'

    def draw_backdrop(self):
        util.put_chars_array(self.win, self.backdrop, self.x, self.y, self.fgcolor, self.bgcolor)

    def draw_marker(self):
        x, y = joy.get_discrete_axis(self.x_axis), joy.get_discrete_axis(self.y_axis)
        self.win.putchar(self.mark_char, self.centerx + x, self.centery + y)

    def update(self):
        self.draw_backdrop()
        self.draw_marker()
