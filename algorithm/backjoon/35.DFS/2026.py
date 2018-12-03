class Queue:
    array = []

    def push(self, num):
        self.array.append(num)

    def pop(self):
        if self.size() > 0:
            return self.array.pop(0)

    def size(self):
        return len(self.array)

    def empty(self):
        if len(self.array) > 0:
            return False
        else:
            return True

    def front(self):
        if self.size() > 0:
            return self.array[0]

    def back(self):
        if self.size() > 0:
            top = self.size()
            return self.array[top-1]


edge = [
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
]

visite = [0 for x in range(7+1)]
edgeGroup = [0 for x in range(7+1)]
d = [[0 for x in range(7+1)] for y in range(7+1)]


def solution():
    for i in edge:
        d[i[0]][i[1]] = 1
        d[i[1]][i[0]] = 1
    q = Queue()

    for i in range(len(d[1])):
        if d[1][i] != 0:
            q.push(i)

    while q.empty() is False:
        node = q.pop()
        if visite[node] == 0:
            visite[node] = 1
            edgeGroup[node] = 1

            for i in range(len(d[node])):
                if d[node][i] != 0:
                    q.push(i)

    print(sum(edgeGroup)-1)






solution()





