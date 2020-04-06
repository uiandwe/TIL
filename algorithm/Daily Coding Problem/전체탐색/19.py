# -*- coding: utf-8 -*-
"""
String이 주어지면, 중복된 char가 없는 가장 긴 서브스트링 (substring)의 길이를 찾으시오.


Given a string, find the longest substring that does not have duplicate characters.


예제)

Input: “aabcbcbc”

Output: 3 // “abc”


Input: “aaaaaaaa”

Output: 1 // “a”


Input: “abbbcedd”

﻿Output: 4 // “bced”
"""

def long_substring(s):
    ret_str = []
    temp = ""
    for i in range(len(s)):
        if s[i] in temp:
            ret_str.append(temp)
            index = temp.find(s[i])
            temp = temp[index+1:] + s[i]
        else:
            temp = temp+s[i]

    if len(ret_str) <= 0:
        return s

    ret_len = 0

    for i in ret_str:
        if len(i) > ret_len:
            ret_len = len(i)

    return ret_len



assert long_substring("aabcbcbc") == 3
assert long_substring("aaaaaaaa") == 1
assert long_substring("abbbcedd") == 4
