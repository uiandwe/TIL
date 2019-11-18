# -*- coding: utf-8 -*-
"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 

implement a function rand7() that returns an integer from 1 to 7 (inclusive).

"""



import random


def rand5():
    return random.randrange(1,6)

def solution():
    i = 5 * rand5() + rand5() - 5
    if i < 22:
        return i % 7 + 1
    return solution()



random_distribution = {}
for i in range(1000000):
    val = solution()
    if val in random_distribution:
        random_distribution[val] += 1
    else:
        random_distribution[val] = 1

import operator

print(sorted(random_distribution.items(), key=operator.itemgetter(1)))
