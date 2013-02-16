from ..cell.alien.alienhead import AlienHead
from ..cell.alien.alien import Alien


class Ship(object):
    def __init__(self, win, x, y, width, height):
        self.win = win
        self.x, self.y = x, y
        self.width, self.height = width, height

        self.empty_fgcolor = (150, 150, 200)
        self.empty_bgcolor = (50, 50, 80)
        self.empty_char = '.'

        # to make self.cells coordinates start at [1][1] too, it's initialized as a dict with every coordinate pointing to None (empty cell)
        self.cells = dict([(i + 1, dict([(j + 1, None) for j in range(self.height)])) for i in range(self.width)])

    def update(self):
        for x in self.cells:
            for y in self.cells[x]:
                c = self.cells[x][y]
                absx, absy = self.get_abs_pos(x, y)
                if c:
                    ch, fg, bg = c.update()
                    if not fg:
                        fg = self.empty_fgcolor
                    if not bg:
                        bg = self.empty_bgcolor
                    self.win.putchar(ch, absx, absy, fg, bg)
                else:
                    self.put_empty_cell(absx, absy)

    def get_key(self, dic, value):
        return next(k for k in dic.iterkeys() if dic[k] == value)

    def get_cell_pos(self, cell):
        return next((self.get_key(self.cells, col), self.get_key(col, cell)) for col in self.cells.itervalues() if cell in col.itervalues())

    def get_abs_pos(self, x=1, y=1, cell=None):
        if cell:
            x, y = self.get_cell_pos(cell)
        return (self.x + x - 1, self.y + y - 1)

    def put_empty_cell(self, x, y):
        self.win.putchar(self.empty_char, x, y, fgcolor=self.empty_fgcolor, bgcolor=self.empty_bgcolor)

    def get_neighboring_cells(self, cell):
        adjacent = set([])
        x, y = self.get_cell_pos(cell)
        if x > 1:
            adjacent.add(self.cells[x - 1][y])
            if y > 1:
                adjacent.add(self.cells[x - 1][y - 1])
            if y < self.height:
                adjacent.add(self.cells[x - 1][y + 1])
        if x < self.width:
            adjacent.add(self.cells[x + 1][y])
            if y > 1:
                adjacent.add(self.cells[x + 1][y - 1])
            if y < self.height:
                adjacent.add(self.cells[x + 1][y + 1])
        if y > 1:
            adjacent.add(self.cells[x][y - 1])
        if y < self.height:
            adjacent.add(self.cells[x][y + 1])
        return adjacent

    def place_alien_head(self, x, y):
        self.cells[x][y] = AlienHead(self)
        # doesn't check these cells exist!
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if not self.cells[i][j]:
                    self.cells[i][j] = Alien(self)

    def add_cell(self, cell_type, x, y):
        self.cells[x][y] = cell_type()
