class queue():
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(self.size()-1)
        else:
            return -1

    def top(self):
        if self.empty() is False:
            return self.array[0]
        else:
            return -1

    def empty(self):
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.array)

map =[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 5, 1, 0, 0],
    [0, 2, 0, 3, 2, 0, 0],
    [0, 5, 3, 0, 3, 1, 5],
    [0, 1, 2, 3, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 2],
    [0, 0, 0, 5, 0, 2, 0]
]

d = [0 for x in range(7)]
visit = [0 for x in range(7)]

def solution(start):

    q = queue()
    q.push(start)

    for i in range(len(d)):
        if map[start][i] > 0:
            d[i] = map[start][i]
        else:
            d[i] = float('inf')
    d[start] = 0


    while q.empty() is False:
        node = q.pop()
        visit[node] = 1
        for i in range(len(map)):
            if i != node and map[node][i] > 0:
                if d[i] > d[node] + map[node][i]:
                    d[i] = d[node] + map[node][i]
                if visit[i] != 1:
                    q.push(i)

    print(d)

solution(1)
solution(2)
