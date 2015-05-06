from models.objects.EnvironmentObject import EnvironmentObject

__author__ = 'martinjuhasz'

class Plane(EnvironmentObject):
    def __init__(self, material, normal, center):
        super(Plane, self).__init__(material)

        self.center = center
        self.normal = normal

    def __repr__(self):
        return 'Plane(material=%s, center=%s, normal=%s)' \
               % (self.material, self.center, self.normal)

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

    def normal_at(self, point):
        return self.normal