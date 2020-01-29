# -*- coding: utf-8 -*-

import copy


class Queue:
    def __init__(self):
        self.array = []

    def size(self):
        return len(self.array)

    def empty(self):
        return True if self.size() <= 0 else False

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if self.empty() is False:
            return self.array.pop(0)
        return -1


if __name__ == '__main__':

    map = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1]]

    map = [[0, -1, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1]]

    map = [[1, -1, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0],
            [0, 0, 0, 0, -1, 1]]

    map = [[1, -1],
            [-1, 1]]

    map = [[-1, 1, 0, 0, 0],
            [0, -1, -1, -1, 0],
            [0, -1, -1, -1, 0],
            [0, -1, -1, -1, 0],
            [0, 0, 0, 0, 0]]
    m = len(map)
    n = len(map[0])

    q = Queue()

    before_hash = None

    visite = [[0 for x in range(n)] for y in range(m)]

    position_x = [0, 0, 1, -1]
    position_y = [1, -1, 0, 0]
    count = 0

    before_map = copy.deepcopy(map)
    check = True
    while check:

        for y in range(m):
            for x in range(n):
                if map[y][x] == 1 and visite[y][x] == 0:
                    q.push((y, x))

        while q.empty() is False:
            node = q.pop()

            visite[node[0]][node[1]] = 1

            for i in range(4):
                next_x = node[1] + position_x[i]
                next_y = node[0] + position_y[i]

                if 0 <= next_x < n and 0 <= next_y < m and map[next_y][next_x] == 0:
                    map[next_y][next_x] = 1

        if before_map == map:
            check = False
            for temp in map:
                if 0 in temp:
                    count = -1
                    break
        else:
            count += 1
            before_map = copy.deepcopy(map)

            print("=============================")
            for temp in map:
                print(temp)

    print("count", count)
