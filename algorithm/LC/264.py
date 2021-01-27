# -*- coding: utf-8 -*-

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly = 0
        to_add = {1}
        while ugly < n:
            x = min(to_add)
            to_add.remove(x)
            ugly += 1
            for p in [2, 3, 5]:
                to_add.add(x * p)

        return x


s = Solution()
assert s.nthUglyNumber(10) == 12
assert s.nthUglyNumber(11) == 15

