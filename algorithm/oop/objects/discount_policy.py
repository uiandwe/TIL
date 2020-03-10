# -*- coding: utf-8 -*-
import abc

class DiscountPolicy:
    __metaclass__ = abc.ABCMeta

    def __init__(self, conditions):
        self.conditions = conditions

    def calculate_discount_amount(self, screening):
        for each in self.conditions:
            if each.isSatisfiedBy(screening):
                return self.get_discount_amount(screening)

    @abc.abstractmethod
    def get_discount_amount(self, screening):
        raise NotImplementedError()
