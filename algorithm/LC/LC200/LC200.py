class Solution:

    def dfs(self, i, j, map, lsland):
        """
        :type i: int
        :type j: int
        :type map: List[List[str]]
        :type lsland: int
        :rtype: int
        """
        position_x = [1, -1, 0, 0]
        position_y = [0, 0, 1, -1]

        n = len(map)
        m = len(map[0])

        for index in range(4):
            next_x = position_x[index] + i
            next_y = position_y[index] + j

            if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
                if map[next_x][next_y] == "1":
                    map[next_x][next_y] = lsland
                    self.dfs(next_x, next_y, map, lsland)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        lsland = 0
        n = len(grid)
        if n <= 0:
            return 0
        m = len(grid[0])
        if m <= 0:
            return 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid, lsland+1)
                    lsland += 1

        return lsland



