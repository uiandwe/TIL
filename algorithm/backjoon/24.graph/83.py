class queue:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        else:
            return -1


    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)


map = []
visit = []
cycle = []

def solution(n, array):
    global map, visit
    map = [[0 for x in range(n+1)] for y in range(n+1)]
    visit = [0 for x in range(n+1)]

    for node in array:
        map[node[0]][node[1]] = 1

    q = queue()
    q.push(1)
    cycle.append(1)

    while q.empty() is False:
        node = q.pop()
        visit[node] = 1
        for i in range(n+1):
            if map[node][i] == 1:
                cycle.append(i)

                if visit[i] == 0:
                    visit[i] = 1
                    q.push(i)
                    
    returnCycle = []
    for i in range(len(cycle)):
        for j in range(i+1, len(cycle)):
            if cycle[j] == cycle[i]: # 사이값들이 사이클
                temp = cycle[i:j+1]
                temp.pop()
                temp = sorted(temp)

                returnCycle.append(temp)

    print(returnCycle)




solution(3, [[1, 2], [2, 3], [3, 2], [2, 1]])


