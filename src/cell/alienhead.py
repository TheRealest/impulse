from ..cell import Cell


class AlienHead(Cell):
    def __init__(self, ship):
        Cell.__init__(self, ship, (180, 255, 180), None, '@')

    def update(self):
        return Cell.update(self)
