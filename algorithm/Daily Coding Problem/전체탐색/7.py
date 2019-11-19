# -*- coding: utf-8 -*-
"""
Given a array of numbers representing the stock prices of a company in chronological order,

write a function that calculates the maximum profit you could have made from buying and selling that stock once.

You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,

since you could buy the stock at 5 dollars and sell it at 10 dollars.

"""


def get_stock_profit(n):

    if len(n) <= 1:
        return 0

    min_value = n[0]
    max_value = float('-inf')

    for value in n:
        if min_value > value:
            min_value = value
        if abs(value - min_value) > max_value:
            max_value = abs(value - min_value)

    return max_value


assert get_stock_profit([9, 11, 8, 5, 7, 10]) == 5
assert get_stock_profit([1, 1, 1, 2]) == 1
assert get_stock_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 9
assert get_stock_profit([-1, 1, 1, 2]) == 3
assert get_stock_profit([-1, -2, -3, 2]) == 5
assert get_stock_profit([1, 2, 3, 4, 5]) == 4
assert get_stock_profit([1, 1, 1, 1, 1]) == 0
assert get_stock_profit([1, 1, 1, 2, 1]) == 1
