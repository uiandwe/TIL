map = [ [1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,1,1,1,1,1,1,0,1],
        [1,1,0,1,1,1,1,1,1,0,1],
        [1,1,0,1,1,1,1,1,1,1,1],
        [1,1,0,0,1,1,0,0,0,0,1],
        [1,1,1,0,0,1,0,1,0,0,1],
        [1,1,1,1,0,1,0,1,0,0,1],
        [1,1,1,1,0,0,0,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,1,1]]

position_x = [0, 0, -1, 1]
position_y = [1, -1, 0, 0]
min_step = float('inf')

def dfs(x, y, step):
    global min_step
    if x == 9 and y == 9:
        if min_step > step:
            min_step = step
    else:
        if map[x][y] == 0:
            step += 1
            map[x][y] = 1
            for i in range(4):
                dfs(x+position_x[i], y+position_y[i], step)

            map[x][y] = 0

def solution():
    for i in map:
        print(i)
    dfs(1, 1, 1)
    print(min_step)

solution()
