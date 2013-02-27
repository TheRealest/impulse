class Cell:
    def __init__(self, level, fgcolor, bgcolor, char=''):
        self.level = level
        self.fgcolor = fgcolor
        self.bgcolor = bgcolor
        self.char = char

        self.adjacent = set([])

    def update_adjacent(self):
        self.adjacent = self.level.get_neighboring_cells(self)

    def update(self):
        return self.char, self.fgcolor, self.bgcolor
