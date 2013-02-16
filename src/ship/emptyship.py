from ship import Ship


class EmptyShip(Ship):
    def __init__(self, win, x, y, width, height):
        Ship.__init__(self, win, x, y, width, height)

        self.place_alien_head(width / 2, height / 2)
