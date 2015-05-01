__author__ = 'martinjuhasz'


class Triangle(object):

    def __init__(self, a, b, c):
        super(Triangle, self).__init__()

        self.a = a
        self.b = b
        self.c = c

        self.u = self.b - self.a
        self.v = self.c - self.a

    def intersection_parameter(self, ray):
        """
        Tests the current object if it intersects with the given ray
        :param ray: the ray to test
        :return: None or Point of intersection
        """

        w = ray.origin - self.a
        dv = ray.direction.cross(self.v)
        dvu = dv.dot(self.u)

        if dvu == 0.0:
            return None

        wu = w.cross(self.u)
        r = dv.dot(w) / dvu
        s = wu.dot(ray.direction) / dvu

        if 0 <= r <= 1 and 0 <= s <= 1 and r + s <= 1:
            return wu.dot(self.v) / dvu
        else:
            return None

    def color_at(self, ray):
        return (115, 141, 201)
