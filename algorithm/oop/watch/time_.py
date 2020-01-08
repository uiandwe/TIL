# -*- coding: utf-8 -*-
class Time_:

    def __init__(self, t):
        self.t = t

    def get_milli_time(self):
        return self.t / 1000000

    def get_nano_time(self):
        return self.t

    def get_second_time(self):
        return self.t / 1000000000
