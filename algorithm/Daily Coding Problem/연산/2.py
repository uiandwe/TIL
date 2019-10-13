# -*- coding: utf-8 -*-
"""
Implement a job scheduler which takes in a function f and an integer n,

and calls f after n milliseconds.

"""

import time

def f():
    print("run func")


n = int(input())
print("n : {}".format(n))

time.sleep(n/1000)
f()
