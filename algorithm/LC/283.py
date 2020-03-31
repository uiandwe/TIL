# -*- coding: utf-8 -*-
class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                if j != i:
                    nums[i] = 0
                j += 1

        return nums


s = Solution()
assert s.moveZeroes([0,1,0,3,12])  == [1,3,12,0,0]
