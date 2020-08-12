# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price: int = prices[0]
        ret_sum = 0
        for i in range(1, len(prices)):
            if prices[i] > min_price:
                ret_sum += prices[i] - min_price
            min_price = prices[i]
        return ret_sum




s = Solution()
assert s.maxProfit([7,1,5,3,6,4]) == 7
assert s.maxProfit([1, 2, 3, 4, 5]) == 4
