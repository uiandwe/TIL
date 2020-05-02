# -*- coding: utf-8 -*-
from collections import deque
def solution(s):
    temp = ""
    d = [len(s)]

    for j in range(1, (len(s)//2) + 1):
        i = j
        start = 0
        now_str = ""
        index = 0
        check = False

        while i <= len(s):
            check_str = s[start:i]
            if index == 0:
                now_str = s[start:i]
            if now_str != check_str:
                if index == 1:
                    temp += now_str
                else:
                    check = True
                    temp += str(index) + now_str
                now_str = check_str
                index = 0
            start = i
            i += j
            index += 1

        if index == 1:
            temp += check_str
        else:
            check = True
            temp += str(index) + check_str
        temp += s[start:]
        if check:
            d.append(len(temp))
        temp = ""

    return sorted(d)[0]


assert solution("aabbaccc") == 7
assert solution("ababcdcdababcdcd") == 9
assert solution("abcabcdede") == 8
assert solution("abcabcabcabcdededededede") == 14
assert solution("xababcdcdababcdcd") == 17


