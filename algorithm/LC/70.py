# -*- coding: utf-8 -*-
class Solution:

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        d = [0 for x in range(n+1)]
        d[1] = 1
        d[2] = 2
        d[3] = 3

        for i in range(4, len(d)):
            d[i] = d[i-1] + d[i-2]

        return d[n]




s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
