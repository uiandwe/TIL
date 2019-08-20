# -*- coding: utf-8 -*-
# LIST from scratch

a = [1, 2, 3, 4, 5]

print(2 in a) # True

print(a[-1]) # 5

print(a[:]) # [1, 2, 3, 4, 5]

print(a[1:]) #[2, 3, 4, 5]

print(a[1:-1]) #[2, 3, 4]

print(a[1:-1:2]) # [2, 4]

print(a[::-1]) # [5, 4, 3, 2, 1] reverse

print(a[:0:-1]) # [5, 4, 3, 2]

a[0] = 0

print(a) # [0, 2, 3, 4, 5]

# add item
a.append(6)

print(a) # [0, 2, 3, 4, 5, 6]

# list + list
a.extend([7, 8, 9])

print(a) # [0, 2, 3, 4, 5, 6, 7, 8, 9]

#delete item
del a[-1]
print(a) # [0, 2, 3, 4, 5, 6, 7, 8]

# list comprehension
b = [x for x in range(3)]
print(b) # [0, 1, 2]

# add two lists
print(a + b) # [0, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2]

