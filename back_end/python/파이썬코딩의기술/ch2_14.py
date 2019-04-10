# -*- coding: utf-8 -*-
def test():
    x = 0
    y = 5

    # 분자가 0일 경우 리턴값이 0이 되어 버림
    result = divide1(x, y)
    if result is None:
        print("Invalid inputs None")
    if not result:
        print("1 Invalid inputs False")

    # 두개를 리턴 (에러값, 데이터값)
    # 잘 동작하지만 리턴값이 두개나 사용해버림
    success, result = divide2(x, y)
    if not success:
        print("2 Invalid inputs False")
    else:
        print("2 Result is %.f" % result)

    # raise 로 except를 강제
    try:
        result = divide3(x, y)
    except ValueError:
        print("3 Invalid inputs")
    else:
        print("3 Result is %.f" % result)

    assert 1 == 2


def divide1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def divide2(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None


def divide3(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('3 Invalid input') from e
