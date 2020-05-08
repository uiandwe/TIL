# -*- coding: utf-8 -*-
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    def maxProfit(self, prices):

        if len(prices) <= 1:
            return 0

        d = [0 for i in prices]
        before_profit = -prices[0]

        for i in range(1, len(prices)):
            d[i] = max(d[i - 1], before_profit + prices[i])
            before_profit = max(before_profit, d[i - 2] - prices[i])
        print(d)
        return d[len(prices) - 1]


s = Solution()
s.maxProfit([1,2,3,0,2])
# s.maxProfit([2, 1])
