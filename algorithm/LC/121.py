# -*- coding: utf-8 -*-
class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        min_value = float('inf')

        for price in prices:
            min_value = min(price, min_value)
            profit = max(profit, price-min_value)

        return profit


s = Solution()
assert s.maxProfit([7,1,5,3,6,4]) == 5
assert s.maxProfit([7,6,4,3,1]) == 0
