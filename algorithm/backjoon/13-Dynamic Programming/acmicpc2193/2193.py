
def solution(n):
    if n == 1 or n == 2:
        return 1

    d = [1 for x in range(n+1)]

    for i in range(n):
        d[i] = d[i-1] + d[-2]

    return d[n]
