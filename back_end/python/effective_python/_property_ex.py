# -*- coding: utf-8 -*-
class Test:
    def __init__(self):
        self.__tlqkf = 'red'

    @property
    def color(self):
        return self.__tlqkf

    @color.setter
    def color(self, clr):
        self.__tlqkf = clr


if __name__ == '__main__':
    t = Test()
    t.color = 'blue'

    print(t.color)
