class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        d = [0 for x in range(n+1)]
        d[0] = d[1] = 1
        if n == 1:
            return 1

        for i in range(2, n+1):
            d[i] = d[i-1] + d[i-2]

        return d[n]



s = Solution()
print(s.climbStairs(2))
print(s.climbStairs(3))
