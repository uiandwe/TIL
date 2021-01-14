from collections import Counter
from typing import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        intersection = d1 & d2

        return [key for key, val in intersection.items() for i in range(val)]





s = Solution()
assert s.intersect(nums1 = [1,2,2,1], nums2 = [2,2]) == [2, 2]
assert s.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [4, 9]
