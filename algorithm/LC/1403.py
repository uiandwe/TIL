# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        nums.sort(reverse=True)

        d = [0] * len(nums)
        sum_list = sum(nums)

        for i in range(len(nums)):
            d[i] = d[i-1] + nums[i]
            if d[i] > sum_list - d[i]:
                return nums[:i+1]
        return nums

s = Solution()
assert s.minSubsequence([6]) == [6]
assert s.minSubsequence([4, 3, 10, 9, 8]) == [10, 9]
assert s.minSubsequence([4,4,7,6,7]) == [7, 7, 6]
