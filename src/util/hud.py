class HUD:
    def __init__(self, win, x, y):
        self.horm_control_bar = HormControlBar(win, x, y)
        self.psy_control_box = PsyControlBox(win, x + 3, y)
        self.nerv_control_box = NervControlBox(win, x + 12, y)
        self.pher_control_bar = PherControlBar(win, x + 29, y)
        self.home_button_box = HomeButtonBox(win, x + 12, y + 3)

    def update(self):
        self.horm_control_bar.update()
        self.psy_control_box.update()
        self.nerv_control_box.update()
        self.pher_control_bar.update()
        self.home_button_box.update()


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
        put_chars_array(self.win, self.backdrop, self.x, self.y, self.fgcolor, self.bgcolor)

    def draw_marker(self):
        x, y = joy.get_discrete_axis(self.x_axis), joy.get_discrete_axis(self.y_axis)
        self.win.putchar(self.mark_char, self.centerx + x, self.centery + y)

    def update(self):
        self.draw_backdrop()
        self.draw_marker()


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
                        '|NERVE  |...|...|',
                        '\---------------/']
        self.x_axis = 'RIGHT-X'
        self.y_axis = 'RIGHT-Y'

    def draw_backdrop(self):
        put_chars_array(self.win, self.backdrop[:6], self.x + 8, self.y, self.fgcolor, self.bgcolor)
        put_chars_array(self.win, self.backdrop[6:], self.x, self.y + 6, self.fgcolor, self.bgcolor)


class ControlBar(ControlBox):
    def __init__(self, win, x, y, fgcolor, bgcolor):
        ControlBox.__init__(self, win, x, y, fgcolor, bgcolor)
        self.axis = ''

    def draw_marker(self):
        h = -joy.get_discrete_axis(self.axis)
        self.win.putchar(self.mark_char, self.centerx, self.centery + h)


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
        put_chars_array(self.win, self.backdrop, self.x, self.y, self.fgcolor, self.bgcolor)

    def set_tint(self):
        if joy.peek_button('HOME'):
            r, g, b = self.tint
            self.win.settint(r, g, b, (self.x, self.y, 8, 3))
        else:
            self.win.settint(0, 0, 0, (self.x, self.y, 8, 3))

    def update(self):
        self.draw_backdrop()
        self.set_tint()
