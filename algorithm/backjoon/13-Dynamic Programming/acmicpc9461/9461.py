def solution(n):
    d = [1 for x in range(n+2)]

    for i in range(4, n+1):
        d[i] = d[i-2] + d[i-3]

    return d[n]


