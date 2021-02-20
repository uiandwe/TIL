# -*- coding: utf-8 -*-
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x:abs(x[0]-x[1]), reverse=True)
        print(costs)
        sm = 0
        countA = countB = len(costs)//2
        for a, b in costs:
            if countA>0 and countB>0:
                if a<b:
                    countA-=1
                    sm += a
                else:
                    countB-=1
                    sm +=b
            elif countA==0:
                sm+=b
            else:
                sm+=a
        return sm
