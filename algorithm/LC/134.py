# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        fual = 0
        for i in range(len(gas)):
            if gas[i] + fual < cost[i]:
                fual = 0
                start = i + 1
            else:
                fual += gas[i] - cost[i]
        return start



s = Solution()
assert s.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2]) == 3
assert s.canCompleteCircuit(gas = [2,3,4], cost = [3,4,3]) == -1
