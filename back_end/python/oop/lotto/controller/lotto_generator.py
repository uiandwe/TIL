# -*- coding: utf-8 -*-
from oop.lotto.domain.lotto import Lotto
from oop.lotto.domain.lotto_machine import LottoMachine
from oop.lotto.domain.lotto_number import LottoNumber


class LottoGenerator(Lotto):

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
