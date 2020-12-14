# -*- coding: utf-8 -*-

def isPalindrome1(s):
    strs = []

    for ch in s:
        if ch.isalnum():
            strs.append(ch.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True

from collections import deque

def isPalindrome2(s):
    strs = deque()

    for ch in s:
        if ch.isalnum():
            strs.append(ch.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

import re

def isPalindrome3(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]



if __name__ == '__main__':
    s = "abc"
    print(isPalindrome1(s), isPalindrome2(s), isPalindrome3(s))

    s = "ababa"
    print(isPalindrome1(s), isPalindrome2(s), isPalindrome3(s))

    s = "A man, a plan, a canal: Panama"
    print(isPalindrome1(s), isPalindrome2(s), isPalindrome3(s))
