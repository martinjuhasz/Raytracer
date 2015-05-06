from models.objects.EnvironmentObject import EnvironmentObject

__author__ = 'martinjuhasz'


class Triangle(EnvironmentObject):

    def __init__(self, material, b, c, a):
        super(Triangle, self).__init__(material)

        self.a = a
        self.b = b
        self.c = c

        self.u = self.b - self.a
        self.v = self.c - self.a

    def __repr__(self):
        return 'Triangle(material=%s, a=%s, b=%s, c=%s, u=%s, v=%s)' \
               % (self.material, self.a, self.b, self.c, self.u, self.v)

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

    def normal_at(self, point):
        return self.u.cross(self.v).normalized()