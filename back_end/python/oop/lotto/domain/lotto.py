# -*- coding: utf-8 -*-


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
        raise NotImplementedError()

    def create_chain_number(self, lotto_machine):
        raise NotImplementedError()

    def create_bonus_number(self, lotto_machine):
        raise NotImplementedError()

    def get_lotto_numbers(self):
        raise NotImplementedError()

    def __str__(self):
        return " ".join([str(number) for number in self.lotto_chain_number])

    def __repr__(self):
        return self.lotto_chain_number

    def get_numbers(self):
        return self.lotto_chain_number

