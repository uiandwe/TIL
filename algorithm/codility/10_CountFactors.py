# -*- coding: utf-8 -*-

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    d = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            d.append(i)
            if i != N // i:
                d.append(N // i)

    return len(d)

assert solution(24) == 8
