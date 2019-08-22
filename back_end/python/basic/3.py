# -*- coding: utf-8 -*-
# shallow copy
a = [1, 2]
b = list(a)
b[0] = 123

print(a, b)

a = [[1], [2]]
b = list(a)
b[0][0] = 123

print(a, b)


# deep copy
import copy
a = [[1], [2]]
b = copy.deepcopy(a)
b[0][0] = 123

print(a, b)
