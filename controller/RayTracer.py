import PIL
from PIL.Image import Image
from models.Color import Color
from models.HitPoint import HitPoint
from models.Point import Point
from models.Ray import Ray

__author__ = 'martinjuhasz'


class RayTracer(object):
    """
    RayTracer transforms a given global lightning system into an 2D Image.
    """

    def __init__(self, camera, objects, light, background_color=Color(0, 0, 0), ambient_color=Color(255, 255, 255),
                 recursion_level=4):
        """
        Default initializer
        :param camera:  The Camera Object from where the system should be rendered
        :param objects: the List of objects in the  system
        :param background_color: color of the images background
        :return: new Class Object
        """
        super(RayTracer, self).__init__()

        self.camera = camera
        self.objects = objects
        self.light = light
        self.background_color = background_color
        self.ambient_color = ambient_color
        self.recursion_level = recursion_level
        self.image = PIL.Image.new(
            'RGB',
            (self.camera.image_pixel_width, self.camera.image_pixel_height),
            (self.background_color.r, self.background_color.g, self.background_color.b))


    def render(self):
        """
        Renders the given Environment into an Image
        :return: Final image
        """
        for x in range(self.camera.image_pixel_width):
            for y in range(self.camera.image_pixel_height):

                # get a ray for each pixel
                ray = self.camera.ray_for_pixel(x, y)
                color = self.trace_ray(0, ray)
                self.image.putpixel((x, y), (color.r, color.g, color.b))

        return self.image

    def trace_ray(self, level, ray):
        hit_point = self.intersect(level, ray)
        if hit_point:
            return self.shade(level, hit_point)
        return self.background_color

    def shade(self, level, hit_point):
        direct_color = hit_point.item.color_at(hit_point.ray, self.light, hit_point.point, self.ambient_color, hit_point.shadowed)

        reflected_ray_vector = hit_point.ray.direction.mirrored_at(hit_point.item.normal_at(hit_point.point))
        reflected_ray = Ray(hit_point.point, reflected_ray_vector)
        reflected_color = hit_point.item.get_reflected_color(self.trace_ray(level + 1, reflected_ray))

        return direct_color + reflected_color

    def intersect(self, level, ray):
        """
        Intersects the given Ray with all objects of the environment
        :param level: current recursion depth
        :param ray: the ray to check hits against
        :return: HitPoint Object or None
        """

        if level >= self.recursion_level:
            return None

        # if ray hits an object
        hit_point = None
        hit_object = None
        maxdist = float('inf')

        for single_object in self.objects:
            hitdist = single_object.intersection_parameter(ray)
            if hitdist:
                if 0 < hitdist < maxdist:
                    hit_point = ray.point_at_parameter(hitdist)
                    hit_object = single_object
                    maxdist = hitdist

        if not hit_object:
            return None

        is_shadowed = self.object_is_shadowed(ray, maxdist)
        return HitPoint(ray, hit_object, hit_point, maxdist, is_shadowed)

    def object_is_shadowed(self, ray, distance):
        """
        Checks if a point (ray at distance) is shadowed by another object
        :param ray: the ray
        :param distance: the distance of the point
        :return: True or False
        """
        # Fixing shadow rounding errors
        # see S.14: http://www.cs.cornell.edu/courses/cs4620/2011fa/lectures/08raytracingWeb.pdf
        hit_point = ray.point_at_parameter(distance - 0.00000001)
        light_vector = Point(self.light.origin) - hit_point
        light_ray = Ray(hit_point, light_vector)

        for single_object in self.objects:
            hitdist = single_object.intersection_parameter(light_ray)
            if hitdist and 0 < hitdist:
                    return True

        return False


