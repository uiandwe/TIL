# -*- coding: utf-8 -*-
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            return min(S[i:] + S[:i] for i in range(len(S)))
        return "".join(sorted(S))
