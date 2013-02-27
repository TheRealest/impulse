from ..util import joy
from flags import Flags


class Impulse:
    def __init__(self):
        self.hormone = joy.get_discrete_axis('LEFT-TRIGGER')
        self.pheromone = joy.get_discrete_axis('RIGHT-TRIGGER')
        self.nerve = joy.get_discrete_axis('LEFT-X')
        self.psychic = -joy.get_discrete_axis('LEFT-Y')

        self.flags = Flags([self.hormone, self.pheromone, self.nerve, self.psychic])

        print self.move, self.skip, self.radius

    def _move(self):
        return self.nerve + self.psychic

    def _skip(self):
        return self.pheromone + 3

    def _radius(self):
        return self.hormone + 4

    move = property(_move)
    skip = property(_skip)
    radius = property(_radius)
