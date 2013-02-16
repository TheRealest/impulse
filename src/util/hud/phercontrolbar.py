from controlbar import ControlBar


class PherControlBar(ControlBar):
    def __init__(self, win, x, y):
        ControlBar.__init__(self, win, x, y, (0, 200, 120), (0, 80, 0))

        self.centerx, self.centery = self.x + 1, self.y + 4
        self.backdrop = ['/P\\',
                        '|.|',
                        '|.|',
                        '|.|',
                        '|-|',
                        '|.|',
                        '|.|',
                        '|.|',
                        '\-/']
        self.axis = 'RIGHT-TRIGGER'
