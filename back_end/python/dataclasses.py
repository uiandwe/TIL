# -*- coding: utf-8 -*-
import inspect
import typing
from contextlib import suppress
from functools import wraps

from dataclasses import dataclass, field, asdict, astuple, make_dataclass


class _SpecialForm:
    Any = object()
    def __getitem__(self, typeargs: Any) -> Any: ...


# https://stackoverflow.com/questions/50563546/validating-detailed-types-in-python-dataclasses
def enforce_types(callable):
    spec = inspect.getfullargspec(callable)

    def check_types(*args, **kwargs):
        parameters = dict(zip(spec.args, args))
        parameters.update(kwargs)
        for name, value in parameters.items():
            with suppress(KeyError):  # Assume un-annotated parameters can be any type
                type_hint = spec.annotations[name]
                if isinstance(type_hint, _SpecialForm):
                    # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
                    continue
                try:
                    actual_type = type_hint.__origin__
                except AttributeError:
                    # In case of non-typing types (such as <class 'int'>, for instance)
                    actual_type = type_hint
                # In Python 3.8 one would replace the try/except with
                # actual_type = typing.get_origin(type_hint) or type_hint
                if isinstance(actual_type, _SpecialForm):
                    # case of typing.Union[…] or typing.ClassVar[…]
                    actual_type = type_hint.__args__
                #
                if not isinstance(value, actual_type):
                    raise TypeError('Unexpected type for {} (expected {} but found {})'.format(name, type_hint, type(value)))

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            check_types(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    if inspect.isclass(callable):
        callable.__init__ = decorate(callable.__init__)
        return callable

    return decorate(callable)


class Valid:
    def validtion(self):
        attributes = inspect.getmembers(self, lambda a: not (inspect.isroutine(a)))
        class_field = dict()
        for attr in attributes:
            if attr[0] == '__annotations__':
                class_field = attr[1]
                break

        for key in class_field.keys():

            if isinstance(class_field[key], typing.GenericMeta):
                continue
            # print(key, class_field[key], self.__getattribute__(key), type(class_field[key]))

            if not isinstance(self.__getattribute__(key), class_field[key]):
                raise TypeError(
                    'Unexpected type for {} (expected {} but found {})'.format(key, class_field[key], type(self.__getattribute__(key))))



@enforce_types
@dataclass
class User:
    name: str = ""
    agree: bool = True
    tag: typing.List[str] = field(default_factory=list)


@dataclass
class User2(Valid):
    name: str = ""
    agree: bool = True
    tag: typing.List[str] = field(default_factory=list)


if __name__ == '__main__':

    p = User("Kim", True)

    assert asdict(p) == {'name': "Kim", 'agree': True, 'tag':[]}
    assert type(p) == User
    assert type(asdict(p)) == dict

    Article = make_dataclass('article',
                             [('title', str),
                              ('text', str),
                              ('index', int, field(default=5))])

    a = Article("title", "text", 1)
    assert type(a) == Article
    assert type(asdict(a)) == dict
    assert type(astuple(a)) == tuple

    

    test = User2(111, 111)
    try:
        test.validtion()
    except TypeError as e:
        print(e)
