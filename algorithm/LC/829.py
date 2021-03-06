# -*- coding: utf-8 -*-
"""
15
4 + 5 + 6
(3+1) + (3+2) + (3+3) = 15
3 + 3 + 3 = 15 - 1 - 2 - 3

=============================
( 3 + 3 + 3 ) % 3 == 0
(15 - 1 - 2 - 3) % 3 == 0
=============================
then
(15 - 1 - 2 - 3 - 4) % 4 != 0

(15 - 1 - 2 - 3 - 4 - 5) % 5 == 0

(15 - 1) % 1 == 0

(15 - 1 - 2) % 2 == 0
"""
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count, i = 0, 1
        while N > 0:
            N -= i
            if N % i == 0:
                count += 1
            i += 1
        return count

s = Solution()
assert s.consecutiveNumbersSum(5) == 2
assert s.consecutiveNumbersSum(15) == 4
