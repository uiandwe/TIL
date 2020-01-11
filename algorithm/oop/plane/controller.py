# -*- coding: utf-8 -*-
from oop.plane.plane import Plane
from oop.plane.turbo_plane import TurboPlane

if __name__ == '__main__':
    plane = Plane()
    plane.fly()

    turbo_plane = TurboPlane()
    turbo_plane.fly()
    turbo_plane.boost()
    turbo_plane.start_stealth()
    turbo_plane.stop_stealth()
