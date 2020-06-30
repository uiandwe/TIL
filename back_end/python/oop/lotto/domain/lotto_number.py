# -*- coding: utf-8 -*-
class LottoNumber:
    min_number = 1
    max_number = 45
    error_max_number = "최대 숫자는 45."
    error_min_number = "최소 숫자는 1."

    def __init__(self, number):
        self.number = self.valid(number)

    def valid(self, number):
        if number < self.min_number:
            raise ValueError(self.error_min_number)

        if number > self.max_number:
            raise ValueError(self.error_max_number)

        return number

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)

    def __eq__(self, other):
        try:
            return self.number == other.number
        except AttributeError:
            return NotImplemented
