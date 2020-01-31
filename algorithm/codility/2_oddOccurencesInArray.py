# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    b_temp = 0

    for i in A:
        b_temp = b_temp ^ i

    return b_temp

assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
