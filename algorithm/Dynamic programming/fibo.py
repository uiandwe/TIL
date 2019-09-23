# https://www.acmicpc.net/problem/1003


def solution(n):
    if n == 0:
        return [1, 0]
    elif n == 1:
        return [0, 1]

    d = [[0, 0] for i in range(n+1)]
    d[0] = [1, 0]
    d[1] = [0, 1]

    for i in range(2, n+1):
        d[i][0] = d[i - 1][0] + d[i - 2][0]
        d[i][1] = d[i - 1][1] + d[i - 2][1]

    return d[n]


def test_soultion():
    assert solution(0) == [1, 0]
    assert solution(1) == [0, 1]
    assert solution(2) == [1, 1]
    assert solution(3) == [1, 2]
    assert solution(4) == [2, 3]
    assert solution(5) == [3, 5]
    assert solution(6) == [5, 8]
    assert solution(7) == [8, 13]
    assert solution(8) == [13, 21]


print(solution(2))
