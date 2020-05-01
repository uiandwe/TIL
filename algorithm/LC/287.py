# -*- coding: utf-8 -*-
class Solution:
    def findDuplicate(self, nums):
        t = r = nums[0]

        while True:
            t = nums[t]
            r = nums[nums[r]]
            if t == r:
                break

        r = nums[0]
        while t != r:
            t = nums[t]
            r = nums[r]
        return r


s = Solution()
assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
assert s.findDuplicate([2, 6, 4, 1, 3, 1, 5]) == 1
assert s.findDuplicate([2, 5, 9, 6, 9, 3, 8, 4, 7, 1]) == 9
