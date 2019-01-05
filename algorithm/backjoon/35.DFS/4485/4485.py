def dfs(x, y, d, map):
    position_x = [1, -1, 0, 0]
    position_y = [0, 0, 1, -1]
    n = len(map)

    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]

        if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
            if d[next_x][next_y] == 0 or d[x][y] + map[next_x][next_y] < d[next_x][next_y]:
                d[next_x][next_y] = d[x][y] + map[next_x][next_y]

                dfs(next_x, next_y, d, map)


def solution(map):
    d = [[0 for x in range(len(map))] for y in range(len(map))]
    d[0][0] = map[0][0]
    n = len(map)
    for i in range(n):
        for j in range(n):
            dfs(i, j, d, map)


    print(d)
    return d[n-1][n-1]
