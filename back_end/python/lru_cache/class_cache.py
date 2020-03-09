# -*- coding: utf-8 -*-
# pip install ring
import ring


class ToTuple:
    def dictionary_check(self, input, array):
        for key, value in input.items():
            if isinstance(value, dict):
                self.dictionary_check(value, array)
                array.append(key)
            elif isinstance(value, list):
                self.list_check(value, array)
                array.append(key)
            else:
                array.append(key)
                array.append(value)

    def list_check(self, input, array):
        for value in input:
            if isinstance(value, list):
                self.list_check(value, array)
            elif isinstance(value, dict):
                self.dictionary_check(value, array)
            else:
                array.append(value)

    def __hash__(self):
        array = []
        self.dictionary_check(self.__dict__, array)
        return hash(tuple(array))


class Test(ToTuple):
    def __init__(self, value, list="list", d={}):
        self.value = value
        self.list = list
        self.d = d

    def __repr__(self):
        return "Test {}".format(self.value)

    def __str__(self):
        return "Test {}".format(self.value)

@ring.lru()
def cache_test(obj):
    print("obj", obj, obj.value, obj.list, obj.d)
    return obj


if __name__ == '__main__':
    t1 = Test(10, "123", {"key": [10, 20, 30]})
    t2 = Test(10, "123", {"key": [10, 20, 30]})
    t3 = Test(10, "123", {"key": [10, 20, 40]})
    t4 = Test(10, "123", {"key": [10, 20, 40]})

    print("result", cache_test(t1))
    print("result", cache_test(t2))
    print("result", cache_test(t3))
    print("result", cache_test(t4))
