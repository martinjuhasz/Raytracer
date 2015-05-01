import PIL
from PIL.Image import Image
from models.Point import Point
from models.Ray import Ray

__author__ = 'martinjuhasz'


class RayTracer(object):
    """
    RayTracer transforms a given global lightning system into an 2D Image.
    """

    def __init__(self, camera, objects, light, background_color=(0, 0, 0)):
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
        self.image = PIL.Image.new(
            'RGB',
            (self.camera.image_pixel_width, self.camera.image_pixel_height),
            self.background_color)


    def render(self):
        """
        Renders the given Environment into an Image
        :return: Final image
        """

        for x in range(self.camera.image_pixel_width):
            for y in range(self.camera.image_pixel_height):

                # get a ray for each pixel
                ray = self.camera.ray_for_pixel(x, y)
                maxdist = float('inf')
                color = self.background_color

                # if ray hits an object
                for single_object in self.objects:
                    hitdist = single_object.intersection_parameter(ray)
                    if hitdist:
                        if 0 < hitdist < maxdist:

                            # check for shadowing object
                            hit_point = ray.point_at_parameter(hitdist)
                            is_shadowed = self.object_is_shadowed(single_object, hit_point)
                            color = single_object.color_at(ray, is_shadowed)
                            maxdist = hitdist

                self.image.putpixel((x, y), color)

        return self.image

    def object_is_shadowed(self, hit_object, hit_point):
        light_vector = Point(self.light.origin) - hit_point
        light_ray = Ray(hit_point, light_vector)

        for single_object in self.objects:
            if single_object is not hit_object:
                hitdist = single_object.intersection_parameter(light_ray)
                if hitdist and 0 < hitdist:
                        return True

        return False


