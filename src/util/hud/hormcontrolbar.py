from controlbar import ControlBar


class HormControlBar(ControlBar):
    def __init__(self, win, x, y):
        ControlBar.__init__(self, win, x, y, 'lime', 'olive')

        self.centerx, self.centery = self.x + 1, self.y + 4
        self.backdrop = ['/H\\',
                        '|.|',
                        '|.|',
                        '|.|',
                        '|-|',
                        '|.|',
                        '|.|',
                        '|.|',
                        '\-/']
        self.axis = 'LEFT-TRIGGER'
