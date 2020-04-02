# -*- coding: utf-8 -*-
class Solution:
    def singleNumber(self, nums):

        low = high = 0
        for i in nums:
            low = ~high & (low ^ i)
            high = ~low & (high ^ i)

        return low

s = Solution()
assert s.singleNumber([2,2,3,2]) == 3
