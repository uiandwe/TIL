map = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

def solution():
    d = [[float('inf') for x in map[0]] for y in map]
    d[0][0] = map[0][0]

    for i in range(len(map)):
        for j in range(len(map[0])):
            if i-1 >= 0:
                d[i][j] = min(map[i][j]+d[i-1][j], d[i][j])
            if j-1 >= 0:
                d[i][j] = min(map[i][j] + d[i][j-1], d[i][j])

    print(d)


solution()
