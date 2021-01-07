# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        m = len(mat)
        n = len(mat[0])
        ret = [[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                d[j-i].append(mat[i][j])

        for key in d.keys():
            d[key].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                ret[i][j] = d[j-i].pop()

        return ret



s = Solution()
s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])
s.diagonalSort([[11,25,66,1,69,7],
                [23,55,17,45,15,52],
                [75,31,36,44,58,8],
                [22,27,33,25,68,4],
                [84,28,14,11,5,50]])
# [[5,17,4,1,52,7],
# [11,11,25,45,8,69],
# [14,23,25,44,58,15],
# [22,27,31,36,50,66],
# [84,28,75,33,55,68]]
