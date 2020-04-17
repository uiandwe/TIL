# -*- coding: utf-8 -*-

def solution(s):
    answer = []

    s = s.split("},{")
    s[0] = s[0].replace("{{", "")
    s[len(s)-1] = s[len(s)-1].replace("}}", "")

    s = sorted(s, key=lambda k: len(k))
    for idx, val in enumerate(s):
        t = list(set(val.split(",")) - set(answer))
        answer.append(t[0])

    return list(map(int, answer))


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
