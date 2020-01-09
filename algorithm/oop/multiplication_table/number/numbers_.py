# -*- coding: utf-8 -*-
from .number_ import Number_


class Numbers_:
    def __init__(self, numbers):
        self._valid_numbers(numbers)
        self._numbers = numbers

    def _valid_numbers(self, numbers):
        for number in numbers:
            assert type(number) is Number_

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self._numbers):
            raise StopIteration

        n = self._numbers[self.index]
        self.index += 1
        return n
