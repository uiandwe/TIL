# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import random

class AbstractSubject(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def sort(self, reverse=False):
        pass



class RealSubject(AbstractSubject):
    def __init__(self):
        self.digits = []

        for i in range(10000):
            self.digits.append(random.random())


    def sort(self, reverse=False):
        self.digits.sort()

        if reverse:
            self.digits.reverse()

class Proxy(AbstractSubject):
    reference_count = 0

    def __init__(self):
        if not getattr(self.__class__, 'cached_object', None):
            self.__class__.cached_object = RealSubject()
            print('created new obj')
        else:
            print('using cached obj')

        self.__class__.reference_count += 1

        print("count of references = ", self.__class__.reference_count)

    def sort(self, reverse=False):
        print('called sort method ')
        print(locals().items())

        self.__class__.cached_object.sort(reverse=reverse)

    def __del__(self):
        self.__class__.reference_count -= 1

        if self.__class__.reference_count == 0:
            print('referenct_count is 0, delteing cached')
            del self.__class__.cached_object

        print('count of object = ', self.__class__.reference_count)


if __name__ == '__main__':
    proxy1 = Proxy()

    proxy2 = Proxy()

    proxy3 = Proxy()

    proxy1.sort(reverse=True)




