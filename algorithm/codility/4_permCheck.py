# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    if len(A) == 0:
        return 0

    for i, v in enumerate(sorted(A)):
        if i+1 != v:
            return 0

    return 1

assert solution([4, 1, 3, 2]) == 1
assert solution([4, 1, 3]) == 0
