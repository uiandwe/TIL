# -*- coding: utf-8 -*-


class Chicken:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return "{} {}".format(self.name, self.price)
