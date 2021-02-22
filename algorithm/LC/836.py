# -*- coding: utf-8 -*-
from typing import *

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] < rec2[2] and rec1[2] > rec2[0] and rec1[1] < rec2[3] and rec1[3] > rec2[1]:
            if rec2[0] == rec2[2] or rec2[1] == rec2[3] or rec1[0] == rec1[2] or rec1[1] == rec1[3]:
                return False
            return True
        return False




s = Solution()
assert s.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]) is True
assert s.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]) is False
assert s.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]) is False
assert s.isRectangleOverlap([5,15,8,18], [0,3,7,9]) is False
assert s.isRectangleOverlap([7,8,13,15], [10,8,12,20]) is True
assert s.isRectangleOverlap([2,17,6,20], [3,8,6,20]) is True
assert s.isRectangleOverlap([-1,0,1,1], [0,-1,0,1]) is False
assert s.isRectangleOverlap([-1,0,1,0], [0,-1,1,1]) is False
