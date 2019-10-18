# -*- coding: utf-8 -*-
import random

count = 0
n = 100000

for i in range(n):
    x = random.random()
    y = random.random()

    if x*x + y*y < 1:
        count += 1

a = 4 * count / n

print(a)
