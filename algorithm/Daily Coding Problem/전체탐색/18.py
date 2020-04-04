# -*- coding: utf-8 -*-

def solution(arr):
    ret_arr = []
    for i, item in enumerate(arr):
        if arr[i] is None:
            continue
        compare1 = sorted([x for x in item])

        check = False

        for ana in range(i+1, len(arr)):
            if arr[ana] is None:
                continue

            compare2 = sorted([x for x in arr[ana]])
            if compare1 == compare2:
                arr[ana] = None
                check = True

        if check:
            ret_arr.insert(0, item)
        else:
            ret_arr.append(item)

    return ret_arr

str = ['code', 'doce', 'ecod', 'framer', 'frame']
assert solution(str) == ['code', 'framer', 'frame']
str = ['code', 'aaagmnrs', 'anagrams', 'doce']
assert solution(str) == ['aaagmnrs', 'code']
