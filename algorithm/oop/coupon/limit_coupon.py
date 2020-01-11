# -*- coding: utf-8 -*-
from oop.coupon.coupon import Coupon


class LimitCoupon(Coupon):
    def __init__(self, limit_price, discount_amount):
        super().__init__(discount_amount)
        self._limit_price = limit_price

    @property
    def limit_price(self):
        return self._limit_price

    def calculate_discounted_price(self, product):
        if product.price < self._limit_price:
            return product.price
        return super().calculate_discounted_price(product)
