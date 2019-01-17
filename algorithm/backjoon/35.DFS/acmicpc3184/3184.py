
def dfs(x, y, map, wolfs, sheeps):

    map[x][y] = "#"

    position_x = [1, -1, 0, 0]
    position_y = [0, 0, 1, -1]

    for i in range(4):
        next_x = x + position_x[i]
        next_y = y + position_y[i]

        if next_x >= 0 and next_x < len(map) and next_y >= 0 and next_y < len(map[0]):
            if map[next_x][next_y] != "#":
                if map[next_x][next_y] == ".":
                    map[next_x][next_y] = "#"
                elif map[next_x][next_y] == "v":
                    wolfs.append([next_x, next_y])
                elif map[next_x][next_y] == "o":
                    sheeps.append([next_x, next_y])
                dfs(next_x, next_y, map, wolfs, sheeps)


def findSheepWolf(map):
    sheep = 0
    wolf = 0

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "v":
                wolf += 1
            if map[i][j] == "o":
                sheep += 1

    return [sheep, wolf]


def mapping(wolfs, sheeps, servival, map):
    for position in sheeps:
        if servival is True:
            map[position[0]][position[1]] = "o"
        else:
            map[position[0]][position[1]] = "d"

    for position in wolfs:
        if servival is True:
            map[position[0]][position[1]] = "d"
        else:
            map[position[0]][position[1]] = "v"


def solution(map):

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "v":
                wolfs = []
                sheeps = []
                wolfs.append([i, j])
                dfs(i, j, map, wolfs, sheeps)

                if len(sheeps) > len(wolfs):
                    mapping(wolfs, sheeps, True, map)
                else:
                    mapping(wolfs, sheeps, False, map)

    for i in map:
        print(i)
    return findSheepWolf(map)

