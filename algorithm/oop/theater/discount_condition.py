from abc import *


class DiscountCondition(metaclass=ABCMeta):
    @abstractmethod
    def is_satisfied_by(self, screening):
        raise NotImplementedError()


class SequenceCondition(DiscountCondition):

    def __init__(self, sequence):
        self.sequence = sequence

    def is_satisfied_by(self, screening):
        return screening.is_sequence(self.sequence)



if __name__ == '__main__':
    from algorithm.oop.theater.screening import Screening

    screening = Screening(1)
    sc = SequenceCondition(2)
    assert sc.is_satisfied_by(screening), "not equal screening number"