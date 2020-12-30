# -*- coding: utf-8 -*-
class Solution:
    def merge(self, intervals):
        merged = []
        for i in sorted(intervals, key=lambda x: x[0]):

            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged.append(i)
        return merged




s = Solution()
# s.merge([[1,3]])
s.merge([[1,3],[2,6],[8,10],[15,18]])
# s.merge([[1,4],[4,6]])
# s.merge([[1,4],[5,6]])
