# -*- coding: utf-8 -*-
class Output:

    def menu(self, menu):
        print("=====================")
        print("메뉴 리스트")
        for idx, food in enumerate(menu):
            print("{}. {} : {}".format(idx, food.name, food.price))

        print("=====================")

    def payment(self, orders, total_payment):
        print("=====================")
        for order in orders:
            print(order)

        print("결제 총 금액 {}".format(total_payment))
        print("=====================")
