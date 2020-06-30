# -*- coding: utf-8 -*-
class Output:
    prize_message = "\n 이번 로또 상금은 총 {}원 입니다."

    def prize_output(self, prizes):
        total_prize_money = 0
        for prize in prizes:
            print("등수 : {}  / 상금 : {}".format(prize[0], prize[1]))
            total_prize_money += prize[1]

        print(self.prize_message.format(total_prize_money))

    def buy_lotto_numbers(self, lottos):
        print("=====================")
        for lotto in lottos:
            print(lotto)
        print("=====================")
