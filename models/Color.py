__author__ = 'martinjuhasz'

class Color(object):
    def __init__(self, r, g, b):
        super(Color, self).__init__()

        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return 'Color(r=%s,g=%s,b=%s)' % (self.r, self.g, self.b)

    def __mul__(self, other):
        if isinstance(other, Color):
            r = self.rgb_value(self.r * other.r)
            g = self.rgb_value(self.g * other.g)
            b = self.rgb_value(self.b * other.b)
            return Color(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            r = self.rgb_value(self.r * other)
            g = self.rgb_value(self.g * other)
            b = self.rgb_value(self.b * other)
            return Color(r, g, b)
        else:
            raise NotImplementedError

    def __add__(self, other):
        if isinstance(other, Color):
            r = self.rgb_value(self.r + other.r)
            g = self.rgb_value(self.g + other.g)
            b = self.rgb_value(self.b + other.b)
            return Color(r, g, b)
        elif isinstance(other, int) or isinstance(other, float):
            r = self.rgb_value(self.r + other)
            g = self.rgb_value(self.g + other)
            b = self.rgb_value(self.b + other)
            return Color(r, g, b)
        else:
            raise NotImplementedError

    def get_rgb(self):
        return int(round(self.r)), int(round(self.g)), int(round(self.b))

    @staticmethod
    def rgb_value(value):
        if value >= 255:
            return 255
        elif value <= 0:
            return 0
        else:
            #return int(round(value))
            return value


