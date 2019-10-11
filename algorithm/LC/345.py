# -*- coding: utf-8 -*-
class Solution:
    def reverseVowels(self, s: str) -> str:
        d = []
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        for i, c in enumerate(s):
            if c in vowels:
                d.append((i, c))
        s = list(s)
        for i, item in enumerate(d):
            point = item[0]
            input_c = d[(i+1)*-1]

            s[point] = input_c[1]

        return ''.join(s)



