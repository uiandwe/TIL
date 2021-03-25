# -*- coding: utf-8 -*-
data = list(input())


print(data)
result = []
val = 0
for d in data:
    if d.isdigit():
        val+= int(d)
    else:
        result.append(d)

print("".join(sorted(result))+str(val))

"""
k1ka5cb7
>abckk13

"""
