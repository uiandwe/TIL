
import inspect

def provide(**provided_kwargs):
    def decorator(fun):
        def decorated(*args, **kwargs):

            func_kwargs = {}
            for key in inspect.signature(fun).parameters.keys():
                if key in provided_kwargs.keys():
                    func_kwargs[key] = provided_kwargs[key]

            kwargs.update(func_kwargs)
            return fun(*args, **kwargs)
        return decorated
    return decorator


@provide(a=2)
def add1(a: int, b: int) -> int:
    return a + b


@provide(a=2, b=3)
def add2(a: int, b: int) -> int:
    return a + b

@provide()
def add3(a: int, b: int) -> int:
    return a + b

@provide(nonexistent=123, b=3)
def add4(a: int, b: int) -> int:
    return a + b

@provide()
def add5(a: int, b: int) -> int:
    return a + b

assert add1(b=3) == 5
assert add2() == 5
assert add3(a=2, b=3) == 5
assert add4(a=2) == 5
assert add5(2, 3) == 5