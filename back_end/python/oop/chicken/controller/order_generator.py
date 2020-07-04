# -*- coding: utf-8 -*-
from chicken.domain.order import Order


class OrderGenerator:
    def __init__(self):
        self.orders = []

    def set_order(self, food, count):
        self.orders.append(Order(food, count))

    def get_orders(self):
        return self.orders

    def clear_order(self):
        self.orders = []
