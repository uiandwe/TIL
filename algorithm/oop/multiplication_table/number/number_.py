# -*- coding: utf-8 -*-
class Number_:

    def __init__(self, number):
        self._valid_number(number)
        self._number = number

    def _valid_number(self, number):
        assert type(number) is int

    def __str__(self):
        return " {} ".format(self._number)

    @property
    def number(self):
        return self._number

