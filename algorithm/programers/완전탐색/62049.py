# -*- coding: utf-8 -*-
def solution(n):
    answer = [0, 0, 1]
    if n == 1:
        return [0]
    if n == 2:
        return [0, 0, 1]

    for i in range(3, n+1):
        temp = []
        for j in reversed(answer):
            if j == 0:
                temp.append(1)
            else:
                temp.append(0)
        answer.append(0)
        answer.extend(temp)

    return answer

solution(1)
solution(2)
solution(3)
solution(4)
