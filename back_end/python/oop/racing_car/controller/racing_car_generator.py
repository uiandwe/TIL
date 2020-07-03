# -*- coding: utf-8 -*-
from oop.racing_car.domain.engine import Engine
from oop.racing_car.domain.car import Car


class RacingCarGenerator:

    def car_generator(self, names):
        return [Car(name, Engine()) for name in names]

