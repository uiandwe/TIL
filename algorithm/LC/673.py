# -*- coding: utf-8 -*-
from collections import Counter

class Solution:
    def findNumberOfLIS(self, nums):
        if len(nums) <= 0:
            return 0

        n = len(nums)
        m, dp, cnt = 0, [1] * n, [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] < dp[j] + 1:
                        dp[i], cnt[i] = dp[j] + 1, cnt[j]
                    elif dp[i] == dp[j] + 1:
                        cnt[i] += cnt[j]
            m = max(m, dp[i])

        # print(dp)
        # print(cnt)

        max_length = max(dp)
        count = 0
        for l, c in zip(dp, cnt):
            if l == max_length:
                count += c
        return count

s = Solution()
# assert s.findNumberOfLIS([1,3,5,4,7,6]) == 4
assert s.findNumberOfLIS([1,2,4,3,5,4,7,2]) == 3
