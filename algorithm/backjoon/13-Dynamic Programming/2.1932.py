d = [
    [-1, 0],
    [-1, 7, -1],
    [-1, 3, 8, -1],
    [-1, 8, 1, 0, -1],
    [-1, 2, 7, 4, 4, -1],
    [-1, 4, 5, 2, 6, 5, -1]
]


for i in range(1, len(d)):
    for j in range(1, len(d[i])-1 ):
        d[i][j] = max(d[i-1][j-1], d[i-1][j])+d[i][j]

print max(d[len(d)-1])
