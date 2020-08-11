# -*- coding: utf-8 -*-
class Solution:
    def removeDuplicates(self, nums) -> int:
        index = 0
        for j in range(len(nums)):
            if nums[j] != nums[index]:
                nums[index] = nums[j]
                index += 1
        return index

