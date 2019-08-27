# -*- coding: utf-8 -*-

l = [5, 4, 3, 2, 1]

l.sort()

print(l)

l.sort(reverse=True)

print(l)

new = sorted(l)

print(new)

d = {3: 'andy', 2:'david', 1:'amy'}

# key만 리턴됨
print(sorted(d))

# set 정렬
from operator import itemgetter

l = [('andy', 10), ('divid', 8), ('amy', 3)]

l.sort(key=itemgetter(1))

print(l)

# dict 정렬
from pprint import pprint
l = [
    {'name': 'andy', 'age': 10},
    {'name': 'divid', 'age': 8},
    {'name': 'amy', 'age': 3}
]

l.sort(key=itemgetter('age'))
pprint(l)
print(l)

# class 정렬
class Node(object):
    def __init__(self, value):
        self.val = value

    def __repr__(self):
        return f"Node({self.val})"


node = [Node(3), Node(2), Node(1)]
node.sort(key=lambda x: x.val)
print(node)

node.sort(key=lambda x: x.val, reverse=True)
print(node)

# class에 정렬 구현
class Child(Node):
    def __lt__(self, other):
        return self.val - other.val < 0

nodes = [Child(3), Child(2), Child(1)]

nodes.sort()

print(nodes)
