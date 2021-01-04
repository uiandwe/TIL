# -*- coding: utf-8 -*-
# https://blog.naver.com/yubhh21/220867303992
# 최장 팰린디롬 찾기

def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)


def Manachen(string):
    string = UpdatedString(string)
    print(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2 * C - i

        if R > i:
            LPS[i] = min(R - i, LPS[iMirror])

        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))
    print(LPS)
    print(c-r, c+r)
    print(string[c - r: c + r].replace("#", ""))
    return r


print(Manachen("acaac"))
