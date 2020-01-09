# -*- coding: utf-8 -*-
from .number_ import Number_
from .numbers_ import Numbers_


class NumberTable:
    start_table_number = 1
    end_table_number = 10

    def __init__(self, table):
        table = self._trans_int(table)
        self.table = Number_(table)
        self.calculation_func = self._multiply

    def __call__(self, *args, **kwargs):
        return Numbers_([self.calculation_func(self.table, i)
                         for i in range(NumberTable.start_table_number, NumberTable.end_table_number)])

    def _multiply(self, x, y):
        return Number_(x.number * y)

    def _trans_int(self, input_number):
        if type(input_number) is int:
            return input_number
        else:
            try:
                return int(input_number)
            except ValueError as e:
                print(e)
                raise ValueError
            except Exception as e:
                print(e)
                raise Exception
