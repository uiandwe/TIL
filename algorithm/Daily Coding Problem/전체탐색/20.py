# -*- coding: utf-8 -*-

"""
길이가 같은 두 문자열(string) A 와 B가 주어지면, A 가 B 로 1:1 암호화 가능한지 찾으시오.


Given two strings of equal length, check if two strings can be encrypted 1 to 1.


예제)

Input: “EGG”, “FOO”

Output: True // E->F, G->O


Input: “ABBCD”, “APPLE”

Output: True // A->A, B->P, C->L, D->E


Input: “AAB”, “FOO”

Output: False
"""

def solution(str1, str2):
    d = {}
    for s1, s2 in zip(str1, str2):
        if s1 in d.keys():
            if d[s1] != s2:
                return False
        else:
            d[s1] = s2

    return True


assert solution("EGG", "FOO") is True
assert solution("AAB", "FOO") is False
assert solution("ABBCD", "APPLE") is True
