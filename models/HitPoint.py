__author__ = 'martinjuhasz'


class HitPoint(object):

    def __init__(self, ray, item, point, distance, shadows):
        super(HitPoint, self).__init__()

        self.ray = ray
        self.item = item
        self.point = point
        self.distance = distance
        self.shadows = shadows