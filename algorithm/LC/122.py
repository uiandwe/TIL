class Solution:
    def maxProfit(self, prices):
        d = [0 for _ in range(len(prices))]

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                d[i] = prices[i] - prices[i - 1]

        return sum(d)


s = Solution()
print(s.maxProfit([7,1,5,3,6,4]))
print(s.maxProfit([1, 2, 3, 4, 5]))