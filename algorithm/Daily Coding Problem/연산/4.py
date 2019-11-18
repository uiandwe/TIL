# -*- coding: utf-8 -*-
"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, 

implement a function rand7() that returns an integer from 1 to 7 (inclusive).

"""


# -*- coding: utf-8 -*-
import random

import matplotlib.pyplot as plt
import pandas as pd


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

# import operator
# print(sorted(random_distribution.items(), key=operator.itemgetter(1)))
hist = [random_distribution[i] for i in range(1, 8)]
hist = pd.DataFrame(data=hist, index=range(1, 8))
hist.reset_index(inplace=True)
hist.columns = ['index', 'value']

print(hist)


plt.bar(hist.index, hist.value)
plt.ylim(hist.value.min(), hist.value.max())
plt.show()
