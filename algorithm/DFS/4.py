# -*- coding: utf-8 -*-

class Queue:
    def __init__(self):
        self.array = []

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.empty():
            return -1
        return self.array.pop(0)

    def size(self):
        return len(self.array)

    def empty(self):
        return True if self.size() <= 0 else False


def dfs(y, x, visit, count, map):
    q = Queue()
    q.push((y, x))
    max_size = len(visit)

    position_x = [0, 0, 1, -1]
    position_y = [1, -1, 0, 0]

    while q.empty() is False:
        node = q.pop()
        visit[node[0]][node[1]] = count

        for i in range(4):
            next_x = node[1]+position_x[i]
            next_y = node[0]+position_y[i]
            if 0 <= next_x < max_size and 0 <= next_y < max_size \
                    and visit[next_y][next_x] == 0 and map[next_y][next_x] == 1:
                q.push((next_y, next_x))


if __name__ == '__main__':

    map = [
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 0]
    ]

    start_x = 0
    start_y = 0
    size = 7
    count = 2

    visit = [[0 for x in range(size)] for y in range(size)]

    for y in range(start_y, size):
        for x in range(start_x, size):
            if map[y][x] == 1 and visit[y][x] == 0:
                dfs(y, x, visit, count, map)
                count += 1

    max_visit = 0
    visit_count = {}
    for v in visit:

        max_visit = max(max(v), max_visit)
        for house in v:
            if house in visit_count.keys():
                visit_count[house] += 1
            else:
                visit_count[house] =1

    print(max_visit-1)
    print(visit_count)




