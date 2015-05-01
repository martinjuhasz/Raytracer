__author__ = 'martinjuhasz'

import math


class Vector(object):

    def __init__(self, direction):
        super(Vector, self).__init__()

        self.direction = direction

    def __repr__(self):
        return 'Vector(%s)' % (self.direction,)

    def __getitem__(self, item):
        return self.direction[item]

    def __add__(self, other):
        """
        Adds two Vectors
        :param other: the second Vector for calculation
        :return: new, resulting Vector
        """
        x = self.direction[0] + other[0]
        y = self.direction[1] + other[1]
        z = self.direction[2] + other[2]
        return Vector([x, y, z])

    def __sub__(self, other):
        """
        Subtracts two Vectors
        :param other: the second Vector for calculation
        :return: new, resulting Vector
        """
        x = self.direction[0] - other[0]
        y = self.direction[1] - other[1]
        z = self.direction[2] - other[2]
        return Vector([x, y, z])

    def __div__(self, other):
        """
        Divides the Vector with a scalar
        :param other: The scalar
        :return: new, resulting Vector
        """
        x = self.direction[0] / other
        y = self.direction[1] / other
        z = self.direction[2] / other
        return Vector([x, y, z])

    def length(self):
        """
        Calculates the length of a vector
        :return: Number with the Vectors length
        """
        return math.sqrt(
            math.pow(self.direction[0], 2) +
            math.pow(self.direction[1], 2) +
            math.pow(self.direction[2], 2))

    def normalized(self):
        """
        Normalizes the current Vector
        :return: new normalized Vector
        """
        length = self.length()
        x = self.direction[0] / length
        y = self.direction[1] / length
        z = self.direction[2] / length
        return Vector([x, y, z])

    def scale(self, scale):
        """
        Scales a Vector
        :param scale: The Scale that should be applied to the Vector
        :return: new scaled Vector
        """
        x = self.direction[0] * scale
        y = self.direction[1] * scale
        z = self.direction[2] * scale
        return Vector([x, y, z])

    def dot(self, vector):
        """
        Calculates the dot(scalar) product
        :param vector: the second vector of the dot product
        :return: value of the calculation
        """
        x = self.direction[0] * vector[0]
        y = self.direction[1] * vector[1]
        z = self.direction[2] * vector[2]
        return x+y+z

    def cross(self, vector):
        """
        Caclulates the cross product
        :param vector: the second vector of the cross product
        :return: Resulting vector
        """
        x = self.direction[1] * vector[2] - self.direction[2] * vector[1]
        y = self.direction[2] * vector[0] - self.direction[0] * vector[2]
        z = self.direction[0] * vector[1] - self.direction[1] * vector[0]
        return Vector([x, y, z])
