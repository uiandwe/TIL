from collections import deque
class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        q = deque()
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    q.append((y, x))

        while q:
            y, x = q.popleft()

            for next_y in range(m):
                matrix[next_y][x] = 0
            for next_x in range(n):
                matrix[y][next_x] = 0

        return matrix



s = Solution()
assert s.setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]
assert s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
