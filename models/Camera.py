import math
from models.Ray import Ray

__author__ = 'martinjuhasz'


class Camera(object):
    def __init__(self, position, up_direction, focus_position, field_of_view, image_width, image_height):
        super(Camera, self).__init__()

        self.e = position  # Point of Camera Postition
        self.up = up_direction  # Vector indicating Cameras up Direction
        self.c = focus_position  # Point of Camera Focus
        self.field_of_view = float(field_of_view)  # Camera Aperture
        self.image_pixel_width = image_width
        self.image_pixel_height = image_height
        self.aspect_ratio = float(self.image_pixel_width) / float(self.image_pixel_height)

        # calculate extrinsic camera parameters
        # this calculates the right-handed coordinate system from our camera
        self.f = (self.c - self.e) / ((self.c - self.e).length())  # Vector from Camera Position towards Camera Focus
        # Right Facing Vector of the Coordinate System
        self.s = (self.f.cross(self.up)) / (self.f.cross(self.up)).length()
        # TODO: propably facing wrong direction?
        self.u = self.s.cross(self.f).scale(-1)  # Up Facing Vector of the coordinate system

        # calculate intrinsic camera parameters
        # defines the 2d mapping range (Sensor)
        alpha = self.field_of_view / 2
        self.height = 2 * math.tan(alpha)
        self.width = self.aspect_ratio * self.height
        self.pixel_width = self.width / (image_width - 1)
        self.pixel_height = self.height / (image_height - 1)

    def __repr__(self):
        return 'Camera(e=%s, up=%s, c=%s, field_of_view=%s, image_width=%s, ' \
               'image_height=%s, ratio=%s, f=%s, s=%s, u=%s, height=%s, width=%s, pixel_width=%s, pixel_height=%s)' \
               % (self.e, self.up, self.c, self.field_of_view, self.image_pixel_width,
                  self.image_pixel_height, self.aspect_ratio, self.f, self.s, self.u,
                  self.height, self.width, self.pixel_width, self.pixel_height)

    def ray_for_pixel(self, x, y):
        # TODO: implement multiple pixels
        xcomp = self.s.scale(x * self.pixel_width - self.width / 2)
        ycomp = self.u.scale(y * self.pixel_height - self.height / 2)
        return Ray(self.e, self.f + xcomp + ycomp)
