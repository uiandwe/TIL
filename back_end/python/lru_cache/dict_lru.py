

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



@hash_dict
@functools.lru_cache()
def cache_test(obj):
    print("obj", obj)
    return obj

if __name__ == '__main__':
    # t1 = Test(10)
    dict1 = {"test": 1}
    cache_test(dict1)

    dict2 = {"test": 1}
    cache_test(dict2)

    dict3 = {"test": 1}
    cache_test(dict3)
