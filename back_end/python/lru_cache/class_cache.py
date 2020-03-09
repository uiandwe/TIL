# -*- coding: utf-8 -*-

import functools

def class_cache(func):
    cache = {}

    class ToTuple:
        def __init__(self):
            self.array = []

        def dictionary_check(self, input):
            for key, value in input.items():
                if isinstance(value, dict):
                    self.dictionary_check(value)
                    self.array.append(key)
                elif isinstance(value, list):
                    self.list_check(value)
                    self.array.append(key)
                else:
                    self.array.append(key)
                    self.array.append(value)

        def list_check(self, input):
            for value in input:
                if isinstance(value, list):
                    self.list_check(value)
                elif isinstance(value, dict):
                    self.dictionary_check(value)
                else:
                    self.array.append(value)

        def __call__(self, values):
            self.array = []
            if isinstance(values, dict):
                self.dictionary_check(values)
            else:
                self.list_check(values)

            return tuple(self.array)

        def __hash__(self):
            return hash(tuple(self.array))

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        temp_args = tuple([ToTuple()(arg.__dict__) for arg in args])
        temp_kwargs = {k: ToTuple()(v.__dict__) for k, v in kwargs.items()}
        h = hash((temp_args, ) + tuple(temp_kwargs.items()))
        if h in cache.keys():
            return cache[h]

        cache[h] = func(*args, **kwargs)
        return cache[h]

    return wrapped


class Test(object):
    def __init__(self, value, list="list", d={}):
        self.value = value
        self.list = list
        self.d = d

    def __repr__(self):
        return "Test {}".format(self.value)

    def __str__(self):
        return "Test {}".format(self.value)


@class_cache
def cache_test(obj):
    print("obj", obj, obj, obj.value, obj.list, obj.d)
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

