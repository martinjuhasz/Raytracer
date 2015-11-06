from controller.RayTracer import RayTracer
from models.Camera import Camera
from models.Color import Color
from models.LightSource import LightSource
from models.materials.ChessBoardMaterial import ChessBoardMaterial
from models.materials.Material import Material
from models.objects.Plane import Plane
from models.Point import Point
from models.objects.Sphere import Sphere
from models.objects.Triangle import Triangle
from models.Vector import Vector
import sys

__author__ = 'martinjuhasz'


def print_status(percentage):
    sys.stdout.write('\r')
    sys.stdout.write("[%-50s] %d %%" % ('=' * (percentage/2), percentage))
    sys.stdout.flush()


if __name__ == "__main__":

    # general parameters
    image_width = 300
    image_height = 300
    field_of_view = 45

    reflection_recursion_level = 2
    antialiasing = 1  # 1= off, 4, 16

    # camera setup
    camera_postition = Point([0, 1.8, 10])
    camera_up_direction = Vector([0, 1, 0])
    camera_focus = Point([0, 3, 0])
    camera = Camera(camera_postition, camera_up_direction, camera_focus, field_of_view, image_width, image_height)

    # setup objects
    objects = [
        Sphere(Material((0, 255, 0)), 1.2, Point([-1.5, 2.5, -2])),
        Sphere(Material((255, 0, 0)), 1.2, Point([1.5, 2.5, -2])),
        Sphere(Material((0, 0, 255)), 1.2, Point([0, 5.5, -2])),
        Plane(ChessBoardMaterial((255, 255, 255), (0, 0, 0), reflection_strength=0), Vector([0, -1, 0]), Point([0, -1, 0])),
        Triangle(Material((255, 255, 0), reflection_strength=0), Point([-1.5, 2.5, -2.2]), Point([1.5, 2.5, -2.2]), Point([0, 5.5, -2.2]))
    ]

    # lights
    lights = [
        LightSource([30, 30, 10], Color(255, 255, 255)),
        # LightSource([-10, 100, 30], Color(255, 255, 255))
    ]

    # render image
    raytracer = RayTracer(camera, objects, lights, recursion_level=reflection_recursion_level, antialiasing=antialiasing, status_callback=print_status)

    print
    print "Starting Raytracing..."
    print
    print "Configuration:"
    print camera
    print raytracer
    print "Objects: %s" % (objects,)
    print "Lights: %s" % (lights,)
    print
    print "Status:"

    image = raytracer.render()
    image.show()
    # image.save("output/export.png", "PNG")