# -*- coding: utf-8 -*-
"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.


"""

def get_perfect_number_10(n):
    d = 0
    for i in str(n):
        d += int(i)

    return (n * 10) + (10 - d)


assert get_perfect_number_10(1) == 19
assert get_perfect_number_10(10) == 109
assert get_perfect_number_10(12) == 127
