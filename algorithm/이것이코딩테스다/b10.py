# -*- coding: utf-8 -*-
text = list(input())

print(text)

result = len(text)
for i in range(1, len(text) + 1):
    temp_text = ""
    temp_count = 1
    before_ch = "".join(text[:i])

    for j in range(i, len(text), i):
        if "".join(text[j:j + i]) == before_ch:
            temp_count += 1
        else:
            if temp_count != 1:
                temp_text += str(temp_count)
            temp_text += "".join(before_ch)
            temp_count = 1
            before_ch = "".join(text[j:j + i])

    if temp_count != 1:
        temp_text += str(temp_count)
    temp_text += "".join(before_ch)
    print(temp_text)
    print("=" * 20)
    result = min(result, len(temp_text))

print(result)

"""
aabbaccc
> 7

ababcdcdababcdcd
> 9     2ababcdcd

abcabcabcabcdedededede
> 14   4abcdedededede


xababcdcdababcdcd
> 17   xababcdcdababcdcd
"""
