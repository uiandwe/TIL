# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def exist(self, board, word):

        def dfs(word, i, j):
            if i <= -1 or i >= len(board) or j <= -1 or j >= len(board[0]): return False
            if board[i][j] == -1 or board[i][j] != word[0]: return False
            if len(word) == 1: return True

            temp, board[i][j] = board[i][j], -1
            if dfs(word[1:], i - 1, j): return True
            if dfs(word[1:], i + 1, j): return True
            if dfs(word[1:], i, j - 1): return True
            if dfs(word[1:], i, j + 1): return True
            board[i][j] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, i, j): return True
        return False

class Solution:
    check = False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])

        d = [[0 for x in range(self.n)] for y in range(self.m)]

        def dfs(y, x, s):

            if y < 0 or y >= self.m or x < 0 or x >= self.n or d[y][x] == 1:
                return

            d[y][x] = 1
            s += board[y][x]

            if s == word:
                self.check = True
                return

            if not word.startswith(s) or len(s) > len(word):
                d[y][x] = 0
                return

            dfs(y + 1, x, s)
            dfs(y - 1, x, s)
            dfs(y, x + 1, s)
            dfs(y, x - 1, s)
            d[y][x] = 0

        for y in range(self.m):
            for x in range(self.n):
                if self.check:
                    return True
                if word[0] == board[y][x]:
                    dfs(y, x, '')

        return self.check


s = Solution()
# assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") is True
# assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") is True
# assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") is False
# assert s.exist([["a","b"],["c","d"]], "cdba") is True
assert s.exist([["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "a"],
                ["a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a", "a",
                 "a", "a", "a", "a", "a", "a", "a", "a", "a", "b"]],
               "baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") is True
