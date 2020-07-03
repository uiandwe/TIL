# -*- coding: utf-8 -*-
from oop.racing_car.domain.racing import Racing


class RacingGenerator(Racing):
    def next_track(self):
        for car in self.cars:
            car.distance += car.engine.run()

    def track_racing(self):
        self.index += 1
        if self.index <= self.track_count:
            return True
        return False
