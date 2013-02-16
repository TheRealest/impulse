from cell import Cell


class Wall(Cell):
    def __init__(self, ship):
        Cell.__init__(self, ship, 'white', None)
        self.char = '|'

    def update(self):
        return Cell.update(self)
