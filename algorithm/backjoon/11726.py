# -*- coding: utf-8 -*-
def solution(n):
    d = [0 for x in range(n+1)]

    d[1] = 1
    d[2] = 3

    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]*2

    return d[n]


assert solution(2) == 3
assert solution(8) == 171
assert solution(12) == 2731
