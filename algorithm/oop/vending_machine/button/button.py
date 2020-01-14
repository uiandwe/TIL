# -*- coding: utf-8 -*-
from oop.vending_machine.product.product import Product


class Button:
    VALID_PRODUCT = '상품만 넣을 수 있습니다.'

    def __init__(self, product, index):
        self.valid_product(product)
        self._product = product
        self._index = index

    def valid_product(self, product):
        assert isinstance(product, Product), Button.VALID_PRODUCT

    def click_button(self):
        return self._product

    @property
    def index(self):
        return self._index

    def __str__(self):
        return "{}. {}".format(self._index, self._product)

    def check_index(self, index):
        return self._index == index
