# -*- coding: utf-8 -*-
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
