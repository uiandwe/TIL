# -*- coding: utf-8 -*-

def combination(n, m):
    if n == 0 or m == 0 or n == m:
        return 1

    return combination(n - 1, m) + combination(n-1, m-1)


print(combination(1, 1))
print(combination(1, 2))
print(combination(2, 1))
print(combination(2, 2))
print(combination(3, 1))
print(combination(4, 1))
print(combination(5, 2))
