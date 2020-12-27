# -*- coding: utf-8 -*-
class Solution:
    def maxSubArray(self, nums):
        d = [0 for x in nums]
        d[0] = nums[0]
        for i in range(1, len(nums)):
            d[i] = max(d[i-1]+nums[i], nums[i])

        return max(d)

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([2, -1, 10]))
print(s.maxSubArray([-2, -1]))
