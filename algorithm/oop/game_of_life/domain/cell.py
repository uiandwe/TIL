# -*- coding: utf-8 -*-
from oop.game_of_life.domain.status import Status


class Cell:
    live_around_count = 3
    die_around_min = 1
    die_around_max = 4

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return "I am {}".format(self.status)

    def get_status(self):
        return self.status.get_status()

    def update_status(self, count):
        if self.get_status():
            if count <= Cell.die_around_min or count >= Cell.die_around_max:
                self.status = Status(Status.die)
        else:
            if count == Cell.live_around_count:
                self.status = Status(Status.live)
            else:
                self.status = Status(Status.die)
