# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        d = [[float('inf') for i in range(n + 1)] for j in range(m + 1)]
        d[m - 1][n] = 1
        d[m][n - 1] = 1

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                life = min(d[y + 1][x], d[y][x + 1])
                if life <= dungeon[y][x]:
                    d[y][x] = 1
                else:
                    d[y][x] = life - dungeon[y][x]

        return d[0][0]


s = Solution()
assert s.calculateMinimumHP([[-2, -3, 3],
                             [-5, -10, 1],
                             [10, 30, -5]]) == 7
assert s.calculateMinimumHP([[100]]) == 1
assert s.calculateMinimumHP([[-1,1]]) == 2
