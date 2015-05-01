from models.EnvironmentObject import EnvironmentObject

__author__ = 'martinjuhasz'

class Plane(EnvironmentObject):
    def __init__(self, center, normal):
        super(Plane, self).__init__()

        self.center = center
        self.normal = normal

    def intersection_parameter(self, ray):
        """
        Tests the current object if it intersects with the given ray
        :param ray: the ray to test
        :return: None or Point of intersection
        """

        op = ray.origin - self.center
        a = op.dot(self.normal)
        b = ray.direction.dot(self.normal)

        if b:
            return -a/b
        else:
            return None

    def color_at(self, ray, is_shadowed=False):
        color = (68, 179, 90)

        if is_shadowed:
            return self.add_shadow(color)
        return color