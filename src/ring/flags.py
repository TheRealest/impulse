class Flags:
    def __init__(self, axes):
        self.power = True
        self.calm = True
        self.focus = True
        self.passion = True
        self.discipline = True

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
        s = 'Power: ' + str(self.power) + ', '
        s += 'Calm: ' + str(self.calm) + ', '
        s += 'Focus: ' + str(self.focus) + ', '
        s += 'Passion: ' + str(self.passion) + ', '
        s += 'Discipline: ' + str(self.discipline)

        return s
