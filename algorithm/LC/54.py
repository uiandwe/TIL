# -*- coding: utf-8 -*-
class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        smax = m*n
        y = 0
        x = -1
        d = 1
        ret = []

        while 0 < smax:

            for i in range(n):
                x += d
                ret.append(matrix[y][x])
                smax -= 1
            n -= 1
            m -= 1
            for i in range(m):
                y += d
                ret.append(matrix[y][x])
                smax -= 1
            d *= -1

        return ret


s = Solution()
assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
assert s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]


