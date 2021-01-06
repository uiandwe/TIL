# -*- coding: utf-8 -*-
from operator import itemgetter
class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=itemgetter(2), reverse=True)

        ret = 0
        for i, j in boxTypes:
            i = min(i, truckSize)
            ret += i * j
            truckSize -= i
            if truckSize == 0:
                break
        return ret


s = Solution()
s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
