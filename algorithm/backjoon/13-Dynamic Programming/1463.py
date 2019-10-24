# top-down
# -*- coding: utf-8 -*-
def solution(n):
    d = [0 for x in range(n+1)]
    if n == 1: return 0
    if d[n] > 0: return d[n]

    d[n] = solution(n-1)+1
    if n % 2 == 0:
        d[n] = min(solution(n//2)+1, d[n])

    if n % 3 == 0:
        d[n] = min(solution(n//3)+1, d[n])

    return d[n]


assert solution(10) == 3
assert solution(2) == 1




def solution(n):

    d = [0 for x in range(20)]
    d[1] = d[2] = d[3] = 1

    for i in range(4, n+1):
        d[i] = d[i-1] + 1
        if i % 2 == 0:
            d[i] = min(d[i], d[int(i/2)]+1)
        if i % 3 == 0:
            d[i] = min(d[i], d[int(i/3)]+1)

    print(d, d[n])



solution(2)
solution(10)


class MakeOne():
    def __init__(self):
        self.array = []

    def __call__(self, *args, **kwargs):
        value = args[0]
        self.array = [0 for i in range(value + 1)]
        self.array[2] = 1
        self.array[3] = 1

        if value <= 3:
            return self.array[self.vlaue]

        for i in range(4, value+1):
            self.array[i] = self.array[i-1] + 1
            if i % 3 == 0 and self.array[int(i/3)]+1 <= self.array[i]:
                self.array[i] = self.array[int(i/3)] + 1
            if i % 2 == 0 and self.array[int(i/2)]+1 <= self.array[i]:
                self.array[i] = self.array[int(i/2)] + 1

        print(self.array)


mo = MakeOne()
mo(4)
mo(6)
mo(10)
