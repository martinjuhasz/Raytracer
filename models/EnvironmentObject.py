__author__ = 'martinjuhasz'


class EnvironmentObject(object):

    def __init__(self, material):
        super(EnvironmentObject, self).__init__()
        self.material = material

    def intersection_parameter(self, ray):
        raise NotImplementedError

    def color_at(self, ray, light, hit_point, ambient_color, is_shadowed=False):
        return self.material.get_color(ray, light, self.normal_at(hit_point), hit_point, ambient_color, is_shadowed)

    def normal_at(self, point):
        raise NotImplementedError

    def get_reflected_color(self, color):
        return self.material.get_reflected_color(color)
