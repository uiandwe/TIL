# -*- coding: utf-8 -*-
from oop.vending_machine.product.product import Product


class Can(Product):
    def __init__(self, name, price):
        super().__init__(name, price)
