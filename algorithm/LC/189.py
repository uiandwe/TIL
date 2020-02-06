# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, nums, k: int):
        n = len(nums)
        pivot = n - (k % n)
        return nums[pivot:] + nums[:pivot]


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

