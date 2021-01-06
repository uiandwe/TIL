# -*- coding: utf-8 -*-
class Solution:
    def generateMatrix(self, n: int):
        l = m = n
        d = [[0 for x in range(m)] for y in range(m)]

        y = 0
        x = -1
        val = 1
        z = 1

        while val <= n*n:
            for i in range(l):
                x += z
                d[y][x] = val
                val += 1

            l -= 1
            m -= 1

            for i in range(m):
                y += z
                d[y][x] = val
                val += 1

            z *= -1

        print(d)

s = Solution()
s.generateMatrix(3)
