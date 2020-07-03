# -*- coding: utf-8 -*-
from .racing_car_generator import RacingCarGenerator
from .racing_generator import RacingGenerator
from oop.racing_car.view.input import Input
from oop.racing_car.view.output import Output
from oop.racing_car.domain.winner import Winner
import time


class RacingCarController:
    def __call__(self, *args, **kwargs):
        print("init cars")

        ip = Input()
        names = ip.input_car_names()

        rcg = RacingCarGenerator()
        cars = rcg.car_generator(names)

        track_count = ip.input_track_count()

        op = Output()
        rg = RacingGenerator(cars, track_count)
        while rg.track_racing():
            rg.next_track()
            op.racing_grade(rg.get_cars())
            time.sleep(0.5)

        w = Winner()
        op.winner_announce(w.final_medal(rg.get_cars()))
