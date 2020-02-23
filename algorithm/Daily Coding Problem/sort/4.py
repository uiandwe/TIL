# -*- coding: utf-8 -*-
def solution(m, lst):
    if len(lst) <= 0:
        return lst

    less = []
    equal = []
    more = []

    for i in lst:
        if i == m:
            equal.append(i)
        elif i < m:
            less.append(i)
        else:
            more.append(i)

    return less + equal + more


assert solution(10, [9, 12, 3, 5, 14, 10, 10]) == [9, 3, 5, 10, 10, 12, 14]
assert solution(8, [9, 12, 3, 5, 14, 10, 10]) == [3, 5, 9, 12, 14, 10, 10]
assert solution(8, [9, 12, 14, 10, 10]) == [9, 12, 14, 10, 10]
assert solution(8, [3, 5]) == [3, 5]
assert solution(8, [8, 8, 8]) == [8, 8, 8]
assert solution(8, []) == []
