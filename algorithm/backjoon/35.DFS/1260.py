map = []
visit = []
class queue:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty():
            return -1
        else:
            return self.array.pop(0)

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)

def dfs(node):
    global visit, map

    print(node)
    visit[node] = 1

    for i in range(len(map[node])):
        if map[node][i] == 1 and visit[i] == 0:
            dfs(i)


def bfs(node, n):
    global visit, map

    q = queue()
    q.push(node)

    while q.empty() is False:
        node = q.pop()
        if visit[node] == 0:
            visit[node] = 1
            print(node)

            for i in range(len(map[node])):
                if map[node][i] == 1 and visit[i] == 0:
                    q.push(i)


def solution(array, start, n):
    global map, visit
    map = [[0 for x in range(n+1)] for y in range(n+1)]
    visit = [0 for x in range(n+1)]

    for node in array:
        map[node[0]][node[1]] = 1
        map[node[1]][node[0]] = 1

    print("dfs")
    dfs(start)

    print("bfs")
    visit = [0 for x in range(n + 1)]
    bfs(start, n)



solution([[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]], 1, 4)
