# -*- coding: utf-8 -*-
from typing import *
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        ret = []
        for val in arr2:
            ret.extend([val] * d.pop(val))

        for key in sorted(d.keys()):
            ret.extend([key] * d[key])

        return ret




s = Solution()
s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6])
