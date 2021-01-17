# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 0:
            return 0

        if len(nums) <= 2:
            return max(nums)

        d = [0 for i in range(len(nums))]
        d[0] = nums[0]
        d[1] = nums[1]
        d[2] = nums[2] + nums[0]

        for i in range(3, len(nums)):
            d[i] = max(d[i-2]+nums[i], d[i-3]+nums[i])

        return max(d)



s = Solution()
assert s.rob([1, 2, 3, 1]) == 4
assert s.rob([2, 7, 9, 3, 1]) == 12
