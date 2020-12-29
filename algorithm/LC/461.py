# -*- coding: utf-8 -*-
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return "{0:b}".format(x ^ y).count("1")


s = Solution()
print(s.hammingDistance(1, 3))
print(s.hammingDistance(1, 4))
