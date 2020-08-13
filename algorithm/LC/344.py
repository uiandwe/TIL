# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i], s[l-i-1] = s[l-i-1], s[i]
