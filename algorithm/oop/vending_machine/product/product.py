# -*- coding: utf-8 -*-
from oop.vending_machine.money.money import Money

class Product:
    VALID_NAME = 'name은 str형 입니다.'
    VALID_PRICE = 'price는 Money형 입니다.'

    def __init__(self, name, price):
        self.valid_name(name)
        self.valid_price(price)

        self._name = name
        self._price = price

    def valid_name(self, name):
        assert type(name) == str, Product.VALID_NAME

    def valid_price(self, price):
        assert isinstance(price, Money), Product.VALID_PRICE

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    def __str__(self):
        return "{} {}".format(self._name, self._price)
