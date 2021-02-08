# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            print(left, right, op)
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                # results.extend(compute(left, right, value))
                results.append((left, right, value))
                print(results)
        return results
s = Solution()
# s.diffWaysToCompute("2-1-1")
s.diffWaysToCompute("2*3-4*5")

