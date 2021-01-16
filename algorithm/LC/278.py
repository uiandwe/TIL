# -*- coding: utf-8 -*-
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(version):
    d = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
    return d[version]

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        print(left)



s = Solution()
s.firstBadVersion(10)
