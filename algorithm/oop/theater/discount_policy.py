class DiscountPolicy:

    def __init__(self, conditions):
        self.conditions = conditions

    def calculate_discount_amount(self, screening):
        for condition in self.conditions:
            if condition.is_satisfied_by(screening):
                print(screening)


if __name__ == '__main__':
    from algorithm.oop.theater.discount_condition import SequenceCondition
    from algorithm.oop.theater.screening import Screening

    screening = Screening(1)

    sc1 = SequenceCondition(1)
    sc2 = SequenceCondition(2)
    sc3 = SequenceCondition(3)
    sc4 = SequenceCondition(4)

    dp = DiscountPolicy([sc1, sc2, sc3, sc4])

    dp.calculate_discount_amount(screening)

