# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):

    while A % K != 0:
        A += 1

    while B % K != 0:
        B -= 1

    return (B-A)//K+1


assert solution(6, 11, 2) == 3
