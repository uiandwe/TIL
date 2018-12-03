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

map = [
[0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 0,],
[0, 0, 0, 0, 0, 1]]

# map = [
# [0, -1, 0, 0, 0, 0],
# [-1, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 1]]

# map = [
# [1, -1, 0, 0, 0, 0],
# [0, -1, 0, 0, 0, 0],
# [0, 0, 0, 0, -1, 0],
# [0, 0, 0, 0, -1, 1]]

map = [
[-1, 1, 0, 0, 0],
[0, -1, -1, -1, 0],
[0, -1, -1, -1, 0],
[0, -1, -1, -1, 0],
[0, 0, 0, 0, 0]
]
position_x = [1, -1, 0, 0]
position_y = [0, 0, 1, -1]


def dfs(n, m):
    q = Queue()
    while True:

        checkEndFlag = True
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] > 0:
                    if map[i][j] == 1:
                        q.push([i, j])
                    map[i][j] += 1
                elif map[i][j] == 0:
                    checkEndFlag = False

        if q.empty() is True and checkEndFlag is False:
            return (False, -1)

        if checkEndFlag is True:
            step = 0
            for i in map:
                temp_max = max(i)
                if step < temp_max:
                    step = temp_max
            return (True, step)

        while q.empty() is False:
            position = q.pop()
            for i in range(4):
                x = position[0]+position_x[i]
                y = position[1]+position_y[i]

                if x>=0 and x<n and y>=0 and y<m:
                    if map[x][y] == 0:
                        map[x][y] = 1

def solution():
    n = len(map)
    m = len(map[0])
    success, step = dfs(n, m)
    print(success, step-2)


solution()
