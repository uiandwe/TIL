# -*- coding: utf-8 -*-
from typing import *

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr.sort()
        pivot = abs(arr[0] - arr[1])

        for i in range(2, len(arr)):
            if abs(arr[i-1] - arr[i]) != pivot:
                return False

        return True


s = Solution()
assert s.canMakeArithmeticProgression([1, 2, 4]) is False
assert s.canMakeArithmeticProgression([3, 5, 1]) is True
