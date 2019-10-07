# -*- coding: utf-8 -*-
"""

For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17.

"""

def solution(arr, k):
    for value in arr:
        if k-value in arr:
            return value, k-value
    return ()

print(solution([10, 15, 3, 7], 17))
print(solution([10, 15, 3, 7], 19))
