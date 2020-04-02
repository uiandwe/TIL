# -*- coding: utf-8 -*-
class Solution:
    def singleNumber(self, nums):
        ret_num = 0
        for i in nums:
            ret_num ^= i

        return ret_num


s = Solution()
assert s.singleNumber([2,2,1]) == 1
assert s.singleNumber([4, 1, 2,2,1]) == 4

