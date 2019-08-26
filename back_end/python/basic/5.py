# -*- coding: utf-8 -*-
# filter items

print([x for x in range(5) if x > 1])

l = ['1', '2', 3, 'hello', 4]

f = lambda x: isinstance(x, int)

print(filter(f, l))

print(list(filter(f, l)))


print(list(i for i in l if f(i)))
