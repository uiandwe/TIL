map = []
visit = []


def dfs(node):
    global visit

    visit[node] = 1

    for i in range(len(map[node])):
        if map[node][i] == 1 and visit[i] == 0:
            dfs(i)


def solution(array, m, start):
    global map, visit
    map = [[0 for x in range(m+1)] for y in range(m+1)]
    visit = [0 for x in range(m+1)]

    for node in array:
        map[node[0]][node[1]] = 1
        map[node[1]][node[0]] = 1

    dfs(start)

    print(visit, sum(visit)-1)


solution([
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
], 7, 1)


