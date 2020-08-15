# -*- coding: utf-8 -*-
class Solution:
    def myAtoi(self, str: str) -> int:

        minus = False
        plus = False
        ret = []
        str = str.lstrip()
        for i, c in enumerate(str):
            if c == "-":
                if minus:
                    return 0
                minus = True
                continue
            elif c == "+":
                if plus:
                    return 0
                plus = True
                continue

            if minus and plus:
                return 0

            if c.isnumeric():
                for j in range(i, len(str)):
                    if str[j].isnumeric():
                        ret.append(str[j])
                    else:
                        # if str[j] == '-' or str[j] == '+':
                        #
                        #     return 0
                        break
                break
            else:
                break

        if len(ret) > 0:
            ret = int("".join(ret))
            if minus:
                ret *= -1
        else:
            return 0

        if pow(2, 31) * -1 <= ret <= pow(2, 31) - 1:
            return ret
        elif pow(2, 31) * -1 > ret:
            return pow(2, 31) * -1
        else:
            return pow(2, 31) - 1




if __name__ == '__main__':
    ss = Solution()
    print(ss.myAtoi("   -42"))
    print(ss.myAtoi("3.14159"))
    print(ss.myAtoi("  -0012a42"))
    print(ss.myAtoi("+1"))
    print(ss.myAtoi("010"))
    print(ss.myAtoi("-2147483648"))
    print(ss.myAtoi("0-1"))
    print(ss.myAtoi("-5-"))

