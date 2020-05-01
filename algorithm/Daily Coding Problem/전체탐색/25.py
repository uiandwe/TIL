# -*- coding: utf-8 -*-

def solution(A):
    temp_set = set()
    max_num = float('-inf')
    over_zero = -1
    for i in A:
        if i > 0:
            temp_set.add(i)
            max_num = max(max_num, i)
        if over_zero == -1:
            over_zero = i

    if len(temp_set) == 0:
        return 1

    for i in range(1, max_num):
        if i not in temp_set:
            return i

    return max_num + 1

assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([-1, -3]) == 1
assert solution([2, 3, 4, 5]) == 1
assert solution([1, 2, 3]) == 4
