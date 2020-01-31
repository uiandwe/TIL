# -*- coding: utf-8 -*-
def solution(H):
    # write your code in Python 3.6

    stack = []
    count = 0
    for x in H:
        while (len(stack) > 0 and stack[len(stack) - 1] > x):
            stack.pop()
        if len(stack) == 0 or stack[len(stack) - 1] < x:
            stack.append(x)
            count += 1
    return count
