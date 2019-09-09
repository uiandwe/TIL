# -*- coding: utf-8 -*-
def solution(s):
    s = s.lower()
    inner_index = 0
    answer = []
    for index in range(len(s)):
        word = s[index]
        inner_index += 1

        if word == " ":
            inner_index = 0
        elif inner_index % 2:
            word = word.upper()

        answer.append(word)

    return ''.join(answer)


def test_solution():
    assert solution("try hello world") == "TrY HeLlO WoRlD"
    assert solution("fuck you") == "FuCk YoU"
    assert solution("ssibal") == "SsIbAl"
    assert solution("ssi bal") == "SsI BaL"
    assert solution("") == ""
    assert solution("a a") == "A A"
    assert solution("aa aa") == "Aa Aa"
    assert solution("aaa aaa") == "AaA AaA"
    assert solution("aAa aAa") == "AaA AaA"


print(solution("fuck you"))
