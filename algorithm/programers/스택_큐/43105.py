def solution(triangle):

    height = len(triangle)
    width = len(triangle[-1])

    d = [[0 for x in range(width)] for y in range(height)]
    d[0][0] = triangle[0][0]

    for index in range(height - 1):
        arr = triangle[index]
        for j, value in enumerate(arr):
            d[index + 1][j] = max(d[index + 1][j], d[index][j] + triangle[index + 1][j])
            d[index + 1][j + 1] = max(d[index + 1][j + 1], d[index][j] + triangle[index + 1][j + 1])

    temp = d[-1]
    return max(temp)


assert solution([[7], [3, 8]]) == 15
assert solution([[7], [3, 8], [8, 1, 0]]) == 18
assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4]]) == 25
assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30
