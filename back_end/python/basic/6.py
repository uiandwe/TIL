# -*- coding: utf-8 -*-
# unpacking

arr = [1, 2, 3]

a, b, c = arr

print(a, b, c)


# enumerate

for i, v in enumerate(range(3)):
    print(i, v)


for i, v in enumerate(range(3), 1):
    print(i, v)

