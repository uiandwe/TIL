# map = [
# [0, 0, 0, 0, 0, 0],
# [0, 0, 2, 0, 1, 0],
# [0, 1, 0, 1, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 1],
# [0, 0, 0, 0, 1, 2]
# ]
# 
# map = [
# [0, 0, 1, 0, 0],
# [0, 0, 2, 0, 1],
# [0, 1, 2, 0, 0],
# [0, 0, 1, 0, 0],
# [0, 0, 0, 0, 2]
# ]


# map = [
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0],
# [1, 2, 0, 0, 0]
# ]

map = [
[0, 2, 0, 1, 0],
[1, 0, 1, 0, 0],
[0, 0, 0, 0, 0],
[2, 0, 0, 1, 1],
[2, 2, 0, 1, 2]
]

permutation = []
pick_len = 0
pick = []
temp_count = []


def dfs(pos):
    if len(pick) == pick_len:
        permutation.append(','.join(str(e) for e in pick))
        return

    for i in range(pos, len(temp_count)):
        pick.append(temp_count[i])
        dfs(i+1)
        pick.pop()


def min_distinct(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def solution(n, m):
    global pick_len, temp_count
    pick_len = m
    home = []
    chicken = []

    for i in range(n):
        for j in range(n):
            if map[i][j] == 2:
                chicken.append([i, j])
            if map[i][j] == 1:
                home.append([i, j])

    temp_count = [x for x in range(0, len(chicken))]
    distinct = []

    dfs(0)

    for p in permutation:
        temp_chicken = p.split(',')
        temp_permutation_distinct = []
        for h in home:
            temp_distinct = float('inf')
            for c in temp_chicken:
                d = min_distinct(h[0], h[1], chicken[int(c)][0], chicken[int(c)][1])
                temp_distinct = min(d, temp_distinct)
            temp_permutation_distinct.append(temp_distinct)
        distinct.append(sum(temp_permutation_distinct))

    print(distinct, min(distinct))

solution(5, 2)
