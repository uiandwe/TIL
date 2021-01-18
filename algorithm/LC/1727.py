# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n, ans = len(matrix), len(matrix[0]), 0

        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j] if matrix[i][j] else 0

        for i in range(m):
            matrix[i].sort(reverse=True)
            for c in range(n):
                ans = max(ans, (c+1)*matrix[i][c])

        return ans



s = Solution()
assert s.largestSubmatrix([[0,0,1],[1,1,1],[1,0,1]]) == 4
assert s.largestSubmatrix([[1,1,0],[1,0,1]]) == 2
assert s.largestSubmatrix([[1,0,1,0,1]]) == 3



