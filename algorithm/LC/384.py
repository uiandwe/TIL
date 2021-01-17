# -*- coding: utf-8 -*-
from typing import *
from random import shuffle
import copy

class Solution:

    def __init__(self, nums: List[int]):
        self.d = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.d

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        s = copy.deepcopy(self.d)
        shuffle(s)
        return s

# Your Solution object will be instantiated and called as such:
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
print(param_1)
param_2 = obj.shuffle()
print(param_2)
param_1 = obj.reset()
print(param_1)
