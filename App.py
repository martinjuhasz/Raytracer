from controller.RayTracer import RayTracer
from models.Camera import Camera
from models.LightSource import LightSource
from models.Plane import Plane
from models.Point import Point
from models.Sphere import Sphere
from models.Triangle import Triangle
from models.Vector import Vector

__author__ = 'martinjuhasz'


if __name__ == "__main__":

    # general parameters
    image_width = 200
    image_height = 200
    field_of_view = 45

    # camera setup
    camera_postition = Point([0, 1.8, 2])
    camera_up_direction = Vector([0, 1, 0])
    camera_focus = Point([0, 1, 8])
    camera = Camera(camera_postition, camera_up_direction, camera_focus, field_of_view, image_width, image_height)

    # setup objects
    objects = [
        Sphere(Point([-2.5, 1, 17]), 1.9),
        Sphere(Point([2.5, 1, 17]), 1.9),
        Sphere(Point([0, -3.0, 17]), 1.9),
        Plane(Point([0, 3.5, 0]), Vector([0, -1, 0])),
        Triangle(Point([2.5, 1, 17]), Point([0, -3.0, 17]), Point([-2.5, 1, 17]))
    ]

    # lights
    light = LightSource([-10, -12, 4], (255, 255, 255))

    # render image
    raytracer = RayTracer(camera, objects, light)
    image = raytracer.render()
    image.show()