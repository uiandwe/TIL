class Solution:
    def isHappy(self, n: int) -> bool:
        d = []

        while True:
            if n in d:
                return False
            d.append(n)

            temp = 0
            while n >= 10:
                t = n % 10
                temp += t * t
                n = n // 10
            temp += n * n

            if temp == 1:
                return True

            n = temp




s = Solution()
print(s.isHappy(19))