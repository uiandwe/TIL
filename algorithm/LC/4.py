# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        d = []
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                d.append(nums1[0])
                nums1.pop(0)
            else:
                d.append(nums2[0])
                nums2.pop(0)

        while nums1:
            d.append(nums1[0])
            nums1.pop(0)

        while nums2:
            d.append(nums2[0])
            nums2.pop(0)

        center = len(d)//2

        if len(d) % 2 == 0:
            return (d[center] + d[center-1])/2
        else:
            return d[center]



s = Solution()
assert s.findMedianSortedArrays([1, 3], [2]) == 2
assert s.findMedianSortedArrays([1, 3], [200]) == 3
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0
assert s.findMedianSortedArrays([], [1]) == 1
assert s.findMedianSortedArrays([], [2, 3]) == 2.5
