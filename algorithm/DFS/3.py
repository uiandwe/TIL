# -*- coding: utf-8 -*-

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


class Stack:
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
            return self.array.pop()
        return -1


def dfs(start, map, size):

    visit = [0 for x in range(size+1)]

    s = Stack()
    s.push(start)

    while s.empty() is False:
        node = s.pop()

        if visit[node] > 0:
            continue

        visit[node] = 1

        for invisit, value in enumerate(map[node]):
            if value >= 1 and visit[invisit] == 0:
                s.push(invisit)

    print(visit, sum(visit) - 1)

    return


def bfs(start, map, size):
    visit = [0 for x in range(size+1)]

    q = Queue()
    q.push(start)

    while q.empty() is False:
        node = q.pop()

        visit[node] = 1

        for invist, value in enumerate(map[node]):
            if value >= 1 and visit[invist] == 0:
                q.push(invist)

    print(visit, sum(visit) - 1)

    return


def solution(array, m, start):
    map = [[0 for x in range(m+1)] for y in range(m+1)]

    for node in array:
        map[node[0]][node[1]] = 1
        map[node[1]][node[0]] = 1

    for data in map:
        print(data)

    dfs(start, map, m)

    bfs(start, map, m)


solution([
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
], 7, 1)
