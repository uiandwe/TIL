# -*- coding: utf-8 -*-
functions = []
for i in range(10):
    functions.append(lambda : i)

i = 0
for f in functions:
    print(f())
    i+=1
