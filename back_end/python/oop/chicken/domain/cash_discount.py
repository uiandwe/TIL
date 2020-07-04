# -*- coding: utf-8 -*-
from .discount import Discount


class CashDiscount(Discount):
    def cal_discount(self, price):
        return price * 0.05
