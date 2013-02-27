### CONSTANTS ###
CONNECTION = 'connection'
REVERSECONNECTION = 'reverse connection'
ACTION = 'action'


class Constellation:
    def __init__(self, size):
        self.locations = [None] * size

    def add_connection(self, position, other, forward=True):
        if forward:
            self[position] = (CONNECTION, other)
        else:
            self[position] = (REVERSECONNECTION, other)
            

    ### CONTAINER-LIKE BEHAVIOR ###
    def __len__(self):
        return len(self.locations)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= len(self):
                raise IndexError('Constellation index %d out of range' % index)
            else:
                if index < 0:
                    index += len(self)
                return self.locations[index]
        elif isinstance(index, slice):
            return [self[i] for i in range(*index.indices(len(self)))]
        else:
            raise TypeError('Constellation index must be integer or slice')

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index >= len(self):
                raise IndexError('Constellation index %d out of range' % index)
            else:
                if index < 0:
                    index += len(self)
                self.locations[index] = value
        else:
            raise TypeError('Constellation set index must be integer')

    def __delitem__(self, index):
        if index is None:
            self.locations = [None] * len(self)
        elif isinstance(index, int):
            if index >= len(self):
                raise IndexError('Constellation index %d out of range' % index)
            else:
                if index < 0:
                    index += len(self)
                self.locations[index] = None
        else:
            raise TypeError('Constellation index must be integer or slice')

    def __repr__(self):
        return str(self.locations)
