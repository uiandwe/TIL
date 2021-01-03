# -*- coding: utf-8 -*-
def wayToScore(n):
    d = [0 for i in range(n+1)]

    d[0] = 1

    for i in range(1, n+1):
        if i-3 >= 0:
            d[i] += d[i-3]
        if i-5 >= 0:
            d[i] += d[i-5]
        if i-10 >= 0:
            d[i] += d[i-10]

    return d[n]

print(wayToScore(13))
