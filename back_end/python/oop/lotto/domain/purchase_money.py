# -*- coding: utf-8 -*-
class PurchaseMoney:

    game_money = 1000
    max_money = 10000
    error_min_money = "최소 금액은 {}원 입니다.".format(game_money)
    error_max_money = "10번 초과는 도박입니다."

    def get_game_count(self, money):

        if money < self.game_money:
            raise Exception(self.error_min_money)

        if money > self.max_money:
            raise Exception(self.error_max_money)

        return int(money / self.game_money)
