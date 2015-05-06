import math

from models.objects.EnvironmentObject import EnvironmentObject


__author__ = 'martinjuhasz'


class Sphere(EnvironmentObject):

    def __init__(self, material, radius, center):
        super(Sphere, self).__init__(material)

        self.center = center
        self.radius = radius

    def __repr__(self):
        return 'Sphere(material=%s, center=%s, radius=%s)' \
               % (self.material, self.center, self.radius)

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

    def normal_at(self, point):
        """
        Returns the normal of the object an the given point
        :param point: Point of the normal starting at
        :return: normal Vector
        """
        return (point - self.center).normalized()