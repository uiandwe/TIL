# -*- coding: utf-8 -*-
"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

"""

def solution(n):
    temp = ''

    while n > 0:
        temp = chr((ord('A')+((n-1) % 26))) + temp
        n = (n-1) // 26

    return temp


print(solution(1))
print(solution(26))
print(solution(27))
