from controlbox import ControlBox


class PsyControlBox(ControlBox):
    def __init__(self, win, x, y):
        ControlBox.__init__(self, win, x, y, 'silver', (250, 60, 60))

        self.centerx, self.centery = self.x + 4, self.y + 4
        self.backdrop = ['/-------+-------\\',
                        '|...|...|PSYCHIC|',
                        '|...|...|-------/',
                        '|...|...|',
                        '|---+---|',
                        '|...|...|',
                        '|...|...|',
                        '|...|...|',
                        '\-------/']
        self.x_axis = 'LEFT-X'
        self.y_axis = 'LEFT-Y'
