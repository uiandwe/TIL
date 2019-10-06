def solution(m, n, puddles):
    d = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for p in puddles:
        d[p[1]][p[0]] = -1

    d[1][1] = 1  # 시작점

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if d[i][j] != -1:
                d[i][j] = max(d[i][j], d[i - 1][j] + d[i][j - 1], d[i - 1][j], d[i][j - 1])

    return d[n][m] % 1000000007


assert solution(1, 2, []) == 1
assert solution(4, 3, [[2, 2]]) == 4
assert solution(4, 3, [[2, 2], [1, 2]]) == 3
