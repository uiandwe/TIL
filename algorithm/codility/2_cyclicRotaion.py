# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):

    m = len(A)

    if m == 0:
        return A

    share = K // m
    if share > 0:
        K = K % m

    if K == m:
        return A

    for i in range(K):
        p = A.pop(m-1)
        A.insert(0, p)

    return A


assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
assert solution([3, 8, 9, 7, 6], 0) == [3, 8, 9, 7, 6]
assert solution([1, 2, 3], 4) == [3, 1, 2]
assert solution([1, 2, 3], 3) == [1, 2, 3]

