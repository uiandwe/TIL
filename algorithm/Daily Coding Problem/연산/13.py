# -*- coding: utf-8 -*-
"""
Spreadsheets often use this alphabetical encoding for its

columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. For example,

given 1, return "A". Given 27, return "AA".

"""

def solution(num):
    answer = []
    while num > 26:
        ch = num % 26
        num = num // 26
        answer.append(chr(int(ch) + 64))
    answer.append(chr(int(num) + 64))

    return "".join(answer)

assert solution(1) == "A"
assert solution(2) == "B"
assert solution(3) == "C"
assert solution(26) == "Z"
assert solution(27) == "AA"
