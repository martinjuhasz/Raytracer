__author__ = 'martinjuhasz'


class LightSource(object):

    def __init__(self, origin, color):
        super(LightSource, self).__init__()

        self.origin = origin
        self.color = color

    def __repr__(self):
        return 'LightSource(origin=%s, color=%s)' % (self.origin, self.color)