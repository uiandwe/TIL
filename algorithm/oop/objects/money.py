# -*- coding: utf-8 -*-
class Money:

    def __init__(self, amount=0):
        self.amount = amount

    @staticmethod
    def wons(amount):
        return Money(amount)

    def plus(self, amount):
        return Money(self.amount + amount.amount)

    def minus(self, amount):
        return Money(self.amount - amount.amount)

    def times(self, percent):
        return Money(self.amount * percent)

    def is_less_than(self, other):
        return self.amount - other.amount < 0

    def is_greather_than_or_equal(self, other):
        return self.amount - other.amount >= 0
