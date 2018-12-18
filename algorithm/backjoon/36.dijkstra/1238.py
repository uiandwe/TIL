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

    def duplication(self, data):
        if self.empty():
            return False
        else:
            for i in self.array:
                if i == data:
                    return True

map = []
path = [
[1, 2, 4],
[1, 3, 2],
[1, 4, 7],
[2, 1, 1],
[2, 3, 5],
[3, 1, 2],
[3, 4, 4],
[4, 2, 3]
]
visiteWeight = []
visite = []
retWedight = []


def dijkstra(node):
    global visiteWeight, map, visite
    visiteWeight[node][node] = 0
    visite[node] = 1

    q = queue()
    q.push(node)

    while q.empty() is False:
        now_node = q.pop()
        visite[now_node] = 1
        for i in range(1, len(map[now_node])):
            pathWeight = map[now_node][i]

            if visite[i] == 0 and pathWeight >= 1:

                if q.duplication(i) is False:
                    q.push(i)

                if visiteWeight[node][i] > pathWeight + visiteWeight[node][now_node]:
                    visiteWeight[node][i] = pathWeight + visiteWeight[node][now_node]


def finialPathWeight():
    global retWedight
    retWedight = [[0 for x in range(4+1)] for y in range(4+1)]

    for i in range(len(visiteWeight)):
        for j in range(len(visiteWeight[i])):
            if i != j:
                retWedight[i][j] = visiteWeight[i][j] + visiteWeight[j][i]


def solution():
    global map, visiteWeight, visite
    map = [[0 for x in range(4+1)] for y in range(4+1)]
    visiteWeight = [[0 for x in range(4+1)] for y in range(4+1)]

    for n in path:
        map[n[0]][n[1]] = n[2]

    for i in range(1, 4+1):
        visite = [0 for x in range(4 + 1)]
        for j in range(1, 4+1):
            val = map[i][j]
            if val > 0:
                visiteWeight[i][j] = map[i][j]
            else:
                visiteWeight[i][j] = float('inf')
        dijkstra(i)

    finialPathWeight()

    for i in retWedight:
        print(i)



solution()
