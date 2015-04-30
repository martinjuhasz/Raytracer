__author__ = 'martinjuhasz'


class Ray(object):

    def __init__(self, origin, direction):
        super(Ray, self).__init__()

        self.origin = origin
        self.direction = direction.normalized()

    def point_at_parameter(self, t):
        """
        Calculates A point on the ray
        :param t: Length to walk on the ray
        :return: New point on the ray at position t
        """
        return self.origin + self.direction.scale(t)
