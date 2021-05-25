# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        self.m = len(image)
        self.n = len(image[0])
        visit = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.val = newColor

        y_position = [1, -1, 0, 0]
        x_position = [0, 0, 1, -1]

        def dfs(y, x):
            image[y][x] = self.val
            visit[y][x] = 1

            for i in range(4):
                next_y = y + y_position[i]
                next_x = x + x_position[i]

                if 0 <= next_y < self.m and 0 <= next_x < self.n:
                    if visit[next_y][next_x] == 0 and image[next_y][next_x] == self.c:
                        dfs(next_y, next_x)

        self.c = image[sr][sc]
        dfs(sr, sc)
        return image



s = Solution()
# s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
s.floodFill([[0,0,0],[0,1,1]], 1, 1, 1)
