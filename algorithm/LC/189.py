# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = n - (k % n)
        for i, v in enumerate(nums[pivot:] + nums[:pivot]):
            nums[i] = v


s = Solution()
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 1) == [7,1,2,3,4,5,6]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 2) == [6,7,1,2,3,4,5]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5,6,7,1,2,3,4]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 4) == [4,5,6,7,1,2,3]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 5) == [3,4,5,6,7,1,2]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 6) == [2,3,4,5,6,7,1]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 7) == [1, 2, 3, 4, 5, 6, 7]
assert s.rotate([1, 2, 3, 4, 5, 6, 7], 0) == [1, 2, 3, 4, 5, 6, 7]


assert s.rotate([-1,-100,3,99], 1) == [99,-1,-100, 3]
assert s.rotate([-1,-100,3,99], 2) == [3,99,-1,-100]

assert s.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]

