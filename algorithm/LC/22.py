# -*- coding: utf-8 -*-
class Solution:
    def generateParenthesis(self, n: int):
        ret = []
        self.recursive(n, 0, 0, "", ret)
        return ret

    def recursive(self, n, open, close, str, ret):
        if open == n and close == n:
            ret.append(str)
            return ret

        if open < n:
            self.recursive(n, open+1, close, str+"(", ret)

        if open > close:
            self.recursive(n, open, close+1, str+")", ret)

s = Solution()
print(s.generateParenthesis(3))
