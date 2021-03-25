# -*- coding: utf-8 -*-
data = list(map(int, list(input())))

print(data)
n = len(data)
if sum(data[:n//2]) == sum(data[n//2:]):
    print("lucky")
else:
    print("ready")




"""
123402
>lucky
7755
> ready
"""
