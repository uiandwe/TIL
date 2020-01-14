# -*- coding: utf-8 -*-
class Money:
    VALID_MONEY = 'money의 타입은 int 형 입니다.'

    def __init__(self, money):
        self.valid_money(money)
        self._money = money

    def valid_money(self, money):
        assert type(money) == int, Money.VALID_MONEY

    @property
    def money(self):
        return self._money

    def __str__(self):
        return "{}".format(self.money)

    def __ge__(self, other):
        return self._money >= other._money

    def __sub__(self, other):
        return self._money - other._money
