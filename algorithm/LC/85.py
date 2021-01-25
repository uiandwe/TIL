# -*- coding: utf-8 -*-
from typing import *

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0

        max_area = 0
        d = [0] * n

        for row in matrix:
            for i, v in enumerate(row):
                if v == '1':
                    d[i] += 1
                else:
                    d[i] = 0

            s = []
            for i, h in enumerate(d):
                start = i
                while s and s[-1][1] > h:
                    index, height = s.pop()
                    max_area = max(max_area, height * (i - index))
                    start = index

                s.append((start, h))

            for i, h in s:
                max_area = max(max_area, h * (n - i))

        return max_area

s = Solution()
assert s.maximalRectangle(matrix = [[ "1", "0", "1", "0", "0"], [ "1", "0", "1", "1", "1"], [ "1", "1", "1", "1", "1"], [ "1", "0", "0", "1", "0"]]) == 6
assert s.maximalRectangle(matrix = []) == 0
assert s.maximalRectangle(matrix = [[]]) == 0
assert s.maximalRectangle(matrix = [['0']]) == 0
assert s.maximalRectangle(matrix = [['1']]) == 1
assert s.maximalRectangle(matrix = [['1', '1']]) == 2
assert s.maximalRectangle(matrix = [['0', '0']]) == 0
assert s.maximalRectangle(matrix = [['1', '0']]) == 1


