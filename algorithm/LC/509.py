# -*- coding: utf-8 -*-
class Solution:
    def fib(self, n: int) -> int:
        d = [0 for _ in range(n+1)]
        if n <= 1:
            return n

        d[1] = 1
        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]

        return d[n]


s = Solution()
assert s.fib(2) == 1
assert s.fib(3) == 2
assert s.fib(4) == 3

