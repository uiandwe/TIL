# -*- coding: utf-8 -*-


class Order:
    def __init__(self, food=None, count=1, discount=None):
        self.food = food
        self.count = count
        self.discount = [discount]

    def __repr__(self):
        return "{} : {} / {}".format(self.food, self.count, self.get_price())

    def get_price(self):
        total_discount = 0
        for discount in self.discount:
            if discount:
                total_discount += discount.cal_discount(self.food.price)
        return self.food.price * self.count - total_discount

    def set_discount(self, discount):
        self.discount.append(discount)
