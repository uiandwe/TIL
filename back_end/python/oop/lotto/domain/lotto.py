# -*- coding: utf-8 -*-
from .lotto_machine import LottoMachine
from .lotto_number import LottoNumber


class Lotto:
    chain_number = 6
    bonus_number = 1
    error_max_chain_number = "6개"
    error_bonus_number = "1개"

    def __init__(self):
        self.lotto_numbers = []
        self.lotto_chain_number = []
        self.lotto_bonus_number = None

    def create_numbers(self, lotto_machine):
        return lotto_machine.create_numbers(LottoNumber.max_number)

    def create_chain_number(self, lotto_machine):
        return lotto_machine.create_chain_numbers(self.chain_number, self.lotto_numbers)

    def create_bonus_number(self, lotto_machine):
        return lotto_machine.create_bonus_numbers(self.chain_number, self.bonus_number, self.lotto_numbers)

    def get_lotto_numbers(self):
        self.lotto_numbers = self.create_numbers(LottoMachine())
        self.lotto_chain_number = self.create_chain_number(LottoMachine())
        self.lotto_bonus_number = self.create_bonus_number(LottoMachine())

    def __str__(self):
        return " ".join([str(number) for number in self.lotto_chain_number])

    def __repr__(self):
        return self.lotto_chain_number

    def get_numbers(self):
        return self.lotto_chain_number

