class Control:
    def __init__(self, win, ship, alienhead):
        self.win = win
        self.ship = ship
        self.alienhead = alienhead

        self.selected = None
        self.was_selected = set([])
        self.prev_selected = {}
        self.selected_tint = (50, 100, 100)

    def update(self):
        pass
        # update selection timer if it exists
        # selection timer emits 'selectnext' signal periodically

    # def clear_selected(self):
    #     self.was_selected |= self.selected
    #     self.selected.clear()

    # def add_selected(self, new):
    #     if isinstance(new, list):
    #         for n in new:
    #             self.selected.add(n)
    #     else:
    #         self.selected.add(new)

    def select_next(self):
        pass

    def tint_selected(self):
        x, y = self.ship.get_abs_pos(cell=self.selected)
        r, g, b = self.selected_tint
        self.win.settint(r, g, b, (x, y, 1, 1))

    def untint_selected(self):
        x, y = self.ship.get_abs_pos(cell=self.selected)
        self.win.settint(0, 0, 0, (x, y, 1, 1))

    def capture_impulse(self):
        pass
        # return impulse

    def deliver_impulse(self, cell, impulse):
        pass

    def flash_selected(self):
        pass

    def start_selection(self):
        pass
        # subscribe select_next() to 'selectnext' signal
