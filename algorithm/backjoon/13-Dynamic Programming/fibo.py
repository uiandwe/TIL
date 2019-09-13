import functools


class Fibo(object):
    def __init__(self):
        self.value = 0

    def __call__(self, *args, **kwargs):
        value = args
        print("run", value[0])
        return self.fibo(value[0])

    @functools.lru_cache(maxsize=100)
    def fibo(self, value):
        if value <= 0:
            return 0
        elif value == 1 or value == 2:
            return 1
        else:
            return self.fibo(value-1) + self.fibo(value-2)


def test_fibo():
    f = Fibo()
    assert f(-1) == 0
    assert f(0) == 0
    assert f(1) == 1
    assert f(2) == 1
    assert f(3) == 2
    assert f(4) == 3
    assert f(5) == 5
    assert f(6) == 8
