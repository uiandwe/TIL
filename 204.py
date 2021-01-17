# -*- coding: utf-8 -*-
from math import sqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2:
            return 0

        d = [True] * n

        for i in range(2, int(sqrt(n))+1):
            if d[i]:
                j = i*i
                while j < n:
                    d[j] = False
                    j += i
        # print(d)
        count = 0
        for p in range(2, n):
            if d[p]:
                count += 1

        return count


s = Solution()
assert s.countPrimes(10) == 4
assert s.countPrimes(3) == 1
assert s.countPrimes(499979)

