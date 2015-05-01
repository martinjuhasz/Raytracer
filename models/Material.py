from models.Color import Color
from models.Point import Point

__author__ = 'martinjuhasz'


class Material(object):
    def __init__(self, color):
        super(Material, self).__init__()

        self.color = Color(color[0], color[1], color[2])

        # can be overridden in material custom subclasses
        self.shadowStrength = 0.7
        self.ambientConstant = 0.5
        self.diffuseConstant = 0.3
        self.specularConstant = 0.4
        self.specularScaling = 20

    def add_shadow(self, color):
        return color * Color(self.shadowStrength, self.shadowStrength, self.shadowStrength)

    def calculate_diffuse(self, color, normal, light, hit_point, light_vector):
        return color * self.diffuseConstant * light_vector.dot(normal)

    def calculate_specular(self, color, ray, hit_point, light, normal, light_vector):
        reflected_light_vector = (light_vector - normal.scale(2 * normal.dot(light_vector))).normalized()
        negative_ray_vector = ray.direction.scale(-1)
        return color * self.specularConstant * (reflected_light_vector.dot(negative_ray_vector) ** self.specularScaling)

    def get_color(self, ray, light, normal, hit_point, ambient_color, is_shadowed):

        color = self.color
        light_vector = (Point(light.origin) - hit_point).normalized()

        # TODO: wikipedia suggesst ambient color here?
        ambient_part = color * self.ambientConstant
        diffuse_part = self.calculate_diffuse(color, normal, light, hit_point, light_vector)
        specular_part = Color(0, 0, 0)

        # angle between light and normal > 90 deg => not facing in same direction => no reflection
        if normal.dot(light_vector) > 0:
            specular_part = self.calculate_specular(color, ray, hit_point, light, normal, light_vector)

        color = ambient_part + diffuse_part + specular_part

        if is_shadowed:
            return self.add_shadow(color)
        return color

