# -*- coding: utf-8 -*-
from typing import *
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        d = []

        for i in range(len(restaurants)):
            if restaurants[i][2] >= veganFriendly and restaurants[i][3] <= maxPrice and restaurants[i][4] <= maxDistance:
                d.append(restaurants[i])

        temp = sorted(d, key=lambda element: (element[1], element[0]), reverse=True)

        ret = []
        for val in temp:
            ret.append(val[0])

        return ret


s = Solution()
assert s.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10) == [3, 1, 5]
assert s.filterRestaurants([[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
                           0, 50, 10) == [4, 3, 2, 1, 5]
