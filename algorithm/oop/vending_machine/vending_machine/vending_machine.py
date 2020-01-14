# -*- coding: utf-8 -*-
from oop.vending_machine.singleton import Singleton
from oop.vending_machine.button.button import Button


class VendingMachine(metaclass=Singleton):

    NOT_FOUND_BUTTON = '선택한 버튼을 찾을 수 없습니다.'
    LESS_MONEY = '넣은 돈이 적습니다.'

    def __init__(self):
        self.buttons = []
        self.money = 0

    def connect_buttons(self, products):
        for product in products:
            self.buttons.append(Button(product, len(self.buttons)))

    def select_button(self, button_number):
        button = self.check_button(button_number)
        self.check_payment(button)
        product = button.click_button()
        return product

    def return_product(self, product):
        self.money -= product.price
        return product

    def return_money(self):
        money = self.money
        self.money = 0
        return money

    def check_button(self, button_number):
        for button in self.buttons:
            if button.check_index(button_number):
                return button
        raise AssertionError(VendingMachine.NOT_FOUND_BUTTON)

    def check_payment(self, button):
        product = button.click_button()
        assert self.money >= product.price, VendingMachine.LESS_MONEY

    def payment(self, money):
        self.money = money

    def show_products(self):
        for button in self.buttons:
            print(button)
