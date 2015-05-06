from models.Color import Color
from models.Point import Point

__author__ = 'martinjuhasz'


class Material(object):
    """
    Material Class that represents the structure and color of an object in the environment
    """
    def __init__(self, color,
                 reflection_strength=0.2,
                 shadow_strength=0.2,
                 ambient_constant=0.6,
                 diffuse_constant=0.3,
                 specular_constant=0.4,
                 specular_scaling=20):
        super(Material, self).__init__()

        self.color = Color(color[0], color[1], color[2])

        self.reflection_strength = reflection_strength
        self.shadow_strength = shadow_strength
        self.ambient_constant = ambient_constant
        self.diffuse_constant = diffuse_constant
        self.specular_constant = specular_constant
        self.specular_scaling = specular_scaling

    def __repr__(self):
        return 'Material(color=%s)' % (self.color,)

    def base_color_at(self, point):
        """
        Color at a given Point of the Object
        :param point: the Point
        :return: a Color
        """
        return self.color

    def add_shadow(self, color, shadows):
        """
        Adds a Shadow to the given Color.
        :param color: Color to shadow
        :param shadows: number of shadows overlaying at this point
        :return: new shadowed Color
        """
        if shadows <= 0:
            return color
        strength = min(1 - (self.shadow_strength * shadows), 0.9)
        return color * Color(strength, strength, strength)

    def calculate_diffuse(self, color, normal, light_vector):
        """
        Calculates the diffuse coloring
        :param color: color of the light
        :param normal: normal Vector of the hit point
        :param light_vector: Vector facing from the hit point towards the light source
        :return: diffuse Color
        """
        return color * self.diffuse_constant * light_vector.dot(normal)

    def calculate_specular(self, color, ray, normal, light_vector):
        """
        Calculates the specular coloring
        :param color:  color of the light
        :param ray: ray of camera towards hit point
        :param normal: normal Vector of the hit point
        :param light_vector: Vector facing from the hit point towards the light source
        :return: specular Color
        """
        reflected_light_vector = light_vector.mirrored_at(normal).normalized()
        negative_ray_vector = ray.direction.scale(-1)
        return color * self.specular_constant * (
            reflected_light_vector.dot(negative_ray_vector) ** self.specular_scaling)

    def get_color(self, ray, lights, normal, hit_point, ambient_color, shadows):
        """
        Returns the final color of an Material at a given point
        :param ray: a Ray from the Camera towards the hit point
        :param lights: List of all light sources
        :param normal: normal Vector of the hit point
        :param hit_point: Point of collision
        :param ambient_color: overall ambient color of the environment (currently not used)
        :param shadows: Number of overlapping shadows at the hit point
        :return: Color of the Material
        """

        color = self.base_color_at(hit_point)

        # TODO: wikipedia suggests ambient color here?
        ambient_part = color * self.ambient_constant
        diffuse_part = Color(0, 0, 0)
        specular_part = Color(0, 0, 0)

        for light in lights:
            light_vector = (Point(light.origin) - hit_point).normalized()
            diffuse_part += self.calculate_diffuse(light.color, normal, light_vector)

            # angle between light and normal > 90 deg => not facing in same direction => no reflection
            if normal.dot(light_vector) > 0:
                specular_part += self.calculate_specular(light.color, ray, normal, light_vector)

        if shadows > 0:
            color = ambient_part
            color = self.add_shadow(color, shadows)
        else:
            color = ambient_part + diffuse_part + specular_part

        return color

    def get_reflected_color(self, color):
        """
        Adds the reflection strength of the material to the given color
        :param color: color to reflect
        :return: reflected Color
        """
        if self.reflection_strength > 0:
            return color * self.reflection_strength
        return Color(0, 0, 0)
