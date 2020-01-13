# -*- coding: utf-8 -*-
from oop.vending_machine.contoller.controller import Controller

if __name__ == '__main__':
    controller = Controller()
    controller.make_products()
    controller.show_products()
    controller.insert_money(2000)
    controller.select_product(0)
