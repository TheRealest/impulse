class Galaxy:
    def __init__(self):
        self.constellations = {}

    def add_constellation(self, name, constellation):
        self.constellations[name] = constellation

    def get_location(self, coordinate):
        name, position = coordinate
        return self.constellations[name][position]
