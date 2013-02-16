from ... import util
from controlbox import ControlBox


class NervControlBox(ControlBox):
    def __init__(self, win, x, y):
        ControlBox.__init__(self, win, x, y, 'aqua', 'navy')

        self.centerx, self.centery = self.x + 12, self.y + 4
        self.backdrop = ['/-------\\',
                        '|...|...|',
                        '|...|...|',
                        '|...|...|',
                        '|---+---|',
                        '|...|...|',
                        '/-------|...|...|',
                        '| NERVE |...|...|',
                        '\---------------/']
        self.x_axis = 'RIGHT-X'
        self.y_axis = 'RIGHT-Y'

    def draw_backdrop(self):
        util.put_chars_array(self.win, self.backdrop[:6], self.x + 8, self.y, self.fgcolor, self.bgcolor)
        util.put_chars_array(self.win, self.backdrop[6:], self.x, self.y + 6, self.fgcolor, self.bgcolor)
