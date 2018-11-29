d = []
visit = [0 for x in range(10)]

def DFS(v, total):
    visit[v] = 1

    for i in range(1, total+1):
        if d[v][i] == 1 and visit[i] == 0:
            print("from ", v, " to ", i)
            DFS(i, total)

def solution(total, start, array):

    for i in range(10):
        d.append([0 for x in range(10)])

    for i in array:
        d[i[0]][i[1]] = 1
        d[i[1]][i[0]] = 1


    DFS(start, total)


solution(3, 1, [[1, 2], [1, 3], [2, 3]])
