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


if __name__ == '__main__':
    from algorithm.oop.theater.discount_condition import SequenceCondition
    from algorithm.oop.theater.screening import Screening
    from algorithm.oop.theater.movie import Movie

    m1 = Movie("english", 10, 1000)
    m2 = Movie("ko", 20, 2000)

    screening1 = Screening(m1, 1)
    screening3 = Screening(m2, 3)

    sc1 = SequenceCondition(1)
    sc2 = SequenceCondition(2)
    sc3 = SequenceCondition(3)
    sc4 = SequenceCondition(4)

    adp = AmountDiscountPolicy([sc1, sc2, sc3, sc4], 100)
    assert adp.calculate_discount_amount(screening1) == 100
    pdp = PercentDiscountPolicy([sc1, sc2, sc3, sc4], 50)
    assert pdp.calculate_discount_amount(screening1) == 500

    adp = AmountDiscountPolicy([sc1, sc2, sc3, sc4], 100)
    assert adp.calculate_discount_amount(screening3) == 100
    pdp = PercentDiscountPolicy([sc1, sc2, sc3, sc4], 50)
    assert pdp.calculate_discount_amount(screening3) == 1000



