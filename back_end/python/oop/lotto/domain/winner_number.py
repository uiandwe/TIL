# -*- coding: utf-8 -*-
from .lotto_number import LottoNumber


class WinnerNumber:
    chain_number = 6
    error_max_chain_number = "6개"

    prize_money = [77777, 7777, 777]
    prize_number_count = [6, 5, 4]
    prize_grade = [1, 2, 3]

    def __init__(self):
        self.winner_numbers = []
        self.prize = {}

        self.set_winner_number_count_by_prize()

    def set_winner_numbers(self, numbers):
        if len(numbers) != self.chain_number:
            raise Exception(self.error_max_chain_number)
        self.winner_numbers = [LottoNumber(number) for number in numbers]

    def set_winner_number_count_by_prize(self):
        for idx, number in enumerate(self.prize_number_count):
            self.prize[number] = {"money": self.prize_money[idx], "grade": self.prize_grade[idx]}

    def compare_winner_number(self, numbers):
        prize = []
        for lotto in numbers:
            prize_count = 0
            for winner_number in self.winner_numbers:
                if winner_number in lotto.get_numbers():
                    prize_count += 1
            if prize_count in self.prize.keys():
                prize.append((self.prize[prize_count]['grade'], self.prize[prize_count]['money']))
            else:
                prize.append((0, 0))

        return prize

