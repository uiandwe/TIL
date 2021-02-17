# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        d = [float('inf') for _ in range(amount+1)]
        d[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    d[i] = min(d[i-coins[j]] + 1, d[i])

        # print(d, d[amount])
        if d[amount] == float('inf'):
            return -1
        return d[amount]

s = Solution()
assert s.coinChange([1, 2, 5], 11) == 3
assert s.coinChange([2], 3) == -1
assert s.coinChange([1], 0) == 0
assert s.coinChange([1], 1) == 1
assert s.coinChange([1], 2) == 2
assert s.coinChange([2], 1) == -1
