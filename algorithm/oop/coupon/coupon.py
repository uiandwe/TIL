# -*- coding: utf-8 -*-
class Coupon:
    def __init__(self, discount_amount):
        self._discount_amount = discount_amount

    @property
    def discount_amount(self):
        return self._discount_amount

    def calculate_discounted_price(self, product):
        if product.price < self._discount_amount:
            return 0
        return product.price - self._discount_amount
