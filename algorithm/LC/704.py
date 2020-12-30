# -*- coding: utf-8 -*-
import bisect
class Solution:
    def search(self, nums, target: int) -> int:
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        return -1
