# -*- coding: utf-8 -*-
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        d = n & 1
        n = n >> 1

        while n:
            if n & 1 != d:
                d = n & 1
                n = n >> 1
            else:
                return False

        return True

s = Solution()
assert s.hasAlternatingBits(5) == True
assert s.hasAlternatingBits(3) == False
