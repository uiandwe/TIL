# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    l = len(A)
    if l <= 0:
        return 0

    if l == 1 and A[0] != 1:
        return 1

    s = (l+1) * (l+1+1) // 2
    return s - sum(A)


assert solution([1, 3]) == 2
assert solution([2, 3, 1, 5]) == 4
assert solution([]) == 0
assert solution([2]) == 1
