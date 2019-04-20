# -*- coding: utf-8 -*-
# values를 정렬하되, group값이 앞에 오도록 helper 사용 (클로져)
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

# 결과값의 bool형태를 리턴하고 싶지만 에러(True가 반환되어야 함)
# 스코프 때문에 정상적인 값이 안됨
def sort_priority1(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found


# nonlocal로 상위 스코프를 참조
def sort_priority2(values, group):
    found = False
    def helper(x):
        nonlocal found # 현재 스코프가 아닌 상위단의 스코프를 참조하도록 한다. (global은 전역변수만 해당)
                       # but 단지 상위단만 참조하여 에러가 발생하기 쉽다.
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, args):
        if args in self.group:
            self.found = True
            return (0, args)
        return (1, args)

if __name__ == '__main__':
    numbers = [8, 3, 1, 2, 5, 4, 7, 6]
    group = {2, 3, 5, 7}
    sort_priority(numbers, group)
    print(numbers)

    found = sort_priority1(numbers, group)
    print("found", found, numbers)

    found = sort_priority2(numbers, group)
    print("found", found, numbers)


    sorter = Sorter(group)
    numbers.sort(key=sorter)
    assert sorter.found is True
    print(sorter.found)

