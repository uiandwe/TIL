# -*- coding: utf-8 -*-
import collections
class Solution:
    def lemonadeChange(self, bills):
        money = collections.defaultdict(int)

        for bill in bills:
            if bill == 5:
                money[5] += 1
            elif bill == 10:
                if money[5] <= 0:
                    return False
                money[5] -= 1
                money[10] += 1
            elif bill == 20:
                if money[5] >= 1 and money[10] >= 1:
                    money[5] -= 1
                    money[10] -= 1
                elif money[5] >= 3:
                    money[5] -= 3
                else:
                    return False
                money[20] += 1
            else:
                return False

        return True



s = Solution()
assert s.lemonadeChange([5, 5, 5, 10, 20]) is True
assert s.lemonadeChange([5, 5, 10, 10, 20]) is False
assert s.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]) is True
