# -*- coding: utf-8 -*-

class Racing:

    def __init__(self, cars, track_count):
        self.cars = cars
        self.index = 0
        self.track_count = track_count

    def next_track(self):
        raise NotImplementedError()

    def get_cars(self):
        return self.cars

    def get_track_count(self):
        return self.track_count

    def track_racing(self):
        raise NotImplementedError()
