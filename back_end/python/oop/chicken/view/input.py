# -*- coding: utf-8 -*-


class Input:

    def input_money(self):
        print(self.input_money_message)
        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)

    def user_select(self, user_select_menu):
        print("=====================")
        for menu in user_select_menu:
            print(menu)

        print("번호를 선택해 주세요")

        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)

    def menu_select(self):
        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)
        print("=====================")

    def menu_count(self):
        print("수량을 선택해 주세요.")
        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)
        print("=====================")

    def payment_select(self):
        print("1. 카드  / 2. 현금")
        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)
        print("=====================")
