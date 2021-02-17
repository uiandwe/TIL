# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
            if a < 0 and (len(stack) == 0 or stack[-1] < 0):
                stack.append(a)
            elif a > 0 and (len(stack) == 0 or stack[-1] > 0):
                stack.append(a)
            else:
                f = True
                while stack:
                    if stack[-1] > 0 and a < 0 and (stack[-1] <= abs(a)):
                        top_val = stack.pop()
                        if top_val == abs(a):
                            f = False
                            break
                    else:
                        if stack[-1] > 0 and  a < 0:
                            f = False
                        break

                if f:
                    stack.append(a)

        print(stack)
        return stack


s = Solution()
assert s.asteroidCollision([5, 10, 5]) == [5, 10, 5]
assert s.asteroidCollision([5, 10, -5]) == [5, 10]
assert s.asteroidCollision([8, -8]) == []
assert s.asteroidCollision([10, 2, -5]) == [10]
assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
assert s.asteroidCollision([-2, 2, 1, -2]) == [-2]
assert s.asteroidCollision([-2, -2, 1, -2]) == [-2, -2, -2]
assert s.asteroidCollision([1, 2, 1, -2]) == [1]
