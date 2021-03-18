# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums):
        d = [0 for x in nums]
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = max(nums[i], d[i-1]+nums[i])

        return max(d)

s = Solution()
assert s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert s.maxSubArray([2, -1, 10]) == 11
assert s.maxSubArray([-2, -1]) == -1
