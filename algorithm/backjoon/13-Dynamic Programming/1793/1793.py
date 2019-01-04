'''
1 -> 0
2 -> 3
3 -> 5
4 -> 11
5 -> 21

d[i] = d[i-1] + d[i-2]*2
'''


def solution(n):

    if n == 1:
        return 0
    if n == 2:
        return 3
    if n == 3:
        return 5

    d = [0 for x in range(n+1)]

    d[1] = 0
    d[2] = 3
    d[3] = 5

    for i in range(4, n+1):
        d[i] = d[i-1] + (d[i-2]*2)
    return d[n]
