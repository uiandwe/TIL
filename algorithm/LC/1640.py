# -*- coding: utf-8 -*-
from typing import *
from collections import defaultdict
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if len(pieces) == 1 and arr != pieces[0]:
            return False

        d = defaultdict(list)

        for l in pieces:
            d[l[0]] = l

        index = 0
        while index < len(arr):
            if arr[index] in d:
                for i in d[arr[index]]:
                    if i == arr[index]:
                        index += 1
                    else:
                        return False
            else:
                return False

        return True

        # result = []
        # for n in arr:
        #     result += d.get(n, [])
        #
        # return arr == result


s = Solution()
assert s.canFormArray(arr = [49,18,16], pieces = [[16,18,49]]) is False
assert s.canFormArray(arr = [91,4,64,78], pieces = [[78],[4,64],[91]]) is True
assert s.canFormArray(arr = [15,88], pieces = [[88],[15]]) is True
assert s.canFormArray(arr = [1,3,5,7], pieces = [[2,4,6,8]]) is False
