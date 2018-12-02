map = [[1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,1,1,1,1,0,1],
[1,1,0,1,1,1,1,1,1,0,1],
[1,1,0,1,1,1,1,1,1,0,1],
[1,1,0,0,1,1,0,0,0,0,1],
[1,1,1,0,0,1,0,1,0,0,1],
[1,1,1,1,0,1,0,1,0,0,1],
[1,1,1,1,0,0,0,1,1,0,1],
[1,1,1,1,1,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,1,1,1]]

position_x = [0, 0, -1, 1]
position_y = [1, -1, 0, 0]


def dfs(x, y, step):
    if x == 9 and y == 9:
        return step
    else:
        if map[x][y] == 0:
            step += 1
            map[x][y] = 1
            for i in range(4):
                dfs(position_x[i], position_y[i], step)

            map[x][y] = 0

def solution():
    for i in map:
        print(i)
    print(dfs(1, 1, 1))

solution()
