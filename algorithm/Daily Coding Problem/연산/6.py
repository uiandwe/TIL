# -*- coding: utf-8 -*-
"""
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 

implement a function rand5() that returns an integer from 1 to 5 (inclusive).

"""
from random import randint

def rand7():
    return randint(1, 7)


def rand5():
    d = rand7() * 7 + rand7() - 7
    if d < 16:
        return d % 5 + 1
    return rand5()

def solution():
    return rand5()



temp_dict = {1:0, 2:0, 3:0, 4:0, 5:0}

for i in range(100000):
    temp_i = solution()
    if temp_i in temp_dict.keys():
        temp_dict[temp_i] += 1
    else:
        print(temp_i)
        break

print(temp_dict)

