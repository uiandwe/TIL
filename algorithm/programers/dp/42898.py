# -*- coding: utf-8 -*-
#https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    d = [[0 for x in range(m+1)] for y in range(n+1)]
    d[1][1] = 1

    for puddle in puddles:
        x = puddle[0]
        y = puddle[1]
        d[y][x] = -1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if d[i][j] == 0:
                if d[i-1][j] == -1 or d[i][j-1] == -1:
                    d[i][j] = max(d[i-1][j], d[i][j-1])
                else:
                    d[i][j] = d[i-1][j] + d[i][j-1]

    return d[n][m] % 1000000007


assert solution(4, 3, [[2, 2]]) == 4
assert solution(4, 3, [[1, 2], [2, 2]]) == 3
assert solution(3, 3, [[2, 2]]) == 2
assert solution(3, 3, [[2, 2], [2, 1], [1, 2]]) == 0
assert solution(2, 2, []) == 2
assert solution(1, 1, []) == 1
assert solution(2, 1, []) == 1
