# -*- coding: utf-8 -*-
from typing import *

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ret = 0
        for i in range(len(piles)//3):
            piles.pop()
            ret += piles.pop()
        return ret
