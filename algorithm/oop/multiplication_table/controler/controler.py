# -*- coding: utf-8 -*-
from oop.multiplication_table.number.number_table import NumberTable


class MultiplicationTable:

    def __call__(self, *args, **kwargs):
        while True:
            print("\ninput number: ")
            try:
                user_input_number = input()
                number_table = NumberTable(user_input_number)()
                self.print_number_table(number_table)

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(e)

    def print_number_table(self, number_table):
        for number in number_table:
            print(number, end=' ')
