def dfs(i, j, dict, array, ret_int, n):

    if n >= 6:
        dict[ret_int] = ret_int
        return

    position_x = [1, -1, 0, 0]
    position_y = [0, 0, 1, -1]

    for k in range(4):
        next_x = i + position_x[k]
        next_y = j + position_y[k]

        if 0 <= next_x and next_x < 5 and 0 <= next_y and next_y < 5:
            temp_ret_int = ret_int
            ret_int = ret_int * 10 + (array[next_x][next_y])
            dfs(next_x, next_y, dict, array, ret_int, n+1)
            ret_int = temp_ret_int


def solution(array):
    dict = {}
    for i in range(5):
        for j in range(5):
            dfs(i, j, dict, array, array[i][j], 1)

    return len(list(dict.keys()))


