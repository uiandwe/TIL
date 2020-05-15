# -*- coding: utf-8 -*-
class Solution:

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = len(nums) - 1

        while w <= b:
            cur = nums[w]
            if cur == 0:
                nums[w] = nums[r]
                nums[r] = 0
                r += 1
                w += 1
            elif cur == 1:
                w += 1
            else:
                nums[w] = nums[b]
                nums[b] = 2
                b -= 1

s = Solution()
nums = [0,0,2,2,1,1]
s.sortColors(nums)
assert nums == [0,0,1,1,2,2]
