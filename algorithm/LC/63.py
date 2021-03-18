# -*- coding: utf-8 -*-
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        d = [[0 for x in y] for y in obstacleGrid]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        d[0][0] = 1

        for y in range(m):
            for x in range(n):
                if obstacleGrid[y][x] == 0:
                    if y > 0:
                        d[y][x] += d[y-1][x]
                    if x > 0:
                        d[y][x] += d[y][x-1]
                else:
                    d[y][x] = 0

        return d[m-1][n-1]

s = Solution()
map = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
s.uniquePathsWithObstacles(map)

map = [
  [0,0,0, 0],
  [0,0,0, 0],
  [0,0,1, 0],
  [0,0,0, 0],
]
s.uniquePathsWithObstacles(map)
