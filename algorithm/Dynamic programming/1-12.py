# -*- coding: utf-8 -*-
def printTable(n):
    for i in range(10):
        print("{} * {} = {}".format(n, i, n*i))


def dp(n, i):
    if i == 10:
        return

    print("{} * {} = {}".format(n, i, n * i))
    dp(n, i+1)

printTable(2)
dp(2, 1)
