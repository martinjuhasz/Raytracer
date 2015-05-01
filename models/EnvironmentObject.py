__author__ = 'martinjuhasz'


class EnvironmentObject(object):
    SHADOW_STRENGTH = 0.7

    def intersection_parameter(self, ray):
        return None

    @staticmethod
    def add_shadow(color):
        return int(round(color[0] * EnvironmentObject.SHADOW_STRENGTH)), int(
            round(color[1] * EnvironmentObject.SHADOW_STRENGTH)), int(
            round(color[2] * EnvironmentObject.SHADOW_STRENGTH))

    def color_at(self, ray, is_shadowed=False):
        return 0, 0, 0