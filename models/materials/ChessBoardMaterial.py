from models.Color import Color
from models.Vector import Vector
from models.materials.Material import Material

__author__ = 'martinjuhasz'


class ChessBoardMaterial(Material):
    def __init__(self, color, second_color, reflection_strength=0.3, shadow_strength=0.7,
                 ambient_constant=0.5, diffuse_constant=0.3, specular_constant=0.4, specular_scaling=20):

        super(ChessBoardMaterial, self).__init__(color, reflection_strength, shadow_strength, ambient_constant,
                                                 diffuse_constant, specular_constant, specular_scaling)

        self.second_color = Color(second_color[0], second_color[1], second_color[2])
        self.check_size = 1

    def base_color_at(self, point):
        v = Vector([point[0], point[1], point[2]])
        v.scale(1.0 / self.check_size)
        if (int(abs(v[0]) + 0.5) + int(abs(v[1]) + 0.5) + int(abs(v[2]) + 0.5)) % 2:
            return self.second_color
        return self.color