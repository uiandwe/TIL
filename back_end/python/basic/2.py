# -*- coding: utf-8 -*-
# list initialize

a = [None] * 3

print(a) # [None, None, None]


a[0] = "foo"

print(a) # ["foo", None, None]


a = [[]] * 3

print(a) # [[], [], []]


b = [[] for _ in range(3)]

a[0].append("hello")

print(a) # [['hello'], ['hello'], ['hello']]

b[0].append("python")

print(b) # [['python'], [], []]

