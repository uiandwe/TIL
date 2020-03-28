if __name__ == '__main__':
    from algorithm.oop.theater.discount_condition import SequenceCondition
    from algorithm.oop.theater.screening import Screening
    from algorithm.oop.theater.movie import Movie
    from algorithm.oop.theater.discount_policy import AmountDiscountPolicy, PercentDiscountPolicy

    sc1 = SequenceCondition(1)
    sc2 = SequenceCondition(2)
    sc3 = SequenceCondition(3)
    sc4 = SequenceCondition(4)

    adp = AmountDiscountPolicy([sc1, sc2, sc3, sc4], 100)
    m1 = Movie("english", 10, 1000, adp)
    screening1 = Screening(m1, 1)
    assert m1.calculate_movie_fee(screening1) == 900

    pdp = PercentDiscountPolicy([sc1, sc2, sc3, sc4], 50)
    m2 = Movie("ko", 20, 2000, pdp)
    screening3 = Screening(m2, 3)
    assert m2.calculate_movie_fee(screening3) == 1000
