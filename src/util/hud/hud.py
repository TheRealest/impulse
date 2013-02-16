from hormcontrolbar import HormControlBar
from phercontrolbar import PherControlBar
from psycontrolbox import PsyControlBox
from nervcontrolbox import NervControlBox
from homebuttonbox import HomeButtonBox


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
