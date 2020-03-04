
import functools
import weakref

def hash_dict(func):
    """Transform mutable dictionnary
    Into immutable
    Useful to be compatible with cache
    """
    class HDict(dict):
        def __hash__(self):
            return hash(frozenset(self.items()))

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        args = tuple([HDict(arg) if isinstance(arg, dict) else arg for arg in args])
        kwargs = {k: HDict(v) if isinstance(v, dict) else v for k, v in kwargs.items()}
        return func(*args, **kwargs)
    return wrapped



class Test:
    def __init__(self, value, something):
        self.value = value
        self.list = tuple(something)

    def __repr__(self):
        return "Test {}".format(self.value)

    def __str__(self):
        return "Test {}".format(self.value)


@hash_dict
@functools.lru_cache()
def cache_test(obj):
    print("obj", obj)
    return obj

if __name__ == '__main__':
    t1 = Test(10, [1, 2, 3])
    t2 = Test(10, [1, 2, 3])
    t3 = Test(10, [1, 2, 3])
    print(hash(frozenset(t1.__dict__)), hash(frozenset(t2.__dict__)), hash(frozenset(t3.__dict__)))

    cache_test(t1.__dict__)
    cache_test(t2.__dict__)
    cache_test(t3.__dict__)

    dict1 = {"test": 1}
    dict2 = {"test": 1}
    dict3 = {"test": 1}
    print(hash(frozenset(dict1)), hash(frozenset(dict2)), hash(frozenset(dict3)))

    cache_test(dict1)
    cache_test(dict2)
    cache_test(dict3)
