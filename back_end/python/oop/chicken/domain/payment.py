# -*- coding: utf-8 -*-


class Payment:

    def __init__(self, orders=None):
        self.orders = orders
        self.total_amount = 0

    def cal_total_amount(self):
        for order in self.orders:
            self.total_amount += order.get_price()

    def get_display(self):
        return self.orders

    def set_orders(self, orders):
        self.orders = orders

    def get_total_amount(self):
        return self.total_amount
