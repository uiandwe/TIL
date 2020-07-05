# -*- coding: utf-8 -*-
class Solution:

    def dfs(self, m, i, j):
        if i < 0 or i >= len(m) or j < 0 or j >= len(m[i]) or m[i][j] == '0':
            return

        m[i][j] = '0'

        self.dfs(m, i + 1, j)
        self.dfs(m, i - 1, j)
        self.dfs(m, i, j + 1)
        self.dfs(m, i, j - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) <= 0:
            return 0

        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    result += 1

        return result
