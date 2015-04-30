import math

__author__ = 'martinjuhasz'


class Sphere(object):

    def __init__(self, center, radius):
        super(Sphere, self).__init__()

        self.center = center
        self.radius = radius

    def intersection_parameter(self, ray):
        """
        Tests the current object if it intersects with the given ray
        :param ray: the ray to test
        :return: None or Point of intersection
        """

        # Following formula to calculate the intersection of a ray with a sphere:
        # skalar product (v) of the vector from ray to spehere center (co) plus minus
        # sqrt( co^2 - (skalar of (co, co) - sphere radius^2 ) )
        co = self.center - ray.origin
        v = co.dot(ray.direction)
        discriminant = v*v - co.dot(co) + self.radius * self.radius
        if discriminant < 0:
            return None
        else:
            return v - math.sqrt(discriminant)


    def color_at(self, ray):
        return (255, 0, 0)