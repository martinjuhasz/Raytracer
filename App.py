from controller.RayTracer import RayTracer
from models.Camera import Camera
from models.ChessBoardMaterial import ChessBoardMaterial
from models.LightSource import LightSource
from models.Material import Material
from models.Plane import Plane
from models.Point import Point
from models.Sphere import Sphere
from models.Triangle import Triangle
from models.Vector import Vector

__author__ = 'martinjuhasz'


if __name__ == "__main__":

    # general parameters
    image_width = 300
    image_height = 300
    field_of_view = 45

    # camera setup
    camera_postition = Point([0, 1.8, 10])
    camera_up_direction = Vector([0, 1, 0])
    camera_focus = Point([0, 3, 0])
    camera = Camera(camera_postition, camera_up_direction, camera_focus, field_of_view, image_width, image_height)

    # setup objects
    objects = [
        Sphere(Material((255, 0, 0)), 1.2, Point([-1.5, 2.5, -2])),
        Sphere(Material((0, 255, 0)), 1.2, Point([1.5, 2.5, -2])),
        Sphere(Material((0, 0, 255)), 1.2, Point([0, 5.5, -2])),
        Plane(ChessBoardMaterial((255, 255, 255), (50, 50, 50), reflection_strength=0), Vector([0, 1, 0]), Point([0, -1, 0])),
        Triangle(Material((255, 0, 255), reflection_strength=0), Point([-1.5, 2.5, -4]), Point([1.5, 2.5, -4]), Point([0, 5.5, -4]))
    ]

    # lights
    lights = [
        LightSource([30, 30, 10], (255, 255, 255)),
        LightSource([-10, 100, 30], (255, 255, 255))
    ]

    # render image
    raytracer = RayTracer(camera, objects, lights)
    image = raytracer.render()
    image.show()