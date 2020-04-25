# -*- coding: utf-8 -*-
class Solution:
    def stack(self, S):
        s_stack = []

        for s in S:
            if s == '#':
                if len(s_stack) > 0:
                    s_stack.pop()
            else:
                s_stack.append(s)

        return "".join(s_stack)

    def backspaceCompare(self, S: str, T: str) -> bool:
        print(self.stack(S) == self.stack(T))
        print(self.stack(S) , self.stack(T))
        return self.stack(S) == self.stack(T)


s = Solution()
s.backspaceCompare("y#fo##f", "y#f#o##f")
