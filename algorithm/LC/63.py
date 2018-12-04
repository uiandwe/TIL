map = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]


def solution():
    d = [[0 for x in range(len(map))] for y in range(len(map[0]))]
    d[0][0] = 1

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                d[i][j] = 0
            else:
                if i > 0:
                    d[i][j] += d[i-1][j]
                if j > 0:
                    d[i][j] += d[i][j-1]

    for i in d:
        print(i)


solution()
