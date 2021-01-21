# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        cnt = 0

        def dfs(y, x):
            if 0 <= y < self.m and 0 <= x < self.n and grid[y][x] == 1:
                grid[y][x] = 0

                d1 = dfs(y+1, x)
                d2 = dfs(y-1, x)
                d3 = dfs(y, x+1)
                d4 = dfs(y, x-1)

                return d1 + d2 + d3 + d4 + 1
            else:
                return 0

        for y in range(self.m):
            for x in range(self.n):
                if grid[y][x] == 1:
                    cnt = max(cnt, dfs(y, x))

        return cnt





grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

s = Solution()
assert s.maxAreaOfIsland(grid) == 6

assert s.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
