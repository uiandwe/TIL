# -*- coding: utf-8 -*-
#https://programmers.co.kr/learn/courses/30/lessons/42898
def solution(m, n, puddles):
    d = [[0 for x in range(m+1)] for y in range(n+1)]
    if puddles and len(puddles) > 0:
        for v in puddles:
            d[v[1]][v[0]] = -1

    d[1][1] =1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if d[i][j] == -1:
                d[i][j] = 0
            else:
                if d[i-1][j] > 0 and d[i][j-1] > 0:
                    d[i][j] = d[i-1][j] + d[i][j-1]
                else:
                    d[i][j] = max(d[i-1][j], d[i][j-1], d[i][j])

    return d[n][m] % 1000000007


assert solution(4, 3, [[2, 2]]) == 4
assert solution(4, 3, [[1, 2], [2, 2]]) == 3
assert solution(3, 3, [[2, 2]]) == 2
assert solution(3, 3, [[2, 2], [2, 1], [1, 2]]) == 0
assert solution(2, 2, []) == 2
assert solution(1, 1, []) == 1
assert solution(2, 1, []) == 1
