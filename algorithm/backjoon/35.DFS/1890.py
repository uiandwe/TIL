map = [
[2, 3, 3, 1],
[1, 2, 1, 3],
[1, 2, 3, 1],
[3, 1, 1, 0]
]

min_step = float('inf')
position_x = [0, 1]
position_y = [1, 0]

def dfs(x, y, step):
    global min_step
    if x == 3 and y == 3:
        if step < min_step:
            min_step = step
        return

    c = map[x][y]
    for i in range(2):
        dx = x + ((c*position_x[i]))
        dy = y + ((c*position_y[i]))
        if dx >= 0 and dx < 4 and dy >= 0 and dy < 4:
            dfs(dx, dy, step+1)

def solution():
    dfs(0, 0, 0)

    print(min_step)

solution()
