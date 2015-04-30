import PIL
from PIL.Image import Image

__author__ = 'martinjuhasz'


class RayTracer(object):
    """
    RayTracer transforms a given global lightning system into an 2D Image.
    """

    def __init__(self, camera, objects, background_color=(0, 0, 0)):
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

                ray = self.camera.ray_for_pixel(x, y)
                maxdist = float('inf')
                color = self.background_color

                for single_object in self.objects:
                    hitdist = single_object.intersection_parameter(ray)
                    if hitdist:
                        if 0 < hitdist < maxdist:
                            maxdist = hitdist
                            color = single_object.color_at(ray)
                self.image.putpixel((x, y), color)

        return self.image


