# -*- coding: utf-8 -*-

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = []
        for i in nums:
            d.append(temp.index(i))

        return d








s = Solution()
print(s.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
