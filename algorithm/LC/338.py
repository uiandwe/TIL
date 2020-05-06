# -*- coding: utf-8 -*-
class Solution:
    def countBits(self, num: int):
        d = ["{0:b}".format(i).count('1') for i in range(num+1)]

        return d


s = Solution()
s.countBits(2)
