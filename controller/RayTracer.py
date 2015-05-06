import PIL
from PIL.Image import Image
from models.Color import Color
from models.HitPoint import HitPoint
from models.Point import Point
from models.Ray import Ray
import math
__author__ = 'martinjuhasz'


class RayTracer(object):
    """
    RayTracer transforms a given global lightning system into an 2D Image.
    """

    def __init__(self, camera, objects, lights, background_color=Color(0, 0, 0), ambient_color=Color(255, 255, 255),
                 recursion_level=2, antialiasing=1, status_callback=None):
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
        self.lights = lights
        self.background_color = background_color
        self.ambient_color = ambient_color
        self.recursion_level = recursion_level

        if antialiasing not in [1, 4, 16]:
            raise NotImplementedError

        self.antialiasing = int(math.sqrt(antialiasing))
        self.status_callback = status_callback
        self.current_status = -1
        self.image = PIL.Image.new(
            'RGB',
            (self.camera.image_pixel_width, self.camera.image_pixel_height),
            (self.background_color.r, self.background_color.g, self.background_color.b))

    def __repr__(self):
        return 'RayTracer(background_color=%s, ambient_color=%s, recursion_level=%s, antialiasing=%s)' % (self.background_color, self.ambient_color, self.recursion_level, self.antialiasing)

    def render(self):
        """
        Renders the given Environment into an Image
        :return: Final image
        """
        for x in range(self.camera.image_pixel_width):
            for y in range(self.camera.image_pixel_height):

                if self.status_callback:
                    percentage = int((x * y) / float(self.camera.image_pixel_width * self.camera.image_pixel_height) * 100)
                    if percentage > self.current_status:
                        self.current_status = percentage
                        self.status_callback(percentage)

                # get a ray for each part of the pixel
                raypoint_gap = 1.0/self.antialiasing
                raypoints_to_check = [(x + (pixel_part_x * raypoint_gap), y + (pixel_part_y * raypoint_gap)) for pixel_part_y in range(0, self.antialiasing) for pixel_part_x in range(0, self.antialiasing)]

                pixel_color = Color(0, 0, 0)
                color_weight = 1.0 / (self.antialiasing ** 2)

                for point in raypoints_to_check:
                    ray = self.camera.ray_for_pixel(point[0], point[1])
                    pixel_color += self.trace_ray(0, ray) * color_weight

                self.image.putpixel((x, y), pixel_color.get_rgb())

        return self.image

    def trace_ray(self, level, ray):
        """
        Starts the (propbably recursive) tracing of the given ray to get its final color
        :param level: current recursion level depth (number of reflections to follow)
        :param ray: the ray that should be followed
        :return: final Color
        """
        hit_point = self.intersect(level, ray)
        if hit_point:
            return self.shade(level, hit_point)
        return self.background_color

    def shade(self, level, hit_point):
        """
        Calculates the color at hit_point including the reflected part
        :param level: current recursion level depth (number of reflections to follow)
        :param hit_point: HitPoint object of ray collision
        :return: shaded Color
        """
        direct_color = hit_point.item.color_at(hit_point.ray, self.lights, hit_point.point, self.ambient_color, hit_point.shadows)

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

        shadows = self.shadows_at_point(ray, maxdist)
        return HitPoint(ray, hit_object, hit_point, maxdist, shadows)

    def shadows_at_point(self, ray, distance):
        """
        Checks if a point (ray at distance) is shadowed by another object
        :param ray: the ray
        :param distance: the distance of the point
        :return: Number of Shadows overlapping
        """
        # Fixing shadow rounding errors
        # see S.14: http://www.cs.cornell.edu/courses/cs4620/2011fa/lectures/08raytracingWeb.pdf
        hit_point = ray.point_at_parameter(distance - 0.00000001)
        count = 0
        for light in self.lights:
            light_vector = Point(light.origin) - hit_point
            light_ray = Ray(hit_point, light_vector)

            for single_object in self.objects:
                hitdist = single_object.intersection_parameter(light_ray)
                if hitdist and 0 < hitdist:
                        count += 1
                        break

        return count


