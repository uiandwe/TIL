# -*- coding: utf-8 -*-
from chicken.domain.menu import Menu
from chicken.domain.chicken import Chicken


class MenuGenerator(Menu):
    def menu_generator(self):
        self.set_menu(Chicken("뿌링클", 18000))
        self.set_menu(Chicken("맛초킹", 17000))
        self.set_menu(Chicken("고추바사삭", 16000))
        self.set_menu(Chicken("볼케이노", 17000))
        self.set_menu(Chicken("허니콤보", 18000))
        self.set_menu(Chicken("갈릭", 17000))
        self.set_menu(Chicken("양념", 18000))
        self.set_menu(Chicken("안심후라이드", 16000))




