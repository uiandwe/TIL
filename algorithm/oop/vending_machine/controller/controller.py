# -*- coding: utf-8 -*-
from oop.vending_machine.vending_machine.vending_machine import VendingMachine
from oop.vending_machine.product.can import Can
from oop.vending_machine.product.cookie import Cookie
from oop.vending_machine.money.money import Money


class Controller:
    VALID_MONEY = 'money는 int형 입니다.'

    def __init__(self):
        self.vm = VendingMachine()

    def __call__(self, *args, **kwargs):
        return

    def make_products(self):
        can = Can("환타", Money(1000))
        cookie = Cookie("막화롱", Money(3000))

        return self.vm.connect_buttons([can, cookie])

    def show_products(self):
        return self.vm.show_products()

    def insert_money(self, money):
        assert type(money) == int, Controller.VALID_MONEY
        m = Money(money)
        self.vm.payment(m)
        print("{}을 넣엇습니다.".format(m))

    def select_product(self, button_number):
        product = self.vm.select_button(button_number)
        return self.vm.return_product(product)

    def return_money(self):
        return self.vm.return_money()
