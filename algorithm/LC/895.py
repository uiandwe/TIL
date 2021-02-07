# -*- coding: utf-8 -*-
from collections import Counter, OrderedDict, defaultdict


class FreqStack:

    def __init__(self):
        self.d = OrderedDict()
        self.c = Counter()

    def push(self, x: int) -> None:
        self.c[x] += 1
        cnt = self.c[x]
        if cnt not in self.d:
            self.d[cnt] = []
        self.d[cnt].append(x)

    def pop(self) -> int:
        k = next(reversed(self.d))
        item = self.d[k].pop()
        if len(self.d[k]) <= 0:
            del self.d[k]
        self.c[k] -= 1
        return item

# class FreqStack:
#
#     def __init__(self):
#         self.d = defaultdict(list)
#
#     def push(self, x: int) -> None:
#         keys = sorted(self.d.keys(), reverse=True)
#         key = 1
#         for k in keys:
#             if x in self.d[k]:
#                 key = k + 1
#                 break
#         self.d[key].append(x)
#
#     def pop(self) -> int:
#         keys = sorted(self.d.keys(), reverse=True)
#         for k in keys:
#             if len(self.d[k]) > 0:
#                 item = self.d[k].pop()
#                 return item

s = FreqStack()
s.push(5)
s.push(7)
s.push(5)
s.push(7)
s.push(4)
s.push(5)
assert s.pop() == 5
assert s.pop() == 7
assert s.pop() == 5
assert s.pop() == 4

