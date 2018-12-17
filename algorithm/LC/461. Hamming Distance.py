class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y
        a = "{0:b}".format(a)
        ret_count = 0
        for i in str(a):
            if int(i) == 1:
                ret_count += 1

        return ret_count

s = Solution()
print(s.hammingDistance(1, 4))
