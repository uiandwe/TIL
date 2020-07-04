# -*- coding: utf-8 -*-


class Menu:

    error_menu_duplication = "같은 메뉴가 등록 되어 있습니다."

    def __init__(self):
        self.menu = []

    def set_menu(self, food):
        for m in self.menu:
            if m.name == food.name:
                raise Exception(self.error_menu_duplication)
        self.menu.append(food)

    def get_display(self):
        return self.menu

    def get_menu(self, idx):
        return self.menu[idx]
