class Cell:
    def __init__(self, ship, fgcolor, bgcolor, char=''):
        self.ship = ship
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.char = char

        self.adjacent = set([])

    def update_adjacent(self):
        self.adjacent = self.ship.get_neighboring_cells(self)

    def update(self):
        return self.char, self.fgcolor, self.bgcolor
