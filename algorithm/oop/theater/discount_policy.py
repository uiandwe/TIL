from abc import *
class DiscountPolicy(metaclass=ABCMeta):

    def __init__(self, conditions):
        self.conditions = conditions

    def calculate_discount_amount(self, screening):
        for condition in self.conditions:
            if condition.is_satisfied_by(screening):
                return self.get_discount_amount(screening)

    @abstractmethod
    def get_discount_amount(self, screening):
        raise NotImplementedError()


class AmountDiscountPolicy(DiscountPolicy):
    def __init__(self, conditions, discount_amount):
        super().__init__(conditions=conditions)
        self.discount_amount = discount_amount

    def get_discount_amount(self, screening):
        return self.discount_amount


class PercentDiscountPolicy(DiscountPolicy):
    def __init__(self, conditions, percent):
        super().__init__(conditions)
        self.percent = percent

    def get_discount_amount(self, screening):
        return screening.get_movie_fee() * (self.percent / 100)
