# -*- coding: utf-8 -*-


class Discount:
    def __init__(self):
        self.discount_amount = 0

    def cal_discount(self, price):
        raise NotImplementedError

    def valid_price(self, price):
        try:
            int(price)
            return True
        except ValueError as e:
            raise ValueError(e)
