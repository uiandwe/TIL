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
    map = [['W', 'L', 'L', 'W', 'W', 'W', 'L'],
            ['L', 'L', 'L', 'W', 'L', 'L', 'L'],
            ['L', 'W', 'L', 'W', 'L', 'W', 'W'],
            ['L', 'W', 'L', 'W', 'L', 'L', 'L'],
            ['W', 'L', 'L', 'W', 'L', 'W', 'W']]

    m = len(map)
    n = len(map[0])
    visite = [[0 for x in range(n)] for y in range(m)]
    q = Queue()

    position_x = [0, 0, 1, -1]
    position_y = [1, -1, 0, 0]

    length_max = 0

    for y in range(m):
        for x in range(n):

            # 섬 구분
            island_max = 0
            island_max_point = ()

            if map[y][x] == 'L':
                visite[y][x] = 1
                q.push((y, x))

            while q.empty() is False:
                node = q.pop()
                for i in range(4):
                    next_x = node[1] + position_x[i]
                    next_y = node[0] + position_y[i]

                    if 0 <= next_x < n and 0 <= next_y < m \
                            and map[next_y][next_x] == 'L' and visite[next_y][next_x] == 0:
                        q.push((next_y, next_x))
                        visite[next_y][next_x] = visite[node[0]][node[1]] + 1

                        if visite[next_y][next_x] > island_max:
                            island_max_point = (next_y, next_x)
                            island_max = visite[next_y][next_x]

            visite2 = [[0 for x in range(n)] for y in range(m)]

            # 최종점에서 최장길이 계산
            if island_max > 0:
                print(island_max, island_max_point)
                island_max = 0
                q.push(island_max_point)
                visite2[island_max_point[0]][island_max_point[1]] = 1

                while q.empty() is False:
                    node = q.pop()
                    for i in range(4):
                        next_x = node[1] + position_x[i]
                        next_y = node[0] + position_y[i]

                        if 0 <= next_x < n and 0 <= next_y < m and map[next_y][next_x] == 'L'\
                                and visite2[next_y][next_x] == 0:
                            q.push((next_y, next_x))
                            visite2[next_y][next_x] = visite2[node[0]][node[1]] + 1

                            if visite2[next_y][next_x] > island_max:
                                island_max = visite2[next_y][next_x]

                for temp in visite2:
                    print(temp)
                    
                print(island_max-1)


    for temp in map:
        print(temp)

    for temp in visite:
        print(temp)



