# -*- coding: utf-8 -*-
from oop.plane.turbo_imp import TurboImp
from oop.plane.stealth_imp import StealthImp
from oop.plane.plane import Plane


class TurboPlane(Plane, TurboImp, StealthImp):

    def boost(self):
        print("가속")

    def start_stealth(self):
        print("안보임")

    def stop_stealth(self):
        print("보임")

    def fly(self):
        print("터보 날다")
