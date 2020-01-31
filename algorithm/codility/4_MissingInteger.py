# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    d = {}

    for i in A:
        if i > 0:
            d[i] =  i

    if len(d.keys()) <= 0:
        return 1
    arr = sorted(d.keys())

    for i, val in enumerate(arr):
        if i+1 != val:
            return i+1

    return len(arr)+1


assert solution([1, 3, 6, 4, 1, 2]) == 5
assert solution([1, 2, 3]) == 4
assert solution([-1, -3]) == 1
