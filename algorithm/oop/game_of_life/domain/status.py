# -*- coding: utf-8 -*-
class Status:
    die = 0
    live = 1

    def __init__(self, status=0):
        self.status = status

    def get_status(self):
        return self.status

    def set_status(self, status=0):
        self.status = status

    def __str__(self):
        return "{}".format(self.status)
