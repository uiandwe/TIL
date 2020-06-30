# -*- coding: utf-8 -*-
import random
from .lotto_number import LottoNumber


class LottoMachine:

    def create_numbers(self, count):
        return [LottoNumber(i) for i in range(1, count+1)]

    def create_chain_numbers(self, count, numbers):
        random.shuffle(numbers)
        return numbers[:count]

    def create_bonus_numbers(self, chain_number, bonus_number, numbers):
        return numbers[chain_number+bonus_number]
