# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A, reverse=True)

        for i in range(2, len(A)):
            if A[i-2] < A[i-1] + A[i]:
                return A[i-2] + A[i-1] + A[i]

        return 0


s = Solution()
assert s.largestPerimeter([2, 1, 2]) == 5
assert s.largestPerimeter([1, 2, 1]) == 0
assert s.largestPerimeter([3, 2, 3, 4]) == 10
assert s.largestPerimeter([3, 6, 2, 3]) == 8
