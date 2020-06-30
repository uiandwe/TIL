# -*- coding: utf-8 -*-
class Input:

    input_money_message = "\n돈 입력,  1000원 단위"
    input_correct_message = "\n지난 주 당첨 번호 입력 6개(,로 구분)"

    def input_money(self):
        print(self.input_money_message)
        try:
            return int(input())
        except Exception as e:
            print(e)
            raise Exception(e)

    def input_correct_number(self):
        print(self.input_correct_message)

        try:
            numbers = input()
            return [int(number) for number in numbers.split(",")]
        except Exception as e:
            print(e)
            raise Exception(e)

