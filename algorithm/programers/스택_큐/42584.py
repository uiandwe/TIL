# -*- coding: utf-8 -*-

def solution(prices):
    answer = [0 for x in prices]
    s = [(prices[0], 0)]

    for index in range(1, len(prices)):
        value = prices[index]
        while s and s[len(s)-1][0] > value:
            t = s.pop(len(s)-1)
            answer[t[1]] = index - t[1]
        s.append((value, index))

    for item in s:
        answer[item[1]] = len(prices) - 1 - (item[1])
    return answer


print(solution([2, 1]))

assert solution([1, 2, 3, 2, 3]) == [4, 3, 1, 1, 0]
assert solution([1, 2, 3]) == [2, 1, 0]
assert solution([1, 2]) == [1, 0]
assert solution([2, 1]) == [1, 0]



# print(solution([2, 1]))



