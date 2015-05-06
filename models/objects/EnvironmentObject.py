__author__ = 'martinjuhasz'


class EnvironmentObject(object):

    def __init__(self, material):
        super(EnvironmentObject, self).__init__()
        self.material = material

    def intersection_parameter(self, ray):
        """
        Tests the current object if it intersects with the given ray
        :param ray: the ray to test
        :return: None or Point of intersection
        """
        raise NotImplementedError

    def color_at(self, ray, lights, hit_point, ambient_color, shadows=0):
        """
        Returns the final color of an Object at a given point based on its material
        :param ray: a Ray from the Camera towards the hit point
        :param lights: List of all light sources
        :param hit_point: Point of collision
        :param ambient_color: overall ambient color of the environment (currently not used)
        :param shadows: Number of overlapping shadows at the hit point
        :return: Color of the Material
        """
        return self.material.get_color(ray, lights, self.normal_at(hit_point), hit_point, ambient_color, shadows)

    def normal_at(self, point):
        """
        Returns the normal of the object an the given point
        :param point: Point of the normal starting at
        :return: normal Vector
        """
        raise NotImplementedError

    def get_reflected_color(self, color):
        """
        Returns the reflected part of a color on its object
        :param color: the Color to reflect
        :return: reflected Color
        """
        return self.material.get_reflected_color(color)
