from models.Vector import Vector

__author__ = 'martinjuhasz'


class Point(object):

    def __init__(self, position):
        super(Point, self).__init__()

        self.position = position

    def __repr__(self):
        return 'Point(%s)' % (self.position,)

    def __getitem__(self, item):
        return self.position[item]

    def __add__(self, vector):
        """
        Adds a Vector to the Point
        :param vector: The Vector that should be added
        :return: Resulting Point
        """
        x = vector[0] + self.position[0]
        y = vector[1] + self.position[1]
        z = vector[2] + self.position[2]
        return Point(x, y, z)

    def __sub__(self, other):
        """
        Subtracts the other Point from the current one
        :param other: A point that should be subtracted
        :return: The resulting vector of the calculation
        """
        x = self.position[0] - other[0]
        y = self.position[1] - other[1]
        z = self.position[2] - other[2]
        return Vector([x, y, z])