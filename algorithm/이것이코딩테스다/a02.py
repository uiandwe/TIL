# -*- coding: utf-8 -*-
data = list(input())

print(data)
result = 0
for i in data:
    if result in (0, 1) or i in ('0', '1'):
        result += int(i)
    else:
        result *= int(i)

print(result)



"""
02984
> 576

567
> 210

12984
> 864


"""
