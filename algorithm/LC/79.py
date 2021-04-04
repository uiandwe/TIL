# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        self.m = len(board)
        self.n = len(board[0])
        visite = [[0] * self.n for _ in range(self.m)]

        def dfs(y, x, s):

            if y < 0 or y >= self.m or x < 0 or x >= self.n or visite[y][x] == 1:
                return False
            if board[y][x] != s[0]:
                return False
            if len(s) == 1:
                return True

            visite[y][x] = 1

            if dfs(y + 1, x, s[1:]): return True
            if dfs(y - 1, x, s[1:]): return True
            if dfs(y, x + 1, s[1:]): return True
            if dfs(y, x - 1, s[1:]): return True
            visite[y][x] = 0
            return False

        for y in range(self.m):
            for x in range(self.n):
                if dfs(y, x, word):
                    return True
        return False


s = Solution()
assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED") is True
assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE") is True
assert s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB") is False
assert s.exist([["a", "b"], ["c", "d"]], "cdba") is True
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
