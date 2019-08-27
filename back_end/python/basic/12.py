# -*- coding: utf-8 -*-
# set

# set comperhension
a = [1, 2, 3, 4, 5, 6, 6, 6, 7]

s = {x for x in a}

print(s)

s = {x for x in a if x > 3}

print(s)


s = {x if x > 3 else -1 for x in a}

print(s)


# uniquify a list

a = [1, 2, 2, 2, 2, 3, 4, 5, 5]

ua = list(set(a))

print(ua)


# union tow sets

a = {1, 2, 2, 2, 3}
b = {5, 5, 6, 6, 7}

print(a | b)

a = [1, 2, 2, 2, 3]
b = [5, 5, 6, 6, 7]

print(set(a + b))



# append items


a = { 1, 2, 3, 3, 3}
a.add(5)
print(a)

a |= {1, 2, 3, 4, 5, 6}
print(a)


# intersection tow sets 교집합

a = { 1, 2, 3, 3, 3}
b = {1, 5, 5, 6, 6, 7}

print(a & b)


# common item to list

a = [1, 1, 2, 3]
b = [1, 3, 5, 5, 6, 6]
com = list(set(a) & set(b))

print(com)


# contain

a = {1, 2}
b = {1, 2, 5, 6}
print(a <= b)


a = {1, 2, 5, 6}
b = {1, 5, 6}
print(a >= b)

# diff

a = {1, 2, 3}
b = {1, 5, 6, 8, 7}
print(a - b)


# symmetric diff

a = {1, 2, 3}
b = {1, 5, 6, 8, 7}
print(a ^ b)
