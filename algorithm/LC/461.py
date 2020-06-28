# -*- coding: utf-8 -*-
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hd_str = "{0:b}".format(x ^ y)
        result = 0
        for s in hd_str:
            if s == '1':
                result += 1

        return result


s = Solution()
print(s.hammingDistance(1, 3))
print(s.hammingDistance(1, 4))
