# -*- coding: utf-8 -*-
data = list(input())

print(data)
result = 0
group_count = 1
curr = data[0]
for i in range(1, len(data)):
    if curr != data[i]:
        curr = data[i]
        group_count += 1

print(group_count, group_count//2)




"""
0001100

> 1

"""
