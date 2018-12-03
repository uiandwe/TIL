map = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]

position_x = [1, -1, 0, 0]
position_y = [0, 0, 1, -1]
cnt = 1

def dfs(x, y, n, m):
    map[x][y] = cnt

    for i in range(4):
        dx = x+position_x[i]
        dy = y+position_y[i]

        if dx>=0 and dx < n and dy >= 0 and dy < m:
            if map[dx][dy] == 1:
                dfs(dx, dy, n, m)


def solution():
    m = 7
    n = 7
    global cnt
    for i in range(n):
        for j in range(m):
            if map[i][j] == 1:
                cnt += 1
                dfs(i, j, n, m)

    dict = {}
    for i in map:
        for j in i:
            if j not in dict:
                dict[j] = 1
            else:
                dict[j] +=1

    print(dict)


solution()
