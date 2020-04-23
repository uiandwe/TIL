# -*- coding: utf-8 -*-
w = 0
h = 0
map = None
visite = None


def dfs(x, y, step):
    global w, h, map, visite

    visite[y][x] = step

    x_position = [1, -1, 0, 0]
    y_position = [0, 0, 1, -1]

    for i in range(4):
        next_x = x + x_position[i]
        next_y = y + y_position[i]

        if 0 <= next_x < w and 0 <= next_y < h:
            if visite[next_y][next_x] > step+1 and map[next_y][next_x] != -1:
                dfs(next_x, next_y, step+1)


def solution():
    global w, h, map, visite

    visite = [[float('inf') for x in range(w)] for y in range(h)]
    for y in range(h):
        for x in range(w):
            if map[y][x] == 1:
                dfs(x, y, 2)

    answer = -1
    for y in range(h):
        for x in range(w):
            if map[y][x] >= 0:
                if visite[y][x] == float('inf'):
                    return answer
                else:
                    answer = max(answer, visite[y][x]-2)

    print(answer)


if __name__ == '__main__':
    wh_input = input()
    wh_input = wh_input.split(" ")
    w = int(wh_input[0])
    h = int(wh_input[1])

    if w < 2 or 1000 < w or h < 2 or 1000 < h:
        print(-1)

    map = []
    for i in range(h):
        node = input()
        nn = [int(x) for x in node.split(" ")]
        map.append(nn)

    solution()