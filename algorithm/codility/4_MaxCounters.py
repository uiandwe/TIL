# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    d = [0 for x in range(N)]
    max_val = 0
    for i in A:
        if i > N:
            d = [max_val for x in range(N)]
        else:
            d[i-1] += 1
            max_val = max(d[i-1], max_val)

    return d


assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
