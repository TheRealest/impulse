from .. import joy
from controlbox import ControlBox


class ControlBar(ControlBox):
    def __init__(self, win, x, y, fgcolor, bgcolor):
        ControlBox.__init__(self, win, x, y, fgcolor, bgcolor)
        self.axis = ''

    def draw_marker(self):
        h = -joy.get_discrete_axis(self.axis)
        self.win.putchar(self.mark_char, self.centerx, self.centery + h)
