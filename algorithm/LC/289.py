# -*- coding: utf-8 -*-

class Solution:
    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        d = [[0 for i in range(n)] for i in range(m)]
        y_scope = [-1, -1, -1, 0, 0, 1, 1, 1]
        x_scope = [-1, 0, 1, -1, 1, -1, 0, 1]

        def checkLife(y, x):
            around_life = 0
            for i in range(8):
                next_y = y + y_scope[i]
                next_x = x + x_scope[i]
                if 0 <= next_y < m and 0 <= next_x < n:
                    if board[next_y][next_x] == 1:
                        around_life += 1

            if board[y][x] == 1:
                if 2 <= around_life <= 3:
                    d[y][x] = 1
                else:
                    d[y][x] = 0
            if board[y][x] == 0 and around_life == 3:
                d[y][x] = 1

        for y in range(m):
            for x in range(n):
                checkLife(y, x)

        for y in range(m):
            for x in range(n):
                board[y][x] = d[y][x]


s = Solution()
# assert s.gameOfLife([[1,1], [1,0]]) == [[1,1], [1,1]]
board = [[0,1,0], [0,0,1], [1,1,1], [0,0,0]]
s.gameOfLife(board)
print(board)
assert board == [[0,0,0], [1,0,1], [0,1,1], [0,1,0]]


def gameOfLifeInfinite(self, live):
    ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
    live = self.gameOfLifeInfinite(live)
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live)
