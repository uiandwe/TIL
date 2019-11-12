# -*- coding: utf-8 -*-
class FunctionalList:
    '''head, tail, init, last, drop 및 take와 같은 추가적인 함수형 매직으로
    목록을 래핑하는 클래스입니다.'''


    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # key의 타입이나 값이 유효하지 않은 경우,리스트의 값은 에러를 발생시킵니다.
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)
    def head(self):
        # 첫 번째 요소를 가져옵니다.
        return self.values[0]
    def tail(self):
        # 첫 번째 이후의 모든 요소들을 가져옵니다.
        return self.values[1:]
    def init(self):
        # 마지막 까지의 직전 요소들을 가져옵니다.
        return self.values[:-1]
    def last(self):
        # 마지막 요소를 가져옵니다.
        return self.values[-1]
    def drop(self, n):
        # 처음 n개를 제외한 모든 요소를 가져옵니다.
        return self.values[n:]
    def take(self, n):
        # 처음 n개의 요소를 가져옵니다.
        return self.values[:n]


if __name__ == '__main__':
    fl = FunctionalList()
    fl.append(10)

    print("len", len(fl))
    print("getitem", fl[0])
    fl[0] = 20
    print("setitem", fl[0])

    for v in fl:
        print("iter", v)

    for v in reversed(fl):
        print("reversed", v)

    del fl[0]
    print("len", len(fl))
