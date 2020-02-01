# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n_min = float('inf')
    n_max = float('-inf')
    for a in A:
        n_min = min(n_min, a)
        n_max = max(n_max, a-n_min)

    print(n_max)

solution([3171, 1011, 1123, 1366, 1013, 1367])

