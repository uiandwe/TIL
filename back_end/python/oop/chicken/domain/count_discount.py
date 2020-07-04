# -*- coding: utf-8 -*-
from .discount import Discount


class CountDiscount(Discount):
    def cal_discount(self, price):
        self.valid_price(price)
        return price * 0.1
