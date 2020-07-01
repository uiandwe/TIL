# -*- coding: utf-8 -*-
import random
class RandomizedCollection(object):

    def __init__(self):
        self.dic = {}
        self.nums = []
        self.count = 0

    def insert(self, val):
        flag = False
        if val not in self.dic:
            self.dic[val] = set()
            flag = True
        self.dic[val].add(self.count)

        if self.count == len(self.nums):
            self.nums.append(val)
        else:
            self.nums[self.count] = val
        self.count += 1
        return flag

    def remove(self, val):
        if val not in self.dic:
            return False
        pos = self.dic[val].pop()
        if len(self.dic[val]) == 0:
            del self.dic[val]
        # fill with last num
        if pos != self.count - 1:
            self.nums[pos] = self.nums[self.count - 1]
            self.dic[self.nums[pos]].remove(self.count - 1)
            self.dic[self.nums[pos]].add(pos)
        self.count -= 1
        return True

    def getRandom(self):
        return self.nums[random.randint(0, self.count - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
