# -*- coding: utf-8 -*-
# https://www.acmicpc.net/problem/10844

def solution(n):
    d = [[0 for x in range(11)] for y in range(n+1)]

    for i in range(1, 10):
        d[1][i] = 1

    for i in range(2, n+1):
        d[i][0] = d[i-1][1]
        for j in range(1, 10):
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

    result = 0
    for i in range(10):
        result += d[n][i]

    return result

assert solution(1) == 9
assert solution(2) == 17
