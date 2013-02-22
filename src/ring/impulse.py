from ..util import joy


class Impulse:
    def __init__(self):
        self.hormone = joy.get_discrete_axis('LEFT-TRIGGER')
        self.pheromone = joy.get_discrete_axis('RIGHT-TRIGGER')
        self.nerve = joy.get_discrete_axis('LEFT-X')
        self.psychic = -joy.get_discrete_axis('LEFT-Y')

        self.flags = Flags([self.hormone, self.pheromone, self.nerve, self.psychic])


class Flags:
    def __init__(self, axes):
        self.power, self.calm, self.focus, self.passion, self.discipline = True, True, True, True, True

        sum, prev = 0, None
        for a in axes:
            if a < 0:
                self.power = False
            elif a > 0:
                self.calm = False

            if a > 1 or a < -1:
                self.discipline = False

            sum += a
            if prev == None:
                prev = a
            else:
                if prev != a:
                    self.passion = False
        if sum != 0:
            self.focus = False

    def __str__(self):
        return str(['Power', self.power, 'Calm', self.calm, 'Focus', self.focus, 'Passion', self.passion, 'Discipline', self.discipline])