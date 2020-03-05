# -*- coding: utf-8 -*-

import functools
import attr


def class_cache(func):
    cache = {}

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        temp_args = tuple([frozenset(arg.__dict__) for arg in args])
        temp_kwargs = {k: frozenset(v.__dict__) for k, v in kwargs.items()}
        h = hash((temp_args, ) + tuple(temp_kwargs.items()))
        if h in cache.keys():
            return cache[h]

        cache[h] = func(*args, **kwargs)
        return cache[h]

    return wrapped


@attr.s
class Test(object):
    value = attr.ib()
    list = attr.ib()
    d = attr.ib()

    def __init__(self, value, list=[], d={}):
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
    t1 = Test(10, [1, 2, [3]], {"key": "value"})
    t2 = Test(10, [1, 2, [3]], {"key": "value"})
    t3 = Test(10, [1, 2, [3]], {"key": "value"})

    print("result", cache_test(t1))
    print("result", cache_test(t2))
    print("result", cache_test(t3))
