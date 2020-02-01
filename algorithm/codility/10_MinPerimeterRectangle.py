# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    min_val = float('inf')

    for i in range(1, int(N ** 0.5) + 1):
        d = []
        if N % i == 0:
            d.append(i)
            if i != N // i:
                d.append(N // i)

        if len(d) == 2:
            min_val = min((d[0]*2) + (d[1]*2), min_val)
        if len(d) == 1:
            min_val = min((d[0] * 4), min_val)

    if min_val == float('inf'):
        return N

    return min_val


assert solution(36) == 24
assert solution(1) == 4
assert solution(30) == 22
assert solution(10) == 14
