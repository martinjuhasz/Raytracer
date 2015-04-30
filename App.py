from controller.RayTracer import RayTracer
from models.Camera import Camera
from models.Plane import Plane
from models.Point import Point
from models.Sphere import Sphere
from models.Vector import Vector

__author__ = 'martinjuhasz'


if __name__ == "__main__":

    # general parameters
    image_width = 400
    image_height = 400
    field_of_view = 45

    # setup camera
    camera_postition = Point([0, 1.8, 10])
    camera_up_direction = Vector([0, 1, 0])
    camera_focus = Point([0, 3, 0])
    camera = Camera(camera_postition, camera_up_direction, camera_focus, field_of_view, image_width, image_height)

    # setup objects
    objects = [
        Sphere(Point([0, 3, 0]), 2),
        Plane(Point([0, 0, 0]), Vector([0, 1, 0]))
    ]

    # render image
    raytracer = RayTracer(camera, objects)
    image = raytracer.render()
    image.show()