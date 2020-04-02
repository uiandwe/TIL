# -*- coding: utf-8 -*-
class Solution:
    """
    XOR
    1. a a b b c d XOR = c^d
    2. c^d 적어도 한 비트 이상 다름
    3. 다른 비트 기준으로  c:0 d:1 나눌수 있음
    4. 전체를 순회하면서 해당 비트가 다른 숫자를 모두 XOR한다.
    5. 4번에서 두번나온 숫자는 XOR로 0이 되고, 결국 두개의 숫자로 나뉜다
    """
    def singleNumber(self, nums):
        xor = 0
        for n in nums:
            xor ^= n
        # print("{0:b}".format(xor))

        idx = 0
        for i in range(64):
            if xor >> i & 1 == 1:
                idx = i
                break

        xor1 = xor2 = 0
        for n in nums:
            if n >> idx & 1 == 1:
                xor1 ^= n
            else:
                xor2 ^= n

        # print(xor1, xor2)
        return xor1, xor2



s = Solution()
# s.singleNumber([1,2,1,3,2,5])
s.singleNumber([-1139700704,-1653765433])
