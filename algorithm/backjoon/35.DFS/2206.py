map = [
[0,1,0,0],
[1,1,1,0],
[1,0,0,0],
[0,0,0,0],
[0,1,1,1],
[0,0,0,0]
]

map = [
[0,1,1,1],
[1,1,1,1],
[1,1,1,1],
[1,1,1,0]
]

ret_min = float('inf')

position_x = [1, -1, 0, 0]
position_y = [0, 0, 1, -1]

map_x = 0
map_y = 0

def dfs(x, y, step):
    global ret_min, map

    if len(map)-1 <= x and len(map[0])-1 <= y:
        if ret_min > step:
            ret_min = step
        return

    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]
        if next_x >= 0 and next_x <= len(map)-1 and next_y >= 0 and next_y <= len(map[0])-1:
            if map[next_x][next_y] == 0:
                map[next_x][next_y] = 1
                dfs(next_x, next_y, step+1)
                map[next_x][next_y] = 0


def solution():
    global map

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                map[i][j] = 0

                dfs(0, 0, 1)

                map[i][j] = 1

    print(ret_min)


solution()
