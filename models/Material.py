from models.Color import Color
from models.Point import Point

__author__ = 'martinjuhasz'


class Material(object):
    def __init__(self, color, reflection_strength=0.3, shadow_strength=0.7, ambient_constant=0.5, diffuse_constant=0.3,
                 specular_constant=0.4, specular_scaling=20):
        super(Material, self).__init__()

        self.color = Color(color[0], color[1], color[2])

        self.reflection_strength = reflection_strength
        self.shadow_strength = shadow_strength
        self.ambient_constant = ambient_constant
        self.diffuse_constant = diffuse_constant
        self.specular_constant = specular_constant
        self.specular_scaling = specular_scaling

    def base_color_at(self, point):
        return self.color

    def add_shadow(self, color):
        return color * Color(self.shadow_strength, self.shadow_strength, self.shadow_strength)

    def calculate_diffuse(self, color, normal, light, hit_point, light_vector):
        return color * self.diffuse_constant * light_vector.dot(normal)

    def calculate_specular(self, color, ray, hit_point, light, normal, light_vector):
        reflected_light_vector = light_vector.mirrored_at(normal).normalized()
        negative_ray_vector = ray.direction.scale(-1)
        return color * self.specular_constant * (
            reflected_light_vector.dot(negative_ray_vector) ** self.specular_scaling)

    def get_color(self, ray, light, normal, hit_point, ambient_color, is_shadowed):

        color = self.base_color_at(hit_point)
        light_vector = (Point(light.origin) - hit_point).normalized()

        # TODO: wikipedia suggesst ambient color here?
        ambient_part = color * self.ambient_constant
        diffuse_part = self.calculate_diffuse(color, normal, light, hit_point, light_vector)
        specular_part = Color(0, 0, 0)

        # angle between light and normal > 90 deg => not facing in same direction => no reflection
        if normal.dot(light_vector) > 0:
            specular_part = self.calculate_specular(color, ray, hit_point, light, normal, light_vector)

        color = ambient_part + diffuse_part + specular_part

        if is_shadowed:
            return self.add_shadow(color)
        return color

    def get_reflected_color(self, color):
        if self.reflection_strength > 0:
            return color * self.reflection_strength
        return Color(0, 0, 0)
