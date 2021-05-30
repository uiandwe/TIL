# -*- coding: utf-8 -*-
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ret = [-1, -1]

        def find_bs(target, p):
            index = -1
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    index = mid
                    if p > 0:
                        l = mid + p
                    else:
                        r = mid + p
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return index

        ret[1] = find_bs(target, 1)
        ret[0] = find_bs(target, -1)

        return ret



s = Solution()
assert s.searchRange([5,7,7,8,8,10], 8) == [3, 4]
assert s.searchRange([5,7,7,8,8,10], 6) == [-1, -1]
assert s.searchRange([1], 1) == [0, 0]
assert s.searchRange([2, 2], 2) == [0, 1]
print(s.searchRange([1, 1, 2], 1))
print(s.searchRange([], 0))
print(s.searchRange([2, 2], 3))
