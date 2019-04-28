# -*- coding: utf-8 -*-
# super를 통해 부모의 init을 하지 말자.
# 코드가 복잡해질수록 잘못된 로직을 일으킨다.

class MyBaseClass(object):
    def __init__(self, value):
        self.value = value


class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo(object):
    def __init__(self):
        self.value *= 2


class PlusFive(object):
    def __init__(self):
        self.value += 5


# super __init__을 활용한 다중 상속
# but 다중 상속은 하지 말자!!
class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = OneWay(5)
print("(5*2)+5 = ", foo.value)


class AnotherWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)

foo = AnotherWay(5)
print("(5*2)+5 = ", foo.value)


class TimesTwo2(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 2


class PlusFive2(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 5

# 다중 상속이 아닐 경우
# super의 init에서 잘못된 초기화가 되는걸 확인
# 같은 class를 상속 받았을때, 서로 super로 init을 하면 값이 틀어짐 
class ThisWay(TimesTwo2, PlusFive2):
    def __init__(self, value):
        TimesTwo2.__init__(self, value)
        PlusFive2.__init__(self, value)


foo = ThisWay(5)
print("(5*2)+5 = ", foo.value)
