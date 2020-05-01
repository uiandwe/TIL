# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, m):
        n = len(m)
        m.reverse()

        for y in range(n):
            for x in range(y, n):
                if y != x:
                    m[y][x], m[x][y] = m[x][y], m[y][x]

        return m


s = Solution()
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

# matrix = [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ]
s.rotate(matrix)
