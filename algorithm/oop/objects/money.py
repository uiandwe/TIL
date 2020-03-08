# -*- coding: utf-8 -*-
class Money:

    def __init__(self, amount=0):
        self.amount = amount

    @staticmethod
    def wons(amount):
        return Money(amount)
